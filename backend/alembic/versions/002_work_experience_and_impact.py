"""work experience table and project impact highlights

Revision ID: 002_work_experience
Revises: 001_initial
Create Date: 2026-03-29

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy import Uuid

revision: str = "002_work_experience"
down_revision: Union[str, None] = "001_initial"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "projects",
        sa.Column("impact_highlights", sa.JSON(), nullable=True),
    )
    op.create_table(
        "work_experience",
        sa.Column("id", Uuid(as_uuid=True), nullable=False),
        sa.Column("role", sa.String(length=200), nullable=False),
        sa.Column("company", sa.String(length=200), nullable=False),
        sa.Column("period", sa.String(length=120), nullable=False),
        sa.Column("summary", sa.Text(), nullable=False),
        sa.Column("key_points", sa.JSON(), nullable=False),
        sa.Column("sort_order", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("work_experience")
    op.drop_column("projects", "impact_highlights")
