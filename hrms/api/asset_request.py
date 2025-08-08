import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import nowdate
from frappe.exceptions import ValidationError


@frappe.whitelist()
def get_asset_requests(
    employee: str,
    for_approval: bool = False,
    limit: int | None = None,
) -> list[dict]:
    filters = {"employee": employee}

    # If for_approval is True, get requests where current user is approver
    if for_approval:
        user = frappe.session.user
        approver_employee = frappe.db.get_value("Employee", {"user_id": user}, "name")
        if approver_employee:
            filters["approver"] = approver_employee

    fields = [
        "name",
        "employee",
        "request_date",
        "requested_item_name",
        "asset_item",
        "reason_for_request",
        "docstatus",
        "creation",
    ]

    # Check if workflow state field exists
    workflow_state_field = None
    try:
        workflow_state_field = frappe.get_meta("Asset Request").get_field(
            "workflow_state"
        )
        if workflow_state_field:
            fields.append("workflow_state")
    except:
        pass

    asset_requests = frappe.get_list(
        "Asset Request",
        fields=fields,
        filters=filters,
        order_by="creation desc",
        limit=limit,
    )

    if workflow_state_field:
        for request in asset_requests:
            request["workflow_state_field"] = "workflow_state"

    return asset_requests 