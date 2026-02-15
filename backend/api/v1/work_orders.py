from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from adapters.db.session import get_db
from adapters.db.repositories.work_order_repository import WorkOrderRepository
from api.deps import require_technician_or_admin, get_current_user
from domain.models.user import User
from domain.models.work_order import WorkOrderStatus
from schemas.work_order import WorkOrderCreate, WorkOrderUpdate, WorkOrderResponse
from use_cases.work_order import (
    create_work_order,
    get_work_order,
    update_work_order,
    list_work_orders,
)

router = APIRouter()


def _to_response(order) -> WorkOrderResponse:
    return WorkOrderResponse(
        id=order.id,
        customer_name=order.customer_name,
        contact_info=order.contact_info,
        equipment_model=order.equipment_model,
        serial_number=order.serial_number,
        intake_reason=order.intake_reason,
        status=order.status,
        warranty=order.warranty,
        estimated_cost=order.estimated_cost,
        diagnosis=order.diagnosis,
        created_at=order.created_at,
        updated_at=order.updated_at,
    )


@router.get("/orders", response_model=list[WorkOrderResponse])
def list_orders(
    status: Optional[WorkOrderStatus] = None,
    date_from: Optional[date] = None,
    date_to: Optional[date] = None,
    sort: str = "newest",
    db: Session = Depends(get_db),
    current_user: User = Depends(require_technician_or_admin),
):
    repo = WorkOrderRepository(db)
    orders = list_work_orders(
        repo,
        status=status,
        date_from=date_from,
        date_to=date_to,
        sort_newest=(sort == "newest"),
    )
    return [_to_response(o) for o in orders]


@router.post("/orders", response_model=WorkOrderResponse)
def create_order(
    data: WorkOrderCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_technician_or_admin),
):
    repo = WorkOrderRepository(db)
    order = create_work_order(repo, data)
    return _to_response(order)


@router.get("/orders/{order_id}", response_model=WorkOrderResponse)
def get_order(
    order_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_technician_or_admin),
):
    repo = WorkOrderRepository(db)
    order = get_work_order(repo, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return _to_response(order)


@router.patch("/orders/{order_id}", response_model=WorkOrderResponse)
def update_order(
    order_id: str,
    data: WorkOrderUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_technician_or_admin),
):
    repo = WorkOrderRepository(db)
    order = update_work_order(repo, order_id, data)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return _to_response(order)
