"""test migration

Revision ID: acd93d4ecb2f
Revises: 
Create Date: 2022-06-06 10:34:32.128954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acd93d4ecb2f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('new_field2', sa.String(), nullable=True))
    op.add_column('todos', sa.Column('new_field', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'new_field')
    op.drop_column('items', 'new_field2')
    # ### end Alembic commands ###