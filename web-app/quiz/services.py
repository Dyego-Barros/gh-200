import secrets
import time
from uuid import uuid4
from collections import defaultdict
from sqlalchemy import select
from .models import Attempt, AttemptItem, Question



class StudyService:
    def __init__(self, db):
        self.db = db

    LEVELS = ('Básico', 'Intermediário', 'Avançado')

    def start(self, owner, levels=None):
        selected = set(self.LEVELS if levels is None else levels)
        if not selected or not selected.issubset(self.LEVELS):
            raise ValueError('Selecione pelo menos um nível válido.')
        active_attempts = self.db.scalars(select(Attempt).where(
            Attempt.owner == owner, Attempt.finished_at.is_(None)
        ).order_by(Attempt.started_at.desc())).all()
        for active in active_attempts:
            if active.deadline > int(time.time()) and {i.question.level for i in active.items} == selected:
                return active
        pools = {
            level: list(self.db.scalars(select(Question).where(
                Question.level == level, Question.is_active.is_(True)
            ))) for level in self.LEVELS if level in selected
        }
        if any(not pool for pool in pools.values()):
            raise ValueError('Há um nível selecionado sem questões disponíveis.')
        # Distribute evenly, redistributing vacancies when a level has fewer questions.
        rng = secrets.SystemRandom()
        for pool in pools.values():
            rng.shuffle(pool)
        chosen = []
        while len(chosen) < 60 and any(pools.values()):
            for pool in pools.values():
                if pool and len(chosen) < 60:
                    chosen.append(pool.pop())
        rng.shuffle(chosen)
        now = int(time.time())
        attempt = Attempt(id=str(uuid4()), owner=owner, started_at=now, deadline=now + 6000)
        attempt.items = [AttemptItem(question=q, position=i) for i, q in enumerate(chosen, 1)]
        self.db.add(attempt)
        self.db.commit()
        return attempt

    def save(self, attempt, answers, finish=False):
        now = int(time.time())
        if attempt.finished_at is not None:
            return
        if now >= attempt.deadline:
            attempt.finished_at = attempt.deadline
        else:
            valid = {str(item.id): item for item in attempt.items}
            if any(key not in valid or value not in 'ABCD' or len(value) != 1 for key, value in answers.items()):
                raise ValueError('Resposta inválida ou questão fora desta rodada.')
            for key, value in answers.items():
                valid[key].answer = value
            if finish:
                attempt.finished_at = now
        self.db.commit()

    @staticmethod
    def result(attempt):
        domains, levels = defaultdict(lambda: [0, 0]), defaultdict(lambda: [0, 0])
        correct = answered = 0
        for item in attempt.items:
            hit = int(item.answer == item.question.correct)
            correct += hit
            answered += item.answer is not None
            for groups, key in ((domains, item.question.domain), (levels, item.question.level)):
                groups[key][0] += hit
                groups[key][1] += 1
        total = len(attempt.items)
        return dict(correct=correct, total=total, answered=answered, percent=100 * correct / total, domains=dict(sorted(domains.items())), levels=dict(levels))
