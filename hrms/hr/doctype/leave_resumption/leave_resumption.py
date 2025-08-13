# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import get_fullname, get_url
from frappe.model.document import Document
from hrms.hr.utils import (
	notify_line_manager, 
	create_system_notification, 
	get_leave_resumption_notification_data
)


class LeaveResumption(Document):
	def on_submit(self):
		self.notify_line_manager()

	def notify_line_manager(self):
		subject_template = "Leave Resumption Submitted by {employee_name}"
		message_template = """
			<p>Dear {lm_name},</p>
			<p>A leave resumption has been submitted by <strong>{employee_name}</strong>.</p>
			<p>{additional_info}</p>
			<p><a href="{doc_url}">View Request</a></p>
		"""
		
		additional_fields = get_leave_resumption_notification_data(self)
		
		notify_line_manager(
			doc=self,
			doctype_name="Leave Resumption",
			subject_template=subject_template,
			message_template=message_template,
			additional_fields=additional_fields
		)
