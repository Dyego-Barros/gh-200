import os
from pathlib import Path
import secrets
import time
import click
from flask import Flask, abort, flash, g, jsonify, redirect, render_template, request, session, url_for
from flask_wtf.csrf import CSRFProtect
from sqlalchemy import create_engine, event, select, func
from sqlalchemy.orm import sessionmaker
from .models import Attempt, Question
from .services import StudyService
from .database import DatabaseManager

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / 'questionario.md'


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True, instance_path=str(ROOT / 'instance'))
    Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    key_path = Path(app.instance_path) / 'secret.key'
    if not key_path.exists():
        try:
            with key_path.open('x') as file:
                os.chmod(key_path, 0o600)
                file.write(secrets.token_hex(32))
        except FileExistsError:
            pass
    app.config.from_mapping(SECRET_KEY=os.environ.get('SECRET_KEY') or key_path.read_text(), DATABASE_URL=os.environ.get('DATABASE_URL', f'sqlite:///{app.instance_path}/quiz.sqlite'), WTF_CSRF_TIME_LIMIT=7200, SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE='Lax', MAX_CONTENT_LENGTH=128*1024)
    if config:
        app.config.update(config)
    CSRFProtect(app)
    engine = create_engine(app.config['DATABASE_URL'], connect_args={'timeout': 20})
    @event.listens_for(engine, 'connect')
    def foreign_keys(connection, _):
        connection.execute('PRAGMA foreign_keys=ON')
    factory = sessionmaker(engine)
    app.extensions['db_engine'] = engine
    database = DatabaseManager(engine, ROOT)
    app.extensions['database'] = database

    @app.before_request
    def open_db():
        g.db = factory()
        session.setdefault('owner', secrets.token_hex(32))
        # Serialize mutations so a stale autosave cannot modify a finished attempt.
        if request.method == 'POST':
            g.db.connection().exec_driver_sql('BEGIN IMMEDIATE')

    @app.teardown_request
    def close_db(error=None):
        if 'db' in g:
            g.db.close()

    def owned_attempt(attempt_id):
        attempt = g.db.scalar(select(Attempt).where(Attempt.id == attempt_id, Attempt.owner == session['owner']))
        if attempt is None:
            abort(404)
        return attempt

    @app.get('/')
    def index():
        attempts = g.db.scalars(select(Attempt).where(Attempt.owner == session['owner']).order_by(Attempt.started_at.desc()).limit(20)).all()
        counts = g.db.execute(select(Question.level, func.count()).where(Question.is_active.is_(True)).group_by(Question.level)).all()
        return render_template('index.html', attempts=attempts, counts=dict(counts), now=int(time.time()))

    @app.post('/rodadas')
    def start():
        try:
            levels = request.form.getlist('levels') if 'level_filter' in request.form or 'levels' in request.form else None
            attempt = StudyService(g.db).start(session['owner'], levels=levels)
        except ValueError as error:
            flash(str(error), 'warning')
            return redirect(url_for('index'))
        return redirect(url_for('study', attempt_id=attempt.id))

    @app.route('/rodadas/<attempt_id>', methods=['GET', 'POST'])
    def study(attempt_id):
        attempt = owned_attempt(attempt_id)
        service = StudyService(g.db)
        if request.method == 'POST':
            answers = {key[2:]: value for key, value in request.form.items() if key.startswith('q_')}
            try:
                service.save(attempt, answers, finish=request.form.get('action') == 'finish')
            except ValueError as error:
                abort(400, str(error))
            if request.headers.get('X-Autosave') == '1':
                return jsonify(finished=attempt.finished_at is not None)
            if attempt.finished_at is None:
                flash('Respostas salvas.', 'success')
        elif attempt.finished_at is None and int(time.time()) >= attempt.deadline:
            service.save(attempt, {})
        if attempt.finished_at is not None:
            return render_template('result.html', attempt=attempt, result=service.result(attempt))
        return render_template('study.html', attempt=attempt, remaining=max(0, attempt.deadline-int(time.time())))

    @app.cli.command('init-db')
    def init_db():
        """Aplica as migrações Alembic."""
        database.migrate()
        click.echo('Banco atualizado.')

    @app.cli.command('import-questions')
    @click.option('--source', type=click.Path(exists=True, path_type=Path), default=SOURCE)
    def import_questions(source):
        """Importa e valida o questionário Markdown completo."""
        try:
            count = database.import_questions(source)
        except (ValueError, OSError) as error:
            raise click.ClickException(str(error)) from error
        click.echo(f'{count} questões importadas.' if count else 'Fonte já importada e conferida; nenhuma alteração.')

    @app.cli.command('setup')
    @click.pass_context
    def setup(ctx):
        """Prepara ou atualiza o banco e importa a fonte Markdown."""
        ctx.invoke(init_db)
        ctx.invoke(import_questions)

    return app
