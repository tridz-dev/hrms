import frappe
from frappe import _


@frappe.whitelist()
def get_leave_resumption_requests(
    employee: str,
    for_approval: bool = False,
    limit: int | None = None,
) -> list[dict]:
    """Return recent Leave Resumption requests for an employee.

    Mirrors the structure of get_resignation_requests/asset_requests
    so the frontend can reuse common list/details UIs.
    """

    filters: dict[str, object] = {"employee": employee}

    # For parity with resignation API (future-proof if approver is added)
    if for_approval:
        user = frappe.session.user
        approver_employee = frappe.db.get_value("Employee", {"user_id": user}, "name")
        if approver_employee:
            filters["approver"] = approver_employee

    fields = [
        "name",
        "employee",
        "join_date",
        "comment",
        "docstatus",
        "creation",
    ]

    # If workflow_state exists, include and annotate like other APIs
    workflow_state_field = None
    try:
        workflow_state_field = frappe.get_meta("Leave Resumption").get_field(
            "workflow_state"
        )
        if workflow_state_field:
            fields.append("workflow_state")
    except Exception:
        pass

    requests = frappe.get_list(
        "Leave Resumption",
        fields=fields,
        filters=filters,
        order_by="creation desc",
        limit=limit,
    )

    if workflow_state_field:
        for r in requests:
            r["workflow_state_field"] = "workflow_state"

    return requests


