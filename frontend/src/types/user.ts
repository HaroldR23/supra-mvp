export type UserRole = "ADMIN" | "TECHNICIAN";

export interface User {
  id: string;
  email: string;
  role: UserRole;
  created_at: string;
}
