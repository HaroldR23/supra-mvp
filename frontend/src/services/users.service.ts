import { api } from "./api";
import type { User } from "@/types/user";

export async function listUsers(): Promise<User[]> {
  const { data } = await api.get<User[]>("/users");
  return data;
}
