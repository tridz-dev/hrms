# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import get_fullname, get_url
from frappe.model.document import Document


class EmployeeResignation(Document):
	def on_submit(self):
		self.notify_line_manager()

	def on_update_after_submit(self):
		frappe.log_error(f"Employee Resignation {self.name} status: {self.workflow_state}")
		if self.workflow_state == "Approved":
			self.process_resignation()

	def notify_line_manager(self):
		frappe.log_error(f"Employee Resignation {self.name} has no Line Manager for employee {self.employee}")
		if not self.employee:
			return
			
		try:
			employee = frappe.get_doc("Employee", self.employee)
			
			if not employee.reports_to:
				frappe.log_error(f"Employee Resignation {self.name} has no Line Manager for employee {self.employee}")
				return
				
			lm_employee = frappe.get_doc("Employee", employee.reports_to)
			
			if not lm_employee.user_id:
				frappe.log_error(f"Line Manager {employee.reports_to} has no linked user_id")
				return
				
			lm_user = lm_employee.user_id
			
			subject = f"Resignation Request Submitted by {get_fullname(employee.user_id)}"
			message = f"""
                <p>Dear {get_fullname(lm_user)},</p>
                <p>A resignation request has been submitted by <strong>{get_fullname(employee)}</strong>.</p>
                <p><strong>Resignation Date:</strong> {self.resignation_submission_date}<br>
                <strong>Last Working Day:</strong> {self.last_working_date}<br>
                <strong>Reason for Resignation:</strong> {self.reason_for_resignation}</p>
                <p><a href="{get_url()}/app/employee-resignation/{self.name}">View Request</a></p>
            """
			
			frappe.sendmail(
                recipients=[lm_user],
                subject=subject,
                message=message
            )

			create_system_notification(message, lm_user, subject)
			frappe.publish_realtime(
                event='eval_js',
                message=f"frappe.show_alert('New Resignation Request from {get_fullname(self.employee)}')",
                user=lm_user
            )
			
		except Exception as e:
			frappe.log_error(f"Failed to notify LM for Employee Resignation {self.name}: {str(e)}")

	def process_resignation(self):
		try:
			employee = frappe.get_doc("Employee", self.employee)
			employee.resignation_letter_date = self.resignation_submission_date	
			employee.reason_for_leaving = self.reason_for_resignation
			employee.save()
			
			frappe.log_error(f"Successfully processed resignation for Employee {self.employee}")
		except Exception as e:
			frappe.log_error(f"Failed to process resignation for Employee Resignation {self.name}: {str(e)}")

		
def create_system_notification(message, user, subject):
	try:
		communication = frappe.get_doc(
			{
				"doctype": "Notification Log",
				"email_content": message,
				"for_user": user,
				"subject": subject,
				"type": "Alert",
			}
		)
		communication.insert(ignore_permissions=True)
	except Exception as e:
		frappe.log_error(f"Failed to create system notification: {str(e)}")
