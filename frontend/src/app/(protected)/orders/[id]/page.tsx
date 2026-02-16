"use client";

import { useParams } from "next/navigation";
import { OrderDetailForm } from "@/features/orders/OrderDetailForm";

export default function OrderDetailPage() {
  const params = useParams();
  const id = params.id as string;

  return <OrderDetailForm orderId={id} />;
}
