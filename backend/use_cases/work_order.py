from decimal import Decimal
from typing import Optional
from datetime import date, datetime

from domain.ports.work_order_repository import WorkOrderRepositoryPort
from domain.models.work_order import WorkOrder, WorkOrderStatus
from schemas.work_order import WorkOrderCreate, WorkOrderUpdate


def create_work_order(
    repo: WorkOrderRepositoryPort, data: WorkOrderCreate
) -> WorkOrder:
    if data.warranty:
        cost = Decimal("0")
    else:
        cost = data.estimated_cost
    now = datetime.utcnow()
    order = WorkOrder(
        id="",  # will be set by DB
        customer_name=data.customer_name,
        contact_info=data.contact_info,
        equipment_model=data.equipment_model,
        serial_number=data.serial_number,
        intake_reason=data.intake_reason,
        status=WorkOrderStatus.RECEIVED,
        warranty=data.warranty,
        estimated_cost=cost,
        diagnosis=None,
        created_at=now,
        updated_at=now,
    )
    return repo.create(order)


def get_work_order(repo: WorkOrderRepositoryPort, order_id: str) -> WorkOrder | None:
    return repo.get_by_id(order_id)


def update_work_order(
    repo: WorkOrderRepositoryPort, order_id: str, data: WorkOrderUpdate
) -> WorkOrder | None:
    existing = repo.get_by_id(order_id)
    if not existing:
        return None
    if data.status is not None:
        existing.status = data.status
    if data.warranty is not None:
        existing.warranty = data.warranty
        if data.warranty:
            existing.estimated_cost = Decimal("0")
    if data.estimated_cost is not None and not existing.warranty:
        existing.estimated_cost = data.estimated_cost
    if data.diagnosis is not None:
        existing.diagnosis = data.diagnosis
    return repo.update(existing)


def list_work_orders(
    repo: WorkOrderRepositoryPort,
    status: Optional[WorkOrderStatus] = None,
    date_from: Optional[date] = None,
    date_to: Optional[date] = None,
    sort_newest: bool = True,
) -> list[WorkOrder]:
    return repo.list_orders(
        status=status,
        date_from=date_from,
        date_to=date_to,
        sort_newest=sort_newest,
    )
