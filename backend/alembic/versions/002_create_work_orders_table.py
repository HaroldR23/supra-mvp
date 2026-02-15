"""create work orders table

Revision ID: 002
Revises: 001
Create Date: 2025-02-14

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "002"
down_revision: Union[str, None] = "001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "work_orders",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("customer_name", sa.String(255), nullable=False),
        sa.Column("contact_info", sa.String(255), nullable=False),
        sa.Column("equipment_model", sa.String(255), nullable=False),
        sa.Column("serial_number", sa.String(255), nullable=False),
        sa.Column("intake_reason", sa.Text(), nullable=False),
        sa.Column(
            "status",
            sa.Enum("RECEIVED", "IN_REVIEW", "IN_REPAIR", "COMPLETED", name="workorderstatusenum"),
            nullable=False,
        ),
        sa.Column("warranty", sa.Boolean(), nullable=False, server_default=sa.text("false")),
        sa.Column("estimated_cost", sa.Numeric(10, 2), nullable=False, server_default=sa.text("0")),
        sa.Column("diagnosis", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("work_orders")
    op.execute("DROP TYPE IF EXISTS workorderstatusenum")
