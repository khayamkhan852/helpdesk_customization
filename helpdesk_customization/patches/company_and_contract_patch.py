import frappe

def execute():
    frappe.db.sql("""
        UPDATE `tabContract Template`
        SET
            custom_general_termsofservice = service_terms,
            custom_bank_details = bank_details
    """)

    frappe.db.sql("""
        UPDATE `tabCompany`
        SET
            custom_company_arabic = company_arabic
    """)        

    frappe.db.sql("""
        UPDATE `tabContract`
        SET
            custom_transaction_date = transaction_date,
            custom_company = company,
            custom_company_name_in_arabic = company_name_in_arabic,
            custom_general_termsofservice = service_terms
    """)



    frappe.db.commit()