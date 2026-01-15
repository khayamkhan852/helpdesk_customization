import frappe

def after_insert(doc, method):
    if not doc.mobile_no and not doc.links:
        return

    for link in doc.links:
        if link.link_doctype == "HD Customer":
            hd_customer = frappe.get_doc(link.link_doctype, link.link_name)
            if hd_customer.name and not hd_customer.custom_contact:
                hd_customer.custom_contact = doc.name
                hd_customer.save(ignore_permissions=True)
                break