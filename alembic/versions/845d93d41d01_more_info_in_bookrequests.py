"""more info in bookrequests

Revision ID: 845d93d41d01
Revises: d6a02deef57b
Create Date: 2025-02-17 18:46:31.223438

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = "845d93d41d01"
down_revision: Union[str, None] = "d6a02deef57b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("prowlarrsource")
    op.execute("DELETE FROM bookrequest")
    with op.batch_alter_table("bookrequest", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("title", sqlmodel.sql.sqltypes.AutoString(), nullable=False)
        )
        batch_op.add_column(
            sa.Column("subtitle", sqlmodel.sql.sqltypes.AutoString(), nullable=True)
        )
        batch_op.add_column(sa.Column("authors", sa.JSON(), nullable=True))
        batch_op.add_column(sa.Column("narrators", sa.JSON(), nullable=True))
        batch_op.add_column(
            sa.Column("cover_image", sqlmodel.sql.sqltypes.AutoString(), nullable=True)
        )
        batch_op.add_column(sa.Column("release_date", sa.DateTime(), nullable=False))
        batch_op.add_column(
            sa.Column("runtime_length_min", sa.Integer(), nullable=False)
        )
        batch_op.alter_column(
            "user_username", existing_type=sa.VARCHAR(), nullable=True
        )
        batch_op.create_unique_constraint("unique_asin_user", ["asin", "user_username"])
        batch_op.create_foreign_key(
            "user_user_username",
            "user",
            ["user_username"],
            ["username"],
            ondelete="SET NULL",
        )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("bookrequest", schema=None) as batch_op:
        batch_op.create_foreign_key(
            "user_user_username",
            "user",
            ["user_username"],
            ["username"],
            ondelete="CASCADE",
        )
        batch_op.drop_constraint("unique_asin_user", type_="unique")
        batch_op.alter_column(
            "user_username", existing_type=sa.VARCHAR(), nullable=False
        )
        batch_op.drop_column("runtime_length_min")
        batch_op.drop_column("release_date")
        batch_op.drop_column("cover_image")
        batch_op.drop_column("narrators")
        batch_op.drop_column("authors")
        batch_op.drop_column("subtitle")
        batch_op.drop_column("title")

    op.create_table(
        "prowlarrsource",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("publish_date", sa.DATETIME(), nullable=False),
        sa.Column("guid", sa.VARCHAR(), nullable=False),
        sa.Column("indexer_id", sa.INTEGER(), nullable=False),
        sa.Column("title", sa.VARCHAR(), nullable=False),
        sa.Column("seeders", sa.INTEGER(), nullable=False),
        sa.Column("leechers", sa.INTEGER(), nullable=False),
        sa.Column("size", sa.INTEGER(), nullable=False),
        sa.ForeignKeyConstraint(["indexer_id"], ["indexer.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###
