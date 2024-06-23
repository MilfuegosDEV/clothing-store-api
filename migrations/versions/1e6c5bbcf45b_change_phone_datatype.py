"""change-phone-datatype

Revision ID: 1e6c5bbcf45b
Revises: 
Create Date: 2024-06-23 17:29:28.963360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e6c5bbcf45b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('SUPPLIER', schema=None) as batch_op:
        batch_op.alter_column('phone',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=8),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('SUPPLIER', schema=None) as batch_op:
        batch_op.alter_column('phone',
               existing_type=sa.String(length=8),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###