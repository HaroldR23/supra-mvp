"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/hooks/useAuth";
import { Header } from "@/components/layout/Header";

export default function ProtectedLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const { isAuthenticated } = useAuth();
  const router = useRouter();

  const [mounted, setMounted] = useState(false);
  const [hasToken, setHasToken] = useState(false);

  useEffect(() => {
    const handleMounted = () => {

      setMounted(true);
      
      const token = localStorage.getItem("token");
      setHasToken(!!token);
      
      if (!token && !isAuthenticated) {
        router.replace("/login");
      }
    };
    handleMounted();
  
  }, [isAuthenticated, router]);

  if (!mounted) {
    return null;
  }

  if (!isAuthenticated && !hasToken) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <p className="text-slate-500">Cargando...</p>
      </div>
    );
  }

  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-1 p-6">{children}</main>
    </div>
  );
}
