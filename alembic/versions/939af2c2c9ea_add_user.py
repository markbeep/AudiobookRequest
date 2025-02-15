"""add user

Revision ID: 939af2c2c9ea
Revises: 
Create Date: 2025-02-15 17:27:55.137981

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '939af2c2c9ea'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('username', sa.LargeBinary(), nullable=False),
    sa.Column('password', sa.LargeBinary(), nullable=False),
    sa.PrimaryKeyConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
