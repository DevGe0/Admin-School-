"""empty message

Revision ID: 40e618ddeca7
Revises: ef7987609419
Create Date: 2022-11-30 12:04:31.188393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40e618ddeca7'
down_revision = 'ef7987609419'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('docente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('apellido', sa.String(length=250), nullable=True),
    sa.Column('email', sa.String(length=250), nullable=True),
    sa.Column('edad', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('docente')
    # ### end Alembic commands ###