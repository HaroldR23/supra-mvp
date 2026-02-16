"use client";

import Link from "next/link";
import {
  Table,
  TableHead,
  TableBody,
  TableRow,
  TableHeader,
  TableCell,
} from "@/components/ui/Table";
import type { WorkOrder } from "@/types/work-order";

const STATUS_LABELS: Record<string, string> = {
  RECEIVED: "Recibido",
  IN_REVIEW: "En revisión",
  IN_REPAIR: "En reparación",
  COMPLETED: "Completado",
};

export function OrderTable({ orders }: { orders: WorkOrder[] }) {
  if (orders.length === 0) {
    return (
      <p className="text-slate-500 py-8 text-center">No hay órdenes que mostrar.</p>
    );
  }

  return (
    <Table>
      <TableHead>
        <TableRow>
          <TableHeader>Cliente</TableHeader>
          <TableHeader>Equipo</TableHeader>
          <TableHeader>Estado</TableHeader>
          <TableHeader>Garantía</TableHeader>
          <TableHeader>Costo est.</TableHeader>
          <TableHeader>Fecha</TableHeader>
          <TableHeader></TableHeader>
        </TableRow>
      </TableHead>
      <TableBody>
        {orders.map((order) => (
          <TableRow key={order.id}>
            <TableCell>{order.customer_name}</TableCell>
            <TableCell>{order.equipment_model}</TableCell>
            <TableCell>{STATUS_LABELS[order.status] || order.status}</TableCell>
            <TableCell>{order.warranty ? "Sí" : "No"}</TableCell>
            <TableCell>
              {order.warranty
                ? "0"
                : typeof order.estimated_cost === "number"
                  ? order.estimated_cost
                  : Number(order.estimated_cost) || 0}
            </TableCell>
            <TableCell>
              {new Date(order.created_at).toLocaleDateString("es-ES")}
            </TableCell>
            <TableCell>
              <Link
                href={`/orders/${order.id}`}
                className="text-slate-600 hover:text-slate-900 underline text-sm"
              >
                Ver
              </Link>
            </TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}
