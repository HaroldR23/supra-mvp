from enum import Enum
from typing import Optional
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


class WorkOrderStatus(str, Enum):
    RECEIVED = "RECEIVED"
    IN_REVIEW = "IN_REVIEW"
    IN_REPAIR = "IN_REPAIR"
    COMPLETED = "COMPLETED"


@dataclass
class WorkOrder:
    id: str
    customer_name: str
    contact_info: str
    equipment_model: str
    serial_number: str
    intake_reason: str
    status: WorkOrderStatus
    warranty: bool
    estimated_cost: Decimal
    diagnosis: Optional[str]
    created_at: datetime
    updated_at: datetime

    def validate_warranty_cost(self) -> None:
        if self.warranty and self.estimated_cost != Decimal("0"):
            raise ValueError("If warranty is True, estimated_cost must be 0")
