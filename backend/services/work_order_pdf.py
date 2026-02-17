from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from domain.models.work_order import WorkOrder


def generate_work_order_pdf(order: WorkOrder) -> bytes:
    """
    Generate a simple PDF summary for a work order.
    """
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)

    width, height = A4
    margin_x = 50
    y = height - 80

    pdf.setTitle(f"Orden_{order.id}")

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(margin_x, y, "Orden de trabajo")
    y -= 30

    pdf.setFont("Helvetica", 10)
    pdf.drawString(margin_x, y, f"ID: {order.id}")
    y -= 16
    pdf.drawString(margin_x, y, f"Fecha de creación: {order.created_at.strftime('%Y-%m-%d %H:%M')}")
    y -= 16
    pdf.drawString(margin_x, y, f"Última actualización: {order.updated_at.strftime('%Y-%m-%d %H:%M')}")
    y -= 28

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(margin_x, y, "Datos del cliente")
    y -= 20

    pdf.setFont("Helvetica", 10)
    pdf.drawString(margin_x, y, f"Nombre: {order.customer_name}")
    y -= 16
    pdf.drawString(margin_x, y, f"Contacto: {order.contact_info}")
    y -= 24

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(margin_x, y, "Equipo")
    y -= 20

    pdf.setFont("Helvetica", 10)
    pdf.drawString(margin_x, y, f"Modelo: {order.equipment_model}")
    y -= 16
    pdf.drawString(margin_x, y, f"Nº de serie: {order.serial_number}")
    y -= 24

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(margin_x, y, "Detalles de la orden")
    y -= 20

    pdf.setFont("Helvetica", 10)
    pdf.drawString(margin_x, y, f"Motivo de ingreso: {order.intake_reason}")
    y -= 16
    pdf.drawString(margin_x, y, f"Estado: {order.status.value}")
    y -= 16

    warranty_text = "Sí" if order.warranty else "No"
    pdf.drawString(margin_x, y, f"En garantía: {warranty_text}")
    y -= 16

    pdf.drawString(margin_x, y, f"Costo estimado: {order.estimated_cost} ARS")
    y -= 24

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(margin_x, y, "Diagnóstico técnico")
    y -= 20

    pdf.setFont("Helvetica", 10)
    diagnosis = order.diagnosis or "Pendiente"

    # Simple multi-line handling for diagnosis
    max_width = width - margin_x * 2
    words = diagnosis.split()
    line = ""
    for word in words:
        test_line = f"{line} {word}".strip()
        if pdf.stringWidth(test_line, "Helvetica", 10) <= max_width:
            line = test_line
        else:
            pdf.drawString(margin_x, y, line)
            y -= 14
            line = word
    if line:
        pdf.drawString(margin_x, y, line)

    pdf.showPage()
    pdf.save()

    pdf_bytes = buffer.getvalue()
    buffer.close()
    return pdf_bytes

