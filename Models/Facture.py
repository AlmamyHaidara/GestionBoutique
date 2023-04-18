import subprocess

import cups
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_invoice(data):
    # Créer un objet Canvas
    pdf = canvas.Canvas("invoice.pdf", pagesize=letter)

    # Définir les polices et tailles de texte
    pdf.setFont("Helvetica-Bold", 16)
    pdf.setFont("Helvetica", 12)

    # Ajouter les informations de facture
    pdf.drawString(50, 750, "Facture n°: {}".format(data["invoice_number"]))
    pdf.drawString(50, 725, "Date: {}".format(data["invoice_date"]))
    pdf.drawString(50, 700, "Client: {}".format(data["customer_name"]))
    pdf.drawString(50, 675, "Adresse: {}".format(data["customer_address"]))

    # Ajouter les détails de la facture
    pdf.drawString(50, 625, "Désignation")
    pdf.drawString(200, 625, "Quantité")
    pdf.drawString(300, 625, "Prix unitaire")
    pdf.drawString(400, 625, "Total")

    y = 600
    for item in data["invoice_items"]:
        pdf.drawString(50, y, item["name"])
        pdf.drawString(200, y, str(item["quantity"]))
        pdf.drawString(300, y, "${:.2f}".format(item["unit_price"]))
        pdf.drawString(400, y, "${:.2f}".format(item["total"]))
        y -= 25

    # Ajouter le total de la facture
    pdf.drawString(300, y - 25, "Total:")
    pdf.drawString(400, y - 25, "${:.2f}".format(data["total"]))

    # Enregistrer le PDF
    pdf.save()
    conn = cups.Connection()
    printers = conn.getPrinters()
    printer_name = "My Printer"
    if printer_name in printers:
        printer_uri = printers[printer_name]["device-uri"]
        conn.printFile(printer_name, "invoice.pdf", "Facture", {})
    else:
        print("L'imprimante {} n'est pas disponible".format(printer_name))
    subprocess.run(["open", "invoice.pdf"], check=True)
    print("Finished")
