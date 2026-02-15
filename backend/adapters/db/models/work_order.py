import uuid
import enum
from sqlalchemy import Column, String, Boolean, DateTime, Text, Numeric, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from adapters.db.models.base import Base


class WorkOrderStatusEnum(str, enum.Enum):
    RECEIVED = "RECEIVED"
    IN_REVIEW = "IN_REVIEW"
    IN_REPAIR = "IN_REPAIR"
    COMPLETED = "COMPLETED"


class WorkOrderModel(Base):
    __tablename__ = "work_orders"

    id = Column(UUID(as_uuid=False), primary_key=True, default=lambda: str(uuid.uuid4()))
    customer_name = Column(String(255), nullable=False)
    contact_info = Column(String(255), nullable=False)
    equipment_model = Column(String(255), nullable=False)
    serial_number = Column(String(255), nullable=False)
    intake_reason = Column(Text, nullable=False)
    status = Column(
        Enum(WorkOrderStatusEnum), nullable=False, default=WorkOrderStatusEnum.RECEIVED
    )
    warranty = Column(Boolean, nullable=False, default=False)
    estimated_cost = Column(Numeric(10, 2), nullable=False, default=0)
    diagnosis = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
