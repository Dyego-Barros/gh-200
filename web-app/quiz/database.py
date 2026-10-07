"""Preparação do SQLite compartilhada pelo servidor e pelos comandos CLI."""
from pathlib import Path
from alembic import command
from alembic.config import Config
from sqlalchemy.orm import Session
from .importer import QuestionnaireImporter


class DatabaseManager:
    def __init__(self, engine, root):
        self.engine = engine
        self.root = Path(root)

    def migrate(self):
        url = self.engine.url
        if url.database and url.database != ':memory:':
            Path(url.database).parent.mkdir(parents=True, exist_ok=True)
        config = Config(str(self.root / 'alembic.ini'))
        config.set_main_option('script_location', str(self.root / 'migrations'))
        config.set_main_option('sqlalchemy.url', url.render_as_string(hide_password=False).replace('%', '%%'))
        command.upgrade(config, 'head')

    def import_questions(self, source):
        with Session(self.engine) as db:
            return QuestionnaireImporter().import_file(db, source)

    def prepare(self, source):
        self.migrate()
        return self.import_questions(source)
