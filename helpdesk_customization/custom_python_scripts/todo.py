import frappe
from frappe.model.document import Document

def validate(doc, method):
    if doc.reference_type and doc.allocated_to:
        user = frappe.get_doc("User", doc.allocated_to)
        if user.enabled and user.mobile_no:
            doc.mobile_no = user.mobile_no
        
        if doc.reference_type == "CRM Task":
            crm_task = frappe.get_doc('CRM Task', doc.reference_name)
            doc.custom_task_due_date = crm_task.due_date
    