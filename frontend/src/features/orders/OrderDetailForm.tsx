"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/Button";
import { Input } from "@/components/ui/Input";
import { Select } from "@/components/ui/Select";
import { useOrder, useUpdateOrder } from "@/hooks/useOrders";
import type { WorkOrderStatus } from "@/types/work-order";

const STATUS_OPTIONS: { value: WorkOrderStatus; label: string }[] = [
  { value: "RECEIVED", label: "Recibido" },
  { value: "IN_REVIEW", label: "En revisión" },
  { value: "IN_REPAIR", label: "En reparación" },
  { value: "COMPLETED", label: "Completado" },
];

interface OrderDetailFormProps {
  orderId: string;
}

export function OrderDetailForm({ orderId }: OrderDetailFormProps) {
  const router = useRouter();
  const { data: order, isLoading, error } = useOrder(orderId);
  const updateOrder = useUpdateOrder();
  const [status, setStatus] = useState<WorkOrderStatus>("RECEIVED");
  const [diagnosis, setDiagnosis] = useState("");
  const [estimatedCost, setEstimatedCost] = useState("0");
  const [warranty, setWarranty] = useState(false);

  useEffect(() => {
    if (order) {
      setStatus(order.status);
      setDiagnosis(order.diagnosis || "");
      setEstimatedCost(
        typeof order.estimated_cost === "number"
          ? String(order.estimated_cost)
          : String(order.estimated_cost || "0")
      );
      setWarranty(order.warranty);
    }
  }, [order]);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    try {
      await updateOrder.mutateAsync({
        id: orderId,
        update: {
          status,
          diagnosis: diagnosis || undefined,
          estimated_cost: warranty ? 0 : Number(estimatedCost) || 0,
          warranty,
        },
      });
    } catch {
      // Error handling
    }
  }

  if (isLoading) return <p className="text-slate-500">Cargando...</p>;
  if (error || !order)
    return <p className="text-red-600">No se pudo cargar la orden.</p>;

  return (
    <div className="space-y-6 max-w-xl">
      <h1 className="text-2xl font-bold text-slate-800">
        Orden #{order.id.slice(0, 8)}
      </h1>

      <div className="grid gap-4 text-sm">
        <p>
          <span className="font-medium text-slate-600">Cliente:</span> {order.customer_name}
        </p>
        <p>
          <span className="font-medium text-slate-600">Contacto:</span> {order.contact_info}
        </p>
        <p>
          <span className="font-medium text-slate-600">Equipo:</span> {order.equipment_model}
        </p>
        <p>
          <span className="font-medium text-slate-600">Nº Serie:</span> {order.serial_number}
        </p>
        <p>
          <span className="font-medium text-slate-600">Motivo de ingreso:</span>{" "}
          {order.intake_reason}
        </p>
      </div>

      <form onSubmit={handleSubmit} className="space-y-4 border-t border-slate-200 pt-6">
        <h2 className="font-semibold text-slate-800">Actualizar orden</h2>

        <Select
          label="Estado"
          options={STATUS_OPTIONS}
          value={status}
          onChange={(e) => setStatus(e.target.value as WorkOrderStatus)}
        />

        <div>
          <label className="text-sm font-medium text-slate-700 block mb-1">
            Diagnóstico técnico
          </label>
          <textarea
            className="border border-slate-300 rounded-lg px-3 py-2 w-full focus:ring-2 focus:ring-slate-500 focus:border-transparent outline-none"
            rows={4}
            value={diagnosis}
            onChange={(e) => setDiagnosis(e.target.value)}
          />
        </div>

        <div className="flex items-center gap-2">
          <input
            type="checkbox"
            id="warranty-update"
            checked={warranty}
            onChange={(e) => setWarranty(e.target.checked)}
            className="rounded border-slate-300"
          />
          <label
            htmlFor="warranty-update"
            className="text-sm font-medium text-slate-700"
          >
            En garantía
          </label>
        </div>

        <Input
          label="Costo estimado"
          type="number"
          min={0}
          step={0.01}
          value={estimatedCost}
          onChange={(e) => setEstimatedCost(e.target.value)}
          disabled={warranty}
        />

        <div className="flex gap-2">
          <Button type="submit" isLoading={updateOrder.isPending}>
            Guardar cambios
          </Button>
          <Button type="button" variant="secondary" onClick={() => router.push("/")}>
            Volver
          </Button>
        </div>
      </form>
    </div>
  );
}
