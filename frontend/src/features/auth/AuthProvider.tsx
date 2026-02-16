"use client";

import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { AuthProvider as AuthContextProvider } from "@/hooks/useAuth";

const queryClient = new QueryClient();

export function AuthProvider({ children }: { children: React.ReactNode }) {
  return (
    <QueryClientProvider client={queryClient}>
      <AuthContextProvider>{children}</AuthContextProvider>
    </QueryClientProvider>
  );
}
