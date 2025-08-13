# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import get_fullname, get_url
from frappe.model.document import Document


class LeaveResumption(Document):
	def on_submit(self):
		self.notify_line_manager()

	def notify_line_manager(self):
		if not self.employee:
			return
			
		try:
			employee = frappe.get_doc("Employee", self.employee)
			
			if not employee.reports_to:
				frappe.log_error(f"Leave Resumption {self.name} has no Line Manager for employee {self.employee}")
				return
				
			lm_employee = frappe.get_doc("Employee", employee.reports_to)
			
			if not lm_employee.user_id:
				frappe.log_error(f"Line Manager {employee.reports_to} has no linked user_id")
				return
				
			lm_user = lm_employee.user_id
			
			subject = f"Leave Resumption Submitted by {get_fullname(employee.user_id)}"
			message = f"""
                <p>Dear {get_fullname(lm_user)},</p>
                <p>A leave resumption has been submitted by <strong>{get_fullname(employee.user_id)}</strong>.</p>
                <p><strong>Join Date:</strong> {self.join_date}<br>
                <strong>Comment:</strong> {self.comment or 'No comment provided'}</p>
                <p><a href="{get_url()}/app/leave-resumption/{self.name}">View Request</a></p>
            """
			
			frappe.sendmail(
                recipients=[lm_user],
                subject=subject,
                message=message
            )

			create_system_notification(message, lm_user, subject)
			frappe.publish_realtime(
                event='eval_js',
                message=f"frappe.show_alert('New Leave Resumption from {get_fullname(employee.user_id)}')",
                user=lm_user
            )
			
		except Exception as e:
			frappe.log_error(f"Failed to notify LM for Leave Resumption {self.name}: {str(e)}")


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
