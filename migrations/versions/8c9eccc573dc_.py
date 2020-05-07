"""empty message

Revision ID: 8c9eccc573dc
Revises: 544377a84fbf
Create Date: 2020-05-02 19:06:36.590783

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c9eccc573dc'
down_revision = '544377a84fbf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('playlist',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('songID', sa.String(length=100), nullable=True),
    sa.Column('prevURL', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('playlist')
    # ### end Alembic commands ###
