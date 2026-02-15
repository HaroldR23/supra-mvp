from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, model_validator

from domain.models.work_order import WorkOrderStatus


class WorkOrderBase(BaseModel):
    customer_name: str
    contact_info: str
    equipment_model: str
    serial_number: str
    intake_reason: str
    warranty: bool = False
    estimated_cost: Decimal = Decimal("0")


class WorkOrderCreate(WorkOrderBase):
    @model_validator(mode="after")
    def validate_warranty_cost(self):
        if self.warranty and self.estimated_cost != Decimal("0"):
            raise ValueError("If warranty is True, estimated_cost must be 0")
        return self


class WorkOrderUpdate(BaseModel):
    status: Optional[WorkOrderStatus] = None
    warranty: Optional[bool] = None
    estimated_cost: Optional[Decimal] = None
    diagnosis: Optional[str] = None

    @model_validator(mode="after")
    def validate_warranty_cost(self):
        if self.warranty is True and self.estimated_cost is not None and self.estimated_cost != Decimal("0"):
            raise ValueError("If warranty is True, estimated_cost must be 0")
        return self


class WorkOrderResponse(BaseModel):
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

    class Config:
        from_attributes = True
