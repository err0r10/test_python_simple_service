"""create table user

Revision ID: fcd74e0fac4e
Revises: 
Create Date: 2023-03-20 15:49:12.041601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcd74e0fac4e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('user')
