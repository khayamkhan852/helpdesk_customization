app_name = "helpdesk_customization"
app_title = "Helpdesk Customization"
app_publisher = "Khayam Khan"
app_description = "This is the App for Helpdesk for custom customizations"
app_email = "khayamkhan852@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "helpdesk_customization",
# 		"logo": "/assets/helpdesk_customization/logo.png",
# 		"title": "Helpdesk Customization",
# 		"route": "/helpdesk_customization",
# 		"has_permission": "helpdesk_customization.api.permission.has_app_permission"
# 	}
# ]

fixtures = [
    {
        "dt": "Custom Field", "filters": [
            [
                "name", "in", [
                    "Sales Invoice-custom_contract",
				    "Sales Invoice-custom_period_start",
                    "Sales Invoice-custom_period_end",
                    "Sales Order-custom_contract",
                    "Sales Order-custom_period_start",
                    "Sales Order-custom_period_end",
                    "ToDo-custom_allocated_to_name",
                    "ToDo-custom_mobile_no",
                    "HD Ticket-custom_resolved_by",
                    "CRM Lead-custom_message",
                    "WhatsApp Notification-custom_minutes",
                    "Quotation-custom_scope_of_work_arabic",
                    "Quotation-custom_scope_of_work_english",
                    "Quotation-custom_scope_of_work",
                ]
            ]
        ]
    },
    "Terms and Conditions",
    {
        "dt": "Property Setter", "filters": [
            [
                "name", "in", [
                    "Sales Invoice-main-field_order",
                    "Sales Invoice-dimension_col_break-hidden",
                    "WhatsApp Notification-doctype_event-options",
                    "WhatsApp Notification-main-field_order",
                    "WhatsApp Notification-date_changed-depends_on",
                    "Quotation-main-field_order",
                ]
            ]
        ]
    }
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/helpdesk_customization/css/helpdesk_customization.css"
# app_include_js = "/assets/helpdesk_customization/js/helpdesk_customization.js"

# include js, css files in header of web template
# web_include_css = "/assets/helpdesk_customization/css/helpdesk_customization.css"
# web_include_js = "/assets/helpdesk_customization/js/helpdesk_customization.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "helpdesk_customization/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "helpdesk_customization/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "helpdesk_customization.utils.jinja_methods",
# 	"filters": "helpdesk_customization.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "helpdesk_customization.install.before_install"
# after_install = "helpdesk_customization.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "helpdesk_customization.uninstall.before_uninstall"
# after_uninstall = "helpdesk_customization.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "helpdesk_customization.utils.before_app_install"
# after_app_install = "helpdesk_customization.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "helpdesk_customization.utils.before_app_uninstall"
# after_app_uninstall = "helpdesk_customization.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "helpdesk_customization.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
    "WhatsApp Notification": "helpdesk_customization.overrides.whatsapp_notification.CustomWhatsAppNotification"
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "ToDo": {
        "validate": "helpdesk_customization.custom_python_scripts.todo.validate"
    },
    "HD Ticket": {
        "before_save": "helpdesk_customization.custom_python_scripts.hd_ticket.before_save"
    } 
}

# Scheduled Tasks
# ---------------

scheduler_events = {
	"cron": {
		"* * * * *": [
            "helpdesk_customization.custom_python_scripts.whatsapp_notification.trigger_notifications_every_minute"
		]
	}
}

# Testing
# -------

# before_tests = "helpdesk_customization.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "helpdesk_customization.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "helpdesk_customization.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["helpdesk_customization.utils.before_request"]
# after_request = ["helpdesk_customization.utils.after_request"]

# Job Events
# ----------
# before_job = ["helpdesk_customization.utils.before_job"]
# after_job = ["helpdesk_customization.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"helpdesk_customization.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

