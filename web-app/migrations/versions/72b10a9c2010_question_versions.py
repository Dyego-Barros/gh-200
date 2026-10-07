"""Preserva versões do questionário para não alterar rodadas anteriores."""
from alembic import op
import sqlalchemy as sa

revision = '72b10a9c2010'
down_revision = '3d8f1afb02f2'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('questions', naming_convention={'uq': 'uq_%(table_name)s_%(column_0_name)s'}, table_args=(
        sa.CheckConstraint("level IN ('Básico','Intermediário','Avançado')", name='ck_questions_level'),
        sa.CheckConstraint("correct IN ('A','B','C','D')", name='ck_questions_correct'),
    )) as batch:
        batch.add_column(sa.Column('is_active', sa.Boolean(), nullable=False, server_default=sa.true()))
        batch.drop_constraint('uq_questions_number', type_='unique')
        batch.create_unique_constraint('uq_questions_source_number', ['source_hash', 'number'])


def downgrade():
    connection = op.get_bind()
    if connection.execute(sa.text('SELECT number FROM questions GROUP BY number HAVING COUNT(*) > 1')).first():
        raise RuntimeError('Downgrade recusado: há versões de questões preservadas no histórico.')
    with op.batch_alter_table('questions') as batch:
        batch.drop_constraint('uq_questions_source_number', type_='unique')
        batch.create_unique_constraint('uq_questions_number', ['number'])
        batch.drop_column('is_active')
