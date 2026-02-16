"use client";

interface TableProps {
  children?: React.ReactNode;
}

export function Table({ children }: TableProps) {
  return (
    <div className="overflow-x-auto rounded-lg border border-slate-200">
      <table className="min-w-full divide-y divide-slate-200">{children}</table>
    </div>
  );
}

export function TableHead({ children }: TableProps) {
  return <thead className="bg-slate-50">{children}</thead>;
}

export function TableBody({ children }: TableProps) {
  return <tbody className="divide-y divide-slate-200 bg-white">{children}</tbody>;
}

export function TableRow({ children }: TableProps) {
  return <tr className="hover:bg-slate-50">{children}</tr>;
}

export function TableHeader({ children }: TableProps) {
  return (
    <th className="px-4 py-3 text-left text-xs font-semibold text-slate-600 uppercase tracking-wider">
      {children ?? "\u00A0"}
    </th>
  );
}

export function TableCell({ children }: TableProps) {
  return <td className="px-4 py-3 text-sm text-slate-900">{children}</td>;
}
