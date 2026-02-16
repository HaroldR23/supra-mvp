"use client";

import Link from "next/link";
import { useAuth } from "@/hooks/useAuth";
import { Button } from "@/components/ui/Button";

export function Header() {
  const { user, logout } = useAuth();

  return (
    <header className="bg-slate-800 text-white px-4 py-3 flex items-center justify-between">
      <nav className="flex items-center gap-6">
        <Link href="/" className="font-semibold hover:underline">
          Taller
        </Link>
        {user?.role === "ADMIN" && (
          <Link href="/orders" className="hover:underline">
            Nueva orden
          </Link>
        )}
        {user?.role === "ADMIN" && (
          <Link href="/users" className="hover:underline">
            Usuarios
          </Link>
        )}
      </nav>
      <div className="flex items-center gap-4">
        <span className="text-sm text-slate-300">{user?.email}</span>
        <span className="text-xs bg-slate-600 px-2 py-0.5 rounded">
          {user?.role === "ADMIN" ? "Admin" : "Técnico"}
        </span>
        <Button variant="secondary" onClick={logout} className="!bg-slate-600 !text-white hover:!bg-slate-500">
          Salir
        </Button>
      </div>
    </header>
  );
}
