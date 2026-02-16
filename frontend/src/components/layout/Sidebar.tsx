"use client";

import Link from "next/link";
import { useAuth } from "@/hooks/useAuth";

export function Sidebar() {
  const { user } = useAuth();

  return (
    <aside className="w-48 bg-slate-100 border-r border-slate-200 p-4">
      <nav className="flex flex-col gap-2">
        <Link href="/" className="px-3 py-2 rounded hover:bg-slate-200 font-medium">
          Órdenes
        </Link>
        {user?.role === "ADMIN" && (
          <Link href="/orders" className="px-3 py-2 rounded hover:bg-slate-200">
            Nueva orden
          </Link>
        )}
      </nav>
    </aside>
  );
}