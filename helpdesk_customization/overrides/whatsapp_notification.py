import frappe
import json
from frappe import _
from frappe_whatsapp.frappe_whatsapp.doctype.whatsapp_notification.whatsapp_notification import WhatsAppNotification
from frappe.utils import add_to_date, datetime, now_datetime

class CustomWhatsAppNotification(WhatsAppNotification):
    def get_document_for_minutes(self):
        now = now_datetime()

        target_time_start = add_to_date(now, minutes=self.custom_minutes).replace(second=0, microsecond=0)
        target_time_end = target_time_start + datetime.timedelta(minutes=1)

        doc_list = frappe.get_all(
            self.reference_doctype,
            fields="name",
            filters=[
                [self.date_changed, ">=", target_time_start],
                [self.date_changed, "<", target_time_end],
            ]
        )

        for d in doc_list:
            doc = frappe.get_doc(self.reference_doctype, d.name)
            self.send_template_message(doc)
