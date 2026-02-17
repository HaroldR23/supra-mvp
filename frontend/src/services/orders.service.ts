import { api } from "./api";
import type { WorkOrder, WorkOrderCreate, WorkOrderUpdate } from "@/types/work-order";

export interface ListOrdersParams {
  status?: string;
  date_from?: string;
  date_to?: string;
  sort?: string;
}

export async function listOrders(params?: ListOrdersParams): Promise<WorkOrder[]> {
  const { data } = await api.get<WorkOrder[]>("/orders", { params });
  return data;
}

export async function getOrder(id: string): Promise<WorkOrder> {
  const { data } = await api.get<WorkOrder>(`/orders/${id}`);
  return data;
}

export async function createOrder(order: WorkOrderCreate): Promise<WorkOrder> {
  const payload = {
    ...order,
    estimated_cost: Number(order.estimated_cost) || 0,
  };
  const { data } = await api.post<WorkOrder>("/orders", payload);
  return data;
}

export async function updateOrder(id: string, update: WorkOrderUpdate): Promise<WorkOrder> {
  const payload = { ...update };
  if (update.estimated_cost !== undefined) {
    payload.estimated_cost = Number(update.estimated_cost) || 0;
  }
  const { data } = await api.patch<WorkOrder>(`/orders/${id}`, payload);
  return data;
}

export async function downloadOrderPdf(id: string): Promise<Blob> {
  const response = await api.get<Blob>(`/orders/${id}/pdf`, {
    responseType: "blob",
  });
  return response.data;
}
