"""add content column to post table

Revision ID: 0ce101b9e2fd
Revises: edfa1ef45f82
Create Date: 2022-01-18 12:18:55.039858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ce101b9e2fd'
down_revision = 'edfa1ef45f82'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
