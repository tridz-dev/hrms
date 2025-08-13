# Leave Resumption Feature

This document describes the frontend and backend changes to introduce the Leave Resumption feature in the HRMS app, following the same patterns used for Asset Request and Employee Resignation.

## Overview

- Add a new entry point from `Profile` for Leave Resumption
- Provide a dashboard page with recent Leave Resumption entries and a CTA to apply
- Provide a list view page with filters
- Provide a form view page to create or edit Leave Resumption
- Add an API to fetch recent Leave Resumption requests for the logged-in employee

## Backend

- API: `hrms.api.leave_resumption.get_leave_resumption_requests(employee: str, for_approval: bool = False, limit: int | None = None)`
  - File: `apps/hrms/hrms/api/leave_resumption.py`
  - Returns a list of `Leave Resumption` docs with fields: `name, employee, join_date, comment, docstatus, creation` and optionally `workflow_state` if present

## Frontend

- Data resource
  - File: `apps/hrms/frontend/src/data/leave_resumption.js`
  - Resource key: `myLeaveResumptionRequests`
  - Endpoint: `hrms.api.leave_resumption.get_leave_resumption_requests`

- Item component
  - File: `apps/hrms/frontend/src/components/LeaveResumptionItem.vue`
  - Mirrors `AssetRequestItem.vue`/`ResignationRequestItem.vue` to display a single entry

- Request summary fields
  - Updated: `apps/hrms/frontend/src/data/config/requestSummaryFields.js`
  - Added export: `LEAVE_RESUMPTION_FIELDS` with `name, employee, join_date, comment, docstatus`
  - Mapped in `RequestList.vue` as `"Leave Resumption": LEAVE_RESUMPTION_FIELDS`

- Views
  - Dashboard: `apps/hrms/frontend/src/views/LeaveResumptionDashboard.vue`
    - Recent list (top 5), CTA to open form, action sheet integration
  - List: `apps/hrms/frontend/src/views/LeaveResumptionApplicationList.vue`
  - Form: `apps/hrms/frontend/src/views/LeaveResumptionApplication.vue`
    - Uses `get_doctype_fields('Leave Resumption')`
    - On create, hides `employee` field; sets `employee` to current user on validate
    - Sets read-only if viewing other employee’s document

- Router updates
  - File: `apps/hrms/frontend/src/router/index.js`
  - Added routes:
    - `LeaveResumptionDashboard` → `/leave-resumption-dashboard`
    - `LeaveResumptionListView` → `/leave-resumption-list`
    - `LeaveResumptionFormView` → `/leave-resumption-form/:id?`

- Profile link
  - File: `apps/hrms/frontend/src/views/Profile.vue`
  - Added a new action link: `Leave Resumption` that navigates to `LeaveResumptionDashboard`

## Usage

1. Navigate to Profile → Leave Resumption
2. Use the Apply button to create a new Leave Resumption
3. View recent items on the dashboard or click View List for full history
4. Tap an item to open the action sheet and, if Draft, open the form for editing

## Notes

- This feature reuses existing patterns and components to ensure consistency
- No changes were made to existing Asset Request or Resignation features

## Known Limitations

- Workflow state is surfaced only if a `workflow_state` field exists on the doctype
- The backend API currently supports `for_approval` for parity but approver field is not wired


