import frappe
from frappe.model.document import Document

def before_save(doc, method):
    if doc.status == "Resolved":
        doc.resolved_by = frappe.session.user