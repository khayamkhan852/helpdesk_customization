import frappe

def trigger_notifications_every_minute(method="every_minute"):
    if frappe.flags.in_import or frappe.flags.in_patch:
        # don't send notifications while syncing or patching
        return

    if method == "every_minute":
        doc_list = frappe.get_all(
            "WhatsApp Notification", filters={"doctype_event": ("in", ("Minutes Before")), "disabled": 0}
        )
        for d in doc_list:
            alert = frappe.get_doc("WhatsApp Notification", d.name)
            alert.get_document_for_minutes()