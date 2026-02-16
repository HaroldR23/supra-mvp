"use client";

import { Select } from "@/components/ui/Select";
import { Input } from "@/components/ui/Input";
import type { WorkOrderStatus } from "@/types/work-order";

const STATUS_OPTIONS: { value: WorkOrderStatus | ""; label: string }[] = [
  { value: "", label: "Todos" },
  { value: "RECEIVED", label: "Recibido" },
  { value: "IN_REVIEW", label: "En revisión" },
  { value: "IN_REPAIR", label: "En reparación" },
  { value: "COMPLETED", label: "Completado" },
];

interface OrderFiltersProps {
  status: WorkOrderStatus | "";
  onStatusChange: (v: WorkOrderStatus | "") => void;
  dateFrom: string;
  onDateFromChange: (v: string) => void;
  dateTo: string;
  onDateToChange: (v: string) => void;
}

export function OrderFilters({
  status,
  onStatusChange,
  dateFrom,
  onDateFromChange,
  dateTo,
  onDateToChange,
}: OrderFiltersProps) {
  return (
    <div className="flex flex-wrap gap-4 p-4 bg-slate-50 rounded-lg border border-slate-200">
      <div className="min-w-[140px]">
        <Select
          label="Filtrar por estado"
          options={STATUS_OPTIONS}
          value={status}
          onChange={(e) => onStatusChange((e.target.value || "") as WorkOrderStatus | "")}
        />
      </div>
      <div className="min-w-[140px]">
        <Input
          label="Fecha desde"
          type="date"
          value={dateFrom}
          onChange={(e) => onDateFromChange(e.target.value)}
        />
      </div>
      <div className="min-w-[140px]">
        <Input
          label="Fecha hasta"
          type="date"
          value={dateTo}
          onChange={(e) => onDateToChange(e.target.value)}
        />
      </div>
    </div>
  );
}
