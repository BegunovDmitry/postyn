"""Database creation

Revision ID: cc4d21e8fcf8
Revises: 
Create Date: 2024-10-15 11:49:14.531775

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc4d21e8fcf8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.String(length=6000), nullable=False),
    sa.Column('create_date_time', sa.DateTime(), nullable=True),
    sa.Column('storage_time__hours', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###
