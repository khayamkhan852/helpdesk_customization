import frappe

def execute():
    print("Populating custom fields for ToDo...")
    
    frappe.db.sql("""
        UPDATE `tabToDo`
        SET
            custom_allocated_to_name = allocated_to_name,
            custom_mobile_no = mobile_no
    """)
    frappe.db.commit()

    print("Custom fields populated successfully.")