# Resignation Flow Update

## Nature of the Change
- The resignation request flow now mirrors the attendance request flow for consistency and improved user experience.
- Users can view a dashboard with recent resignation requests, open details in a modal, and create or edit requests as needed.

## Rationale
- Aligns resignation UX with other HRMS modules (like Attendance) for familiarity and ease of use.
- Provides quick access to request details and actions via modals.

## Usage Instructions
- **Dashboard**: Access via the Resignation menu. See recent requests and click to view details in a modal.
- **Create New**: Click 'Request Resignation' or 'New Resignation' to open the form for a new request.
- **Edit**: In the modal, if the request is in draft, click the link/button to edit and submit.
- **View List**: Click 'View List' to see all resignation requests.

## Developer Notes
- Uses `RequestList.vue` and `RequestActionSheet.vue` for listing and modal details.
- Routing updated for dashboard, list, and form views.
- No breaking changes to other modules. 