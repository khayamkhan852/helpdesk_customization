import frappe

def execute():
    print("Populating custom fields for ToDo...")
    
    frappe.db.sql("""
        UPDATE `tabHD Ticket`
        SET
            custom_talha_phone = talha_phone
    """)
    frappe.db.commit()

    print("Custom fields populated successfully.")