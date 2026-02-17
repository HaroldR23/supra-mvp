"use client";

import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import {
  listOrders,
  getOrder,
  createOrder,
  updateOrder,
  downloadOrderPdf,
  type ListOrdersParams,
} from "@/services/orders.service";
import type { WorkOrderCreate, WorkOrderUpdate } from "@/types/work-order";

export function useOrders(params?: ListOrdersParams) {
  return useQuery({
    queryKey: ["orders", params],
    queryFn: () => listOrders(params),
  });
}

export function useOrder(id: string | null) {
  return useQuery({
    queryKey: ["order", id],
    queryFn: () => getOrder(id!),
    enabled: !!id,
  });
}

export function useCreateOrder() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (data: WorkOrderCreate) => createOrder(data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["orders"] });
    },
  });
}

export function useUpdateOrder() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ id, update }: { id: string; update: WorkOrderUpdate }) =>
      updateOrder(id, update),
    onSuccess: (_, { id }) => {
      queryClient.invalidateQueries({ queryKey: ["orders"] });
      queryClient.invalidateQueries({ queryKey: ["order", id] });
    },
  });
}

export function useDownloadOrderPdf() {
  return useMutation({
    mutationFn: (id: string) => downloadOrderPdf(id),
  });
}
