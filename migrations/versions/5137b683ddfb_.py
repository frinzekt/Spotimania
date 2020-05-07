"""empty message

Revision ID: 5137b683ddfb
Revises: 4655bcb421e2
Create Date: 2020-05-07 17:56:20.916651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5137b683ddfb'
down_revision = '4655bcb421e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('playlist_song',
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('playlistId', sa.Integer(), nullable=True),
    sa.Column('songId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['playlistId'], ['playlist.id'], ),
    sa.ForeignKeyConstraint(['songId'], ['song.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('individualResults',
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('answerArtist', sa.String(length=100), nullable=True),
    sa.Column('answerSong', sa.String(length=100), nullable=True),
    sa.Column('isAnswerArtistCorrect', sa.Boolean(), nullable=True),
    sa.Column('isAnswerSongCorrect', sa.Boolean(), nullable=True),
    sa.Column('resultId', sa.Integer(), nullable=True),
    sa.Column('songId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['resultId'], ['results.id'], ),
    sa.ForeignKeyConstraint(['songId'], ['song.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('playlist__song')
    op.drop_table('individual_results')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('individual_results',
    sa.Column('date_created', sa.DATETIME(), nullable=True),
    sa.Column('date_modified', sa.DATETIME(), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('answerArtist', sa.VARCHAR(length=100), nullable=True),
    sa.Column('answerSong', sa.VARCHAR(length=100), nullable=True),
    sa.Column('isAnswerArtistCorrect', sa.BOOLEAN(), nullable=True),
    sa.Column('isAnswerSongCorrect', sa.BOOLEAN(), nullable=True),
    sa.Column('resultId', sa.INTEGER(), nullable=True),
    sa.Column('songId', sa.INTEGER(), nullable=True),
    sa.CheckConstraint('"isAnswerArtistCorrect" IN (0, 1)'),
    sa.CheckConstraint('"isAnswerSongCorrect" IN (0, 1)'),
    sa.ForeignKeyConstraint(['resultId'], ['results.id'], ),
    sa.ForeignKeyConstraint(['songId'], ['song.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('playlist__song',
    sa.Column('date_created', sa.DATETIME(), nullable=True),
    sa.Column('date_modified', sa.DATETIME(), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('playlistId', sa.INTEGER(), nullable=True),
    sa.Column('songId', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['playlistId'], ['playlist.id'], ),
    sa.ForeignKeyConstraint(['songId'], ['song.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('individualResults')
    op.drop_table('playlist_song')
    # ### end Alembic commands ###
