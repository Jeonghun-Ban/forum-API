"""modify relationship board with article

Revision ID: 785756bde3c0
Revises: 664b19fa09b0
Create Date: 2020-03-20 00:45:01.908107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '785756bde3c0'
down_revision = '664b19fa09b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('board', sa.String(), nullable=True))
    op.create_foreign_key(None, 'article', 'board', ['board'], ['name'])
    op.drop_constraint('board_articles_fkey', 'board', type_='foreignkey')
    op.drop_column('board', 'articles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('board', sa.Column('articles', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('board_articles_fkey', 'board', 'article', ['articles'], ['id'])
    op.drop_constraint(None, 'article', type_='foreignkey')
    op.drop_column('article', 'board')
    # ### end Alembic commands ###
