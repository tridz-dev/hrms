# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import get_fullname, get_url
from frappe.model.document import Document
from hrms.hr.utils import (
	notify_line_manager, 
	create_system_notification, 
	get_asset_request_notification_data
)


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
		subject_template = "Asset Request Submitted by {employee_name}"
		message_template = """
			<p>Dear {lm_name},</p>
			<p>An asset request has been submitted by <strong>{employee_name}</strong>.</p>
			<p>{additional_info}</p>
			<p><a href="{doc_url}">View Request</a></p>
		"""
		
		additional_fields = get_asset_request_notification_data(self)
		
		notify_line_manager(
			doc=self,
			doctype_name="Asset Request",
			subject_template=subject_template,
			message_template=message_template,
			additional_fields=additional_fields
		)

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