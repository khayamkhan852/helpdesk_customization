import frappe

def execute():
    print("Populating custom fields for Sales Orders...")
    
    frappe.db.sql("""
        UPDATE `tabSales Order`
        SET
            custom_period_start = period_start,
            custom_period_end = period_end,
            custom_contract = contract
    """)
    frappe.db.commit()

    print("Custom fields populated successfully.")