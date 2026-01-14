import frappe

def execute():
    print("Populating custom fields for CRM Lead...")
    
    frappe.db.sql("""
        UPDATE `tabCRM Lead`
        SET
            custom_message = initial_message3
    """)
    frappe.db.commit()

    print("Custom fields populated successfully.")