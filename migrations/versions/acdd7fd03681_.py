"""empty message

Revision ID: acdd7fd03681
Revises: 
Create Date: 2017-08-01 11:10:23.574567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acdd7fd03681'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('gallery_items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('creator', sa.Unicode(length=127), server_default=u'', nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('gallery_items', schema=None) as batch_op:
        batch_op.drop_column('creator')

    # ### end Alembic commands ###
