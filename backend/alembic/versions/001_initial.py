"""initial schema

Revision ID: 001_initial
Revises:
Create Date: 2026-03-29

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy import Uuid

revision: str = "001_initial"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "projects",
        sa.Column("id", Uuid(as_uuid=True), nullable=False),
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("slug", sa.String(length=120), nullable=False),
        sa.Column("summary", sa.String(length=500), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("tech_stack", sa.JSON(), nullable=False),
        sa.Column("repo_url", sa.String(length=2048), nullable=False),
        sa.Column("demo_url", sa.String(length=2048), nullable=True),
        sa.Column("featured", sa.Boolean(), nullable=False),
        sa.Column("sort_order", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_projects_slug"), "projects", ["slug"], unique=True)

    op.create_table(
        "skill_categories",
        sa.Column("id", Uuid(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("sort_order", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )

    op.create_table(
        "skills",
        sa.Column("id", Uuid(as_uuid=True), nullable=False),
        sa.Column("category_id", Uuid(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("proficiency", sa.Integer(), nullable=False),
        sa.Column("years", sa.Integer(), nullable=True),
        sa.Column("highlights", sa.JSON(), nullable=False),
        sa.Column("sort_order", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["category_id"], ["skill_categories.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "contacts",
        sa.Column("id", Uuid(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("subject", sa.String(length=200), nullable=False),
        sa.Column("message", sa.Text(), nullable=False),
        sa.Column("company", sa.String(length=200), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_contacts_email"), "contacts", ["email"], unique=False)

    op.create_table(
        "analytics_visits",
        sa.Column("id", Uuid(as_uuid=True), nullable=False),
        sa.Column("path", sa.String(length=512), nullable=False),
        sa.Column("ip_hash", sa.String(length=64), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("(CURRENT_TIMESTAMP)"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("analytics_visits")
    op.drop_index(op.f("ix_contacts_email"), table_name="contacts")
    op.drop_table("contacts")
    op.drop_table("skills")
    op.drop_table("skill_categories")
    op.drop_index(op.f("ix_projects_slug"), table_name="projects")
    op.drop_table("projects")
