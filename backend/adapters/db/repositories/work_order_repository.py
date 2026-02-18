from typing import Optional
from datetime import datetime, date
from decimal import Decimal
from sqlalchemy.orm import Session
from sqlalchemy import and_

from ...db.models.work_order import WorkOrderModel, WorkOrderStatusEnum
from domain.ports.work_order_repository import WorkOrderRepositoryPort
from domain.models.work_order import WorkOrder, WorkOrderStatus


def _to_domain(model: WorkOrderModel) -> WorkOrder:
    return WorkOrder(
        id=str(model.id),
        customer_name=str(model.customer_name),
        contact_info=str(model.contact_info),
        equipment_model=str(model.equipment_model),
        serial_number=str(model.serial_number),
        intake_reason=str(model.intake_reason),
        status=WorkOrderStatus(model.status.value),
        warranty=bool(model.warranty),
        estimated_cost=Decimal(str(model.estimated_cost)),
        diagnosis=model.diagnosis,
        created_at=datetime.fromisoformat(str(model.created_at)),
        updated_at=datetime.fromisoformat(str(model.updated_at)),
    )


def _to_model(order: WorkOrder) -> WorkOrderModel:
    return WorkOrderModel(
        id=order.id,
        customer_name=order.customer_name,
        contact_info=order.contact_info,
        equipment_model=order.equipment_model,
        serial_number=order.serial_number,
        intake_reason=order.intake_reason,
        status=WorkOrderStatusEnum(order.status.value),
        warranty=order.warranty,
        estimated_cost=order.estimated_cost,
        diagnosis=order.diagnosis,
    )


class WorkOrderRepository(WorkOrderRepositoryPort):
    def __init__(self, db: Session):
        self._db = db

    def create(self, order: WorkOrder) -> WorkOrder:
        model = WorkOrderModel(
            customer_name=order.customer_name,
            contact_info=order.contact_info,
            equipment_model=order.equipment_model,
            serial_number=order.serial_number,
            intake_reason=order.intake_reason,
            status=WorkOrderStatusEnum(order.status.value),
            warranty=order.warranty,
            estimated_cost=order.estimated_cost,
            diagnosis=order.diagnosis,
        )
        self._db.add(model)
        self._db.commit()
        self._db.refresh(model)
        return _to_domain(model)

    def get_by_id(self, order_id: str) -> Optional[WorkOrder]:
        model = self._db.query(WorkOrderModel).filter(WorkOrderModel.id == order_id).first()
        return _to_domain(model) if model else None

    def list_orders(
        self,
        status: Optional[WorkOrderStatus] = None,
        date_from: Optional[date] = None,
        date_to: Optional[date] = None,
        sort_newest: bool = True,
    ) -> list[WorkOrder]:
        query = self._db.query(WorkOrderModel)
        if status:
            query = query.filter(WorkOrderModel.status == WorkOrderStatusEnum(status.value))
        if date_from:
            query = query.filter(WorkOrderModel.created_at >= date_from)
        if date_to:
            from datetime import datetime, time

            end_of_day = datetime.combine(date_to, time(23, 59, 59, 999999))
            query = query.filter(WorkOrderModel.created_at <= end_of_day)
        if sort_newest:
            query = query.order_by(WorkOrderModel.created_at.desc())
        models = query.all()
        return [_to_domain(m) for m in models]

    def update(self, order: WorkOrder) -> WorkOrder:
        model = self._db.query(WorkOrderModel).filter(WorkOrderModel.id == order.id).first()
        if not model:
            raise ValueError(f"Work order {order.id} not found")
        model.customer_name = order.customer_name
        model.contact_info = order.contact_info
        model.equipment_model = order.equipment_model
        model.serial_number = order.serial_number
        model.intake_reason = order.intake_reason
        model.status = WorkOrderStatusEnum(order.status.value)
        model.warranty = order.warranty
        model.estimated_cost = order.estimated_cost
        model.diagnosis = order.diagnosis
        self._db.commit()
        self._db.refresh(model)
        return _to_domain(model)
