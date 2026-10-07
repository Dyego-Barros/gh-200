from collections import Counter
import pytest
from sqlalchemy import select, func
from sqlalchemy.orm import Session
from quiz import create_app, SOURCE
from quiz.importer import QuestionnaireImporter
from quiz.models import Question, Attempt
from quiz.services import StudyService


@pytest.fixture
def app(tmp_path):
    app = create_app({'TESTING': True, 'WTF_CSRF_ENABLED': False, 'DATABASE_URL': f'sqlite:///{tmp_path}/test.sqlite', 'SECRET_KEY': 'test-only'})
    assert app.test_cli_runner().invoke(args=['init-db']).exit_code == 0
    assert app.test_cli_runner().invoke(args=['import-questions']).exit_code == 0
    yield app
    app.extensions['db_engine'].dispose()


def test_source_and_idempotency(app):
    rows = QuestionnaireImporter().parse(SOURCE)
    assert Counter(r['level'] for r in rows) == {'Básico': 46, 'Intermediário': 75, 'Avançado': 59}
    assert rows[0]['correct'] == 'A'
    assert rows[-1]['correct'] == 'C'
    assert rows[10]['correct'] == 'B'
    with Session(app.extensions['db_engine']) as db:
        assert QuestionnaireImporter().import_file(db, SOURCE) == 0
        for row in rows:
            question = db.scalar(select(Question).where(Question.number == row['number']))
            assert all(getattr(question, key) == value for key, value in row.items())
        assert db.scalar(select(func.count()).select_from(Question)) == 180


def test_corrupt_import_is_atomic(app, tmp_path):
    target = tmp_path / 'broken.md'
    target.write_text(SOURCE.read_text().replace('- **A.** .github/workflows', '- **Z.** .github/workflows'))
    with Session(app.extensions['db_engine']) as db:
        with pytest.raises(ValueError):
            QuestionnaireImporter().import_file(db, target)
        assert db.scalar(select(func.count()).select_from(Question)) == 180


def test_round_balance_resume_and_score(app):
    with Session(app.extensions['db_engine']) as db:
        service = StudyService(db)
        attempt = service.start('owner')
        assert attempt.deadline - attempt.started_at == 6000
        assert len({i.question_id for i in attempt.items}) == 60
        assert Counter(i.question.level for i in attempt.items) == {'Básico': 20, 'Intermediário': 20, 'Avançado': 20}
        assert service.start('owner').id == attempt.id
        answers = {str(i.id): i.question.correct for i in attempt.items[:30]}
        service.save(attempt, answers, finish=True)
        result = service.result(attempt)
        assert result['correct'] == 30 and result['percent'] == 50
        assert result['answered'] == 30
        assert sum(v[0] for v in result['domains'].values()) == 30
        assert sum(v[1] for v in result['levels'].values()) == 60
        service.save(attempt, {str(i.id): i.question.correct for i in attempt.items})
        assert service.result(attempt)['correct'] == 30
        assert service.start('owner').id != attempt.id


def test_expiry_rejects_late_answers(app, monkeypatch):
    with Session(app.extensions['db_engine']) as db:
        service = StudyService(db)
        attempt = service.start('owner')
        first = attempt.items[0]
        service.save(attempt, {str(first.id): first.question.correct})
        monkeypatch.setattr('quiz.services.time.time', lambda: attempt.deadline)
        service.save(attempt, {str(i.id): i.question.correct for i in attempt.items}, finish=True)
        assert attempt.finished_at == attempt.deadline
        assert service.result(attempt)['correct'] == 1


def test_invalid_answers_no_partial_save(app):
    with Session(app.extensions['db_engine']) as db:
        service = StudyService(db)
        attempt = service.start('owner')
        with pytest.raises(ValueError):
            service.save(attempt, {str(attempt.items[0].id): 'A', '999999': 'B'})
        assert all(i.answer is None for i in attempt.items)
        with pytest.raises(ValueError):
            service.save(attempt, {str(attempt.items[0].id): 'AB'})


def test_web_flow_ownership_and_no_key_leak(app):
    client = app.test_client()
    assert client.get('/').status_code == 200
    response = client.post('/rodadas')
    location = response.headers['Location']
    page = client.get(location)
    assert page.status_code == 200
    assert b'Gabarito:' not in page.data
    with Session(app.extensions['db_engine']) as db:
        attempt = db.scalar(select(Attempt))
        item = attempt.items[0]
        answer = {f'q_{item.id}': item.question.correct}
    saved = client.post(location, data=answer, headers={'X-Autosave': '1'})
    assert saved.json == {'finished': False}
    assert b'checked' in client.get(location).data
    stranger = app.test_client()
    assert stranger.get(location).status_code == 404
    assert stranger.post(location, data=answer).status_code == 404
    result = client.post(location, data={'action':'finish'})
    assert result.status_code == 200
    assert b'1/60' in result.data
    assert b'Gabarito:' in result.data


