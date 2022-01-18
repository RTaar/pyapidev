"""create post table

Revision ID: edfa1ef45f82
Revises: 
Create Date: 2022-01-18 11:21:11.195700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edfa1ef45f82'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id', sa.Integer(), nullable=False, primary_key=True)
    , sa.Column('title', sa.String(), nullable=False))


def downgrade():
    op.drop_table('posts')
