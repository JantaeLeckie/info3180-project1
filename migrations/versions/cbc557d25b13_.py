"""empty message

Revision ID: cbc557d25b13
Revises: 8b89963b9005
Create Date: 2021-03-22 20:03:53.034278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbc557d25b13'
down_revision = '8b89963b9005'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('property', sa.Column('property_bathroom', sa.String(length=255), nullable=True))
    op.drop_column('property', 'property_bathrooms')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('property', sa.Column('property_bathrooms', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('property', 'property_bathroom')
    # ### end Alembic commands ###