def test_csrf(app):
    app.config['WTF_CSRF_ENABLED'] = True
    assert app.test_client().post('/rodadas').status_code == 400


def test_updated_source_preserves_history(app, tmp_path):
    with Session(app.extensions['db_engine']) as db:
        service = StudyService(db)
        old_attempt = service.start('old-owner')
        old_ids = {item.question_id for item in old_attempt.items}
        service.save(old_attempt, {str(i.id): i.question.correct for i in old_attempt.items}, finish=True)
        updated = tmp_path / 'updated.md'
        updated.write_text(SOURCE.read_text().replace('**Resposta: A.**', '**Resposta: D.**', 1))
        assert QuestionnaireImporter().import_file(db, updated) == 180
        assert QuestionnaireImporter().import_file(db, updated) == 0
        assert service.result(old_attempt)['correct'] == 60
        new_attempt = service.start('new-owner')
        assert old_ids.isdisjoint({i.question_id for i in new_attempt.items})
        assert db.scalar(select(func.count()).select_from(Question).where(Question.is_active.is_(True))) == 180


def test_fresh_setup_and_csrf_flow(tmp_path):
    import re
    app = create_app({'TESTING': True, 'SECRET_KEY': 'test', 'DATABASE_URL': f'sqlite:///{tmp_path}/fresh.sqlite'})
    try:
        runner = app.test_cli_runner()
        result = runner.invoke(args=['setup'])
        assert result.exit_code == 0, result.output
        assert runner.invoke(args=['setup']).exit_code == 0
        client = app.test_client()
        page = client.get('/')
        token = re.search(r'name="csrf_token" value="([^"]+)"', page.text)[1]
        started = client.post('/rodadas', data={'csrf_token': token})
        assert started.status_code == 302
        study = client.get(started.location)
        assert study.status_code == 200
        assert study.text.count('<fieldset') == 60
        finished = client.post(started.location, data={'csrf_token': token, 'action': 'finish'})
        assert finished.status_code == 200
        assert '0/60' in finished.text
    finally:
        app.extensions['db_engine'].dispose()


@pytest.mark.parametrize('old,new', [
    ('### GH200-002', '### GH200-001'),
    ('· Básico', '· Desconhecido'),
    ('**Resposta: A.**', '**Resposta: Z.**'),
])
def test_invalid_markdown_rejected(tmp_path, old, new):
    source = tmp_path / 'invalid.md'
    source.write_text(SOURCE.read_text().replace(old, new, 1))
    with pytest.raises(ValueError):
        QuestionnaireImporter().parse(source)


@pytest.mark.parametrize('levels,expected', [
    (['Básico'], {'Básico': 46}),
    (['Intermediário'], {'Intermediário': 60}),
    (['Avançado'], {'Avançado': 59}),
    (['Básico', 'Avançado'], {'Básico': 30, 'Avançado': 30}),
    (['Básico', 'Intermediário'], {'Básico': 30, 'Intermediário': 30}),
    (['Intermediário', 'Avançado'], {'Intermediário': 30, 'Avançado': 30}),
])
def test_filtered_rounds(app, levels, expected):
    client = app.test_client()
    response = client.post('/rodadas', data={'level_filter': '1', 'levels': levels})
    assert response.status_code == 302
    with Session(app.extensions['db_engine']) as db:
        attempt = db.get(Attempt, response.location.rsplit('/', 1)[1])
        assert Counter(i.question.level for i in attempt.items) == expected
        total = sum(expected.values())
        assert len({i.question_id for i in attempt.items}) == total
        assert attempt.deadline - attempt.started_at == 6000
        answers = {f'q_{i.id}': i.question.correct for i in attempt.items}
    page = client.get(response.location)
    assert f'de {total}</legend>' in page.text
    result = client.post(response.location, data={**answers, 'action': 'finish'})
    assert f'{total}/{total}' in result.text
    assert '100.0%' in result.text


def test_filter_resume_and_validation(app):
    client = app.test_client()
    basic = client.post('/rodadas', data={'levels': ['Básico']}).location
    advanced = client.post('/rodadas', data={'levels': ['Avançado']}).location
    assert basic != advanced
    assert client.post('/rodadas', data={'levels': ['Básico']}).location == basic
    for data in ({'level_filter': '1'}, {'levels': ['Inválido']}):
        response = client.post('/rodadas', data=data, follow_redirects=True)
        assert 'Selecione pelo menos um nível válido.' in response.text
    with Session(app.extensions['db_engine']) as db:
        assert db.scalar(select(func.count()).select_from(Attempt)) == 2
