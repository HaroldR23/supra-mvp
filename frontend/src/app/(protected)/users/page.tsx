"use client";

import { useQuery } from "@tanstack/react-query";
import { listUsers } from "@/services/users.service";
import { Table, TableHead, TableBody, TableRow, TableHeader, TableCell } from "@/components/ui/Table";

export default function UsersPage() {
  const { data: users = [], isLoading, error } = useQuery({
    queryKey: ["users"],
    queryFn: listUsers,
  });

  if (isLoading) return <p className="text-slate-500">Cargando...</p>;
  if (error) return <p className="text-red-600">Error al cargar usuarios.</p>;

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold text-slate-800">Usuarios</h1>
      <Table>
        <TableHead>
          <TableRow>
            <TableHeader>Email</TableHeader>
            <TableHeader>Rol</TableHeader>
          </TableRow>
        </TableHead>
        <TableBody>
          {users.map((u) => (
            <TableRow key={u.id}>
              <TableCell>{u.email}</TableCell>
              <TableCell>{u.role === "ADMIN" ? "Admin" : "Técnico"}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}
