from abc import ABC, abstractmethod
from typing import Optional
from datetime import date
from ..models.work_order import WorkOrder, WorkOrderStatus


class WorkOrderRepositoryPort(ABC):
    @abstractmethod
    def create(self, order: WorkOrder) -> WorkOrder:
        pass

    @abstractmethod
    def get_by_id(self, order_id: str) -> Optional[WorkOrder]:
        pass

    @abstractmethod
    def list_orders(
        self,
        status: Optional[WorkOrderStatus] = None,
        date_from: Optional[date] = None,
        date_to: Optional[date] = None,
        sort_newest: bool = True,
    ) -> list[WorkOrder]:
        pass

    @abstractmethod
    def update(self, order: WorkOrder) -> WorkOrder:
        pass
