# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "document_library"
app_title = "Document Library"
app_publisher = "PT. Mitra Computa Asia, Indonesia"
app_description = "Document Library is a custom ERPNext application to track, manage, store and keep versions of documents soft-copies."
app_icon = "octicon octicon-file-submodule"
app_color = "#ba1d1d"
app_email = "info@mitra.computa.asia"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/document_library/css/document_library.css"
# app_include_js = "/assets/document_library/js/document_library.js"

# include js, css files in header of web template
# web_include_css = "/assets/document_library/css/document_library.css"
# web_include_js = "/assets/document_library/js/document_library.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "document_library.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "document_library.install.before_install"
# after_install = "document_library.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "document_library.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"document_library.tasks.all"
# 	],
# 	"daily": [
# 		"document_library.tasks.daily"
# 	],
# 	"hourly": [
# 		"document_library.tasks.hourly"
# 	],
# 	"weekly": [
# 		"document_library.tasks.weekly"
# 	]
# 	"monthly": [
# 		"document_library.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "document_library.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "document_library.event.get_events"
# }

