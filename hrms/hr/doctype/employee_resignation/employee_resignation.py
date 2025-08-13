# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import get_fullname, get_url
from frappe.model.document import Document
from hrms.hr.utils import (
	notify_line_manager, 
	create_system_notification, 
	get_resignation_notification_data
)


class EmployeeResignation(Document):
	def on_submit(self):
		self.notify_line_manager()

	def on_update_after_submit(self):
		frappe.log_error(f"Employee Resignation {self.name} status: {self.workflow_state}")
		if self.workflow_state == "Approved":
			self.process_resignation()

	def notify_line_manager(self):
		subject_template = "Resignation Request Submitted by {employee_name}"
		message_template = """
			<p>Dear {lm_name},</p>
			<p>A resignation request has been submitted by <strong>{employee_name}</strong>.</p>
			<p>{additional_info}</p>
			<p><a href="{doc_url}">View Request</a></p>
		"""
		
		additional_fields = get_resignation_notification_data(self)
		
		notify_line_manager(
			doc=self,
			doctype_name="Employee Resignation",
			subject_template=subject_template,
			message_template=message_template,
			additional_fields=additional_fields
		)

	def process_resignation(self):
		try:
			employee = frappe.get_doc("Employee", self.employee)
			employee.resignation_letter_date = self.resignation_submission_date	
			employee.reason_for_leaving = self.reason_for_resignation
			employee.save()
			
			frappe.log_error(f"Successfully processed resignation for Employee {self.employee}")
		except Exception as e:
			frappe.log_error(f"Failed to process resignation for Employee Resignation {self.name}: {str(e)}")
