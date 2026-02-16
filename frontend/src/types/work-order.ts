export type WorkOrderStatus =
  | "RECEIVED"
  | "IN_REVIEW"
  | "IN_REPAIR"
  | "COMPLETED";

export interface WorkOrder {
  id: string;
  customer_name: string;
  contact_info: string;
  equipment_model: string;
  serial_number: string;
  intake_reason: string;
  status: WorkOrderStatus;
  warranty: boolean;
  estimated_cost: string | number;
  diagnosis: string | null;
  created_at: string;
  updated_at: string;
}

export interface WorkOrderCreate {
  customer_name: string;
  contact_info: string;
  equipment_model: string;
  serial_number: string;
  intake_reason: string;
  warranty: boolean;
  estimated_cost: string | number;
}

export interface WorkOrderUpdate {
  status?: WorkOrderStatus;
  warranty?: boolean;
  estimated_cost?: string | number;
  diagnosis?: string;
}
