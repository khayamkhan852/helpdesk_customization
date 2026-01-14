import frappe

def execute():
    print("Populating custom fields for Quotation...")
    
    frappe.db.sql("""
        UPDATE `tabQuotation`
        SET
            custom_scope_of_work_english = scope_of_work_english,
            custom_scope_of_work_arabic = scope_of_work_arabic
    """)
    frappe.db.commit()

    print("Custom fields populated successfully.")