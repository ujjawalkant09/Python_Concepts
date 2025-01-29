"""
SOLID Principle 
"""

import abc




"""
S stand for Single Responsibility Principle
single region to change
A class have only one region to change
"""
# If you see below here every class follow single responsibility principle like InvoicePrinter will print invoice
#  and InvoiceSaver will save the invoice 

class Invoice:
    def __init__(self, items, tax_rate):
        self.items = items
        self.tax_rate = tax_rate

    def calculate_total(self):
        return sum(self.items) * (1 + self.tax_rate)

class InvoicePrinter:
    def print_invoice(self, invoice):
        print(f"Invoice Total: {invoice.calculate_total()}")

class InvoiceSaver:
    def save_to_db(self, invoice):
        print("Invoice saved to database.")

# Usage Example
invoice = Invoice([100, 200, 300], 0.1)  # List of items and 10% tax rate
printer = InvoicePrinter()
saver = InvoiceSaver()

printer.print_invoice(invoice)  # ✅ Handles only printing
saver.save_to_db(invoice)       # ✅ Handles only saving
