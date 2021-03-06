"""email not unique, add state

Revision ID: bd8fa260b710
Revises: 4047e2141d5d
Create Date: 2021-05-14 00:11:17.419933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd8fa260b710'
down_revision = '4047e2141d5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('booking', sa.Column('state', sa.String(length=20), nullable=True))
    op.drop_constraint('booking_email_key', 'booking', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('booking_email_key', 'booking', ['email'])
    op.drop_column('booking', 'state')
    # ### end Alembic commands ###
