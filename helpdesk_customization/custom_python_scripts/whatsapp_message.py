import frappe
import json

def after_insert(doc, method):
    if doc.type != "Incoming" and doc.content_type != "flow" and not doc.flow_response:
        return

    if not doc.is_reply:
        return

    try:
        flow_response = json.loads(doc.flow_response)

        ticket_subject = flow_response.get("subject")
        ticket_description = flow_response.get("description")
        priority = flow_response.get("priority")
        domain = flow_response.get("domain")
        issue_type = flow_response.get("issue_type")

        if not (ticket_subject and ticket_description):
            return

        hd_ticket = frappe.get_doc({
            "doctype": "HD Ticket",
            "subject": ticket_subject,
            "description": ticket_description,
            "priority": priority,
            "status": "Open",
        })

        hd_ticket.insert(ignore_permissions=True)
    
    except Exception as e:
        frappe.log_error(
            frappe.get_traceback(),
            "WhatsApp Flow → HD Ticket Creation Failed"
        )


