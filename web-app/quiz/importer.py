"""Importação atômica do questionário Markdown, com versões para o histórico."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import re
from sqlalchemy import select, update
from .models import Question


class QuestionnaireImporter:
    LEVELS = {'Básico', 'Intermediário', 'Avançado'}

    def parse(self, path):
        data = Path(path).read_bytes()
        text = data.decode('utf-8-sig')
        title = re.search(r'^# .+ — (\d+) questões', text, re.M)
        if not title:
            raise ValueError('O título deve informar o total de questões.')
        rows = []
        domain = None
        # Split at every heading so malformed question headings cannot be skipped.
        sections = re.split(r'(?=^#{2,3} )', text, flags=re.M)
        for section in sections:
            heading, _, body = section.partition('\n')
            if heading.startswith('## '):
                if not re.fullmatch(r'## Domínio \d+ .+', heading):
                    raise ValueError(f'Domínio inválido: {heading}')
                domain = heading[3:]
            elif heading.startswith('### '):
                match = re.fullmatch(r'### GH200-(\d+) · (.+)', heading)
                if not match or match[2] not in self.LEVELS or not domain:
                    raise ValueError(f'Identificação ou nível inválido: {heading}')
                statement, separator, remainder = body.partition('- **A.** ')
                if not separator or not statement.strip():
                    raise ValueError(f'Enunciado ou alternativa A ausente: {heading}')
                options_text, details, key_text = (separator + remainder).partition('<details>')
                options = re.findall(r'^- \*\*([A-D])\.\*\* (.+)$', options_text, re.M)
                if [letter for letter, _ in options] != list('ABCD'):
                    raise ValueError(f'Alternativas inválidas: {heading}')
                if options_text.strip() != '\n'.join(f'- **{letter}.** {value}' for letter, value in options):
                    raise ValueError(f'Texto de alternativas inválido: {heading}')
                answers = re.findall(r'^\*\*Resposta: ([A-D])\.\*\* (.+)$', key_text, re.M)
                if not details or len(answers) != 1 or '</details>' not in key_text:
                    raise ValueError(f'Gabarito ausente ou duplicado: {heading}')
                rows.append(dict(number=int(match[1]), domain=domain, level=match[2],
                                 statement=statement.strip(), **{k.lower(): v for k, v in options},
                                 correct=answers[0][0], explanation=answers[0][1],
                                 source_hash=sha256(data).hexdigest()))
        numbers = [row['number'] for row in rows]
        if len(numbers) != int(title[1]) or set(numbers) != set(range(1, int(title[1]) + 1)):
            raise ValueError('Questões duplicadas, ausentes ou total divergente do título.')
        counts = Counter(row['level'] for row in rows)
        if any(counts[level] < 20 for level in self.LEVELS):
            raise ValueError('São necessárias pelo menos 20 questões de cada nível.')
        return rows

    def import_file(self, db, path):
        rows = self.parse(path)
        source_hash = rows[0]['source_hash']
        existing = db.scalars(select(Question).where(Question.source_hash == source_hash)).all()
        if existing:
            by_number = {q.number: q for q in existing}
            if len(existing) != len(rows) or not all(
                r['number'] in by_number and all(getattr(by_number[r['number']], k) == v for k, v in r.items())
                for r in rows
            ):
                raise ValueError('Dados persistidos divergem da fonte. Importação cancelada.')
            if all(q.is_active for q in existing):
                return 0
        # Keep old questions unchanged: completed and ongoing rounds reference their IDs.
        db.execute(update(Question).values(is_active=False))
        if existing:
            for question in existing:
                question.is_active = True
        else:
            db.add_all(Question(**row, is_active=True) for row in rows)
        db.commit()
        return len(rows)
