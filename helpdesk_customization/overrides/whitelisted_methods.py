# Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


import json

import frappe
from frappe.model.document import Document
from frappe.utils.jinja import validate_template

@frappe.whitelist()
def get_contract_template(template_name, doc):
	if isinstance(doc, str):
		doc = json.loads(doc)

	contract_template = frappe.get_doc("Contract Template", template_name)
	contract_terms = None
	service_terms = None
	bank_details = None

	if contract_template.contract_terms:
		contract_terms = frappe.render_template(contract_template.contract_terms, doc)

	if contract_template.service_terms:
		service_terms = frappe.render_template(contract_template.service_terms, doc)

	if contract_template.service_terms:
		bank_details = frappe.render_template(contract_template.bank_details, doc)

	return {"contract_template": contract_template, "contract_terms": contract_terms, "service_terms": service_terms, "bank_details": bank_details}
