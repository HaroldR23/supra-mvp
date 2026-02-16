"use client";

import { useState } from "react";
import Link from "next/link";
import { OrderTable } from "@/features/orders/OrderTable";
import { OrderFilters } from "@/features/orders/OrderFilters";
import { useOrders } from "@/hooks/useOrders";
import { useAuth } from "@/hooks/useAuth";
import type { WorkOrderStatus } from "@/types/work-order";

export function DashboardView() {
  const { user } = useAuth();
  const [status, setStatus] = useState<WorkOrderStatus | "">("");
  const [dateFrom, setDateFrom] = useState("");
  const [dateTo, setDateTo] = useState("");

  const params = {
    status: status || undefined,
    date_from: dateFrom || undefined,
    date_to: dateTo || undefined,
    sort: "newest",
  };

  const { data: orders = [], isLoading, error } = useOrders(params);

  return (
    <div className="space-y-4">
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
        <h1 className="text-2xl font-bold text-slate-800">Órdenes de trabajo</h1>
        {user?.role === "ADMIN" && (
          <Link
            href="/orders"
            className="inline-flex items-center justify-center px-4 py-2 bg-slate-800 text-white rounded-lg hover:bg-slate-700 font-medium"
          >
            Nueva orden
          </Link>
        )}
      </div>

      <OrderFilters
        status={status}
        onStatusChange={setStatus}
        dateFrom={dateFrom}
        onDateFromChange={setDateFrom}
        dateTo={dateTo}
        onDateToChange={setDateTo}
      />

      {isLoading && <p className="text-slate-500">Cargando...</p>}
      {error && (
        <p className="text-red-600">Error al cargar las órdenes. Intente de nuevo.</p>
      )}
      {!isLoading && !error && <OrderTable orders={orders} />}
    </div>
  );
}
