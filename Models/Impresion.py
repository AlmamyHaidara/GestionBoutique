import subprocess

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_invoice(data):
    # Créer un objet Canvas
    pdf = canvas.Canvas("invoice.pdf", pagesize=letter)

    # Ajouter les informations de la facture
    # ...

    # Enregistrer le PDF
    pdf.save()


# Appeler la fonction pour générer la facture
data = {
    "invoice_number": "INV-2023-001",
    "invoice_date": "2023-04-16",
    "customer_name": "John Doe",
    "customer_address": "123 Main St, Anytown USA",
    "invoice_items": [
        {
            "name": "Produit 1",
            "quantity": 2,
            "unit_price": 10.99,
            "total": 21.98
        },
        {
            "name": "Produit 2",
            "quantity": 1,
            "unit_price": 5.50,
            "total": 5.50
        },
        {
            "name": "Produit 3",
            "quantity": 3,
            "unit_price": 8.75,
            "total": 26.25
        }
    ],
    "total": 53.73
}
generate_invoice(data)

# Ouvrir le fichier PDF généré avec l'application de visualisation de PDF par défaut
subprocess.run(["open", "invoice.pdf"], check=True)
