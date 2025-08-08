# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import get_fullname, get_url
from frappe.model.document import Document


class AssetRequest(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		asset_item: DF.Link | None
		employee: DF.Link | None
		reason_for_request: DF.Text | None
		request_date: DF.Date | None
		requested_item_name: DF.Data | None
	# end: auto-generated types
	def on_submit(self):
		self.notify_line_manager()

	def on_update_after_submit(self):
		frappe.log_error(f"Asset Request {self.name} status: {self.workflow_state}")
		if self.workflow_state == "Approved":
			self.create_asset_movement()

	def notify_line_manager(self):
		frappe.log_error(f"Asset Request {self.name} has no Line Manager for employee {self.employee}")
		if not self.employee:
			return
			
		try:
			employee = frappe.get_doc("Employee", self.employee)
			
			if not employee.reports_to:
				frappe.log_error(f"Asset Request {self.name} has no Line Manager for employee {self.employee}")
				return
				
			lm_employee = frappe.get_doc("Employee", employee.reports_to)
			
			if not lm_employee.user_id:
				frappe.log_error(f"Line Manager {employee.reports_to} has no linked user_id")
				return
				
			lm_user = lm_employee.user_id
			
			subject = f"Asset Request Submitted by {get_fullname(employee.user_id)}"
			message = f"""
                <p>Dear {get_fullname(lm_user)},</p>
                <p>An asset request has been submitted by <strong>{get_fullname(employee)}</strong>.</p>
                <p><strong>Requested Item:</strong> {self.requested_item_name}<br>
                <strong>Reason for Request:</strong> {self.reason_for_request}</p>
                <p><a href="{get_url()}/app/asset-request/{self.name}">View Request</a></p>
            """
			
			frappe.sendmail(
                recipients=[lm_user],
                subject=subject,
                message=message
            )

			create_system_notification(message, lm_user, subject)
			frappe.publish_realtime(
                event='eval_js',
                message=f"frappe.show_alert('New Asset Request from {get_fullname(self.employee)}')",
                user=lm_user
            )
			
		except Exception as e:
			frappe.log_error(f"Failed to notify LM for Asset Request {self.name}: {str(e)}")

	def create_asset_movement(self):
		try:
			asset_movement = frappe.get_doc(
			{
				"doctype": "Asset Movement",
				"purpose": "Issue",
				"assets":[{
					"asset": self.asset_item,
					"to_employee": self.employee,
				}]	
			}

			)
			asset_movement.insert()
			asset_movement.submit()
		except Exception as e:
			frappe.log_error(f"Failed to create Asset Movement for Asset Request {self.name}: {str(e)}")

		
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