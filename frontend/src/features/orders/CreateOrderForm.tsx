"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/Button";
import { Input } from "@/components/ui/Input";
import { useCreateOrder } from "@/hooks/useOrders";

export function CreateOrderForm() {
  const router = useRouter();
  const createOrder = useCreateOrder();
  const [warranty, setWarranty] = useState(false);
  const [form, setForm] = useState({
    customer_name: "",
    contact_info: "",
    equipment_model: "",
    serial_number: "",
    intake_reason: "",
    estimated_cost: "0",
  });

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    try {
      const order = await createOrder.mutateAsync({
        ...form,
        warranty,
        estimated_cost: warranty ? 0 : Number(form.estimated_cost) || 0,
      });
      router.push(`/orders/${order.id}`);
    } catch {
      // Error handling via toast/alert if needed
    }
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4 max-w-xl">
      <h1 className="text-2xl font-bold text-slate-800">Crear orden</h1>

      <Input
        label="Nombre del cliente"
        value={form.customer_name}
        onChange={(e) => setForm((f) => ({ ...f, customer_name: e.target.value }))}
        required
      />
      <Input
        label="Contacto"
        value={form.contact_info}
        onChange={(e) => setForm((f) => ({ ...f, contact_info: e.target.value }))}
        required
      />
      <Input
        label="Modelo del equipo"
        value={form.equipment_model}
        onChange={(e) => setForm((f) => ({ ...f, equipment_model: e.target.value }))}
        required
      /> 
      <Input
        label="Número de serie"
        value={form.serial_number}
        onChange={(e) => setForm((f) => ({ ...f, serial_number: e.target.value }))}
        required
      />asdasd
      <div>
        <label className="text-sm font-medium text-slate-700 block mb-1">
          Motivo de ingreso
        </label>
        <textarea
          className="border border-slate-300 rounded-lg px-3 py-2 w-full focus:ring-2 focus:ring-slate-500 focus:border-transparent outline-none"
          rows={3}
          value={form.intake_reason}
          onChange={(e) => setForm((f) => ({ ...f, intake_reason: e.target.value }))}
          required
        />
      </div>

      <div className="flex items-center gap-2">
        <input
          type="checkbox"
          id="warranty"
          checked={warranty}
          onChange={(e) => setWarranty(e.target.checked)}
          className="rounded border-slate-300"
        />
        <label htmlFor="warranty" className="text-sm font-medium text-slate-700">
          En garantía
        </label>
      </div>

      <Input
        label="Costo estimado"
        type="number"
        min={0}
        step={0.01}
        value={form.estimated_cost}
        onChange={(e) => setForm((f) => ({ ...f, estimated_cost: e.target.value }))}
        disabled={warranty}
      />

      <div className="flex gap-2">
        <Button type="submit" isLoading={createOrder.isPending}>
          Crear orden
        </Button>
        <Button type="button" variant="secondary" onClick={() => router.back()}>
          Cancelar
        </Button>
      </div>
    </form>
  );
}
