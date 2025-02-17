"""add updated at to bookrequest

Revision ID: e4f418be2275
Revises: 7735bdd2c970
Create Date: 2025-02-17 19:52:21.287598

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'e4f418be2275'
down_revision: Union[str, None] = '7735bdd2c970'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bookrequest', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bookrequest', schema=None) as batch_op:
        batch_op.drop_column('updated_at')

    # ### end Alembic commands ###
