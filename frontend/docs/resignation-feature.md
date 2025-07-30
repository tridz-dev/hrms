# Resignation Application Feature

## Overview
This document describes the implementation of the resignation application feature in the HRMS frontend. The feature allows employees to submit resignation applications through the mobile app interface.

## Changes Made

### 1. New View Component
**File:** `src/views/ResignationApplication.vue`

- **Purpose:** Provides a form interface for employees to submit resignation applications
- **Features:**
  - Uses HRMS standard FormView component for consistent design
  - Dynamic field generation from backend API
  - Date picker for resignation date (minimum 30 days from current date)
  - Optional text area for resignation reason
  - Real-time form validation
  - Standard HRMS form submission handling
  - Consistent UI/UX with other HRMS forms

### 2. Router Configuration
**File:** `src/router/index.js`

- **Change:** Added new route for resignation application
- **Route:** `/resignation-application`
- **Component:** `ResignationApplication.vue`

### 3. Profile View Enhancement
**File:** `src/views/Profile.vue`

- **Changes:**
  - Added new profile link for "Resignation Application" after salary information
  - Implemented conditional styling for resignation option (red color theme)
  - Added `handleLinkClick` function to handle different types of profile links
  - Modified click handler to support both modal and navigation actions

## Technical Implementation Details

### Form Architecture
- Uses HRMS standard `FormView` component
- Manually defined fields (no backend doctype required)
- Follows the same pattern as other HRMS forms (Attendance Request, Leave Application, etc.)
- Custom validation logic for resignation date requirements

### Form Validation
- Resignation date must be at least 30 days from the current date
- Date field is required with minimum date constraint
- Reason field is optional
- Real-time validation with error messages displayed inline

### UI/UX Design
- Consistent with existing HRMS form design patterns
- Uses standard FormField components for all inputs
- Red color theme for resignation option in profile to indicate its serious nature
- Responsive design for mobile and desktop
- Standard HRMS form submission flow with loading states

### Backend Integration
- Placeholder API call structure is included in the code
- Ready for backend implementation
- Error handling for failed submissions

## Files Modified

1. **`src/views/ResignationApplication.vue`** (New)
   - Complete resignation form component
   - Manually defined fields (resignation_date, reason)
   - Custom validation logic for date requirements

2. **`src/router/index.js`**
   - Added route: `/resignation-application`

3. **`src/views/Profile.vue`**
   - Added resignation option to profile links
   - Enhanced click handling logic
   - Added conditional styling

4. **`src/utils/dialogs.js`**
   - Added `showSuccessAlert` function for success notifications

## Backend Requirements (Future Implementation)

The frontend is prepared for the following backend API:

### Form Submission API
The form will use the standard HRMS form submission mechanism through the FormView component, which typically calls:
```python
# Standard form submission endpoint
# Parameters: All form field values including:
{
    "employee": "employee_id",
    "resignation_date": "YYYY-MM-DD",
    "reason": "optional_reason_text",
    "doctype": "Resignation Application"
}
```

**Note:** No backend doctype is required as fields are manually defined in the frontend.

## Usage Instructions

1. Navigate to Profile section in the HRMS app
2. Scroll down to find "Resignation Application" option (appears in red)
3. Click on the option to open the resignation form
4. Select a resignation date (minimum 30 days from today)
5. Optionally provide a reason for resignation
6. Click "Submit Resignation" to submit the application
7. Use "Cancel" to return to profile without submitting

## Notes

- The feature maintains consistency with existing HRMS functionality
- No existing features are affected by these changes
- The implementation follows Frappe UI standards and patterns
- Error handling and user feedback are properly implemented
- The form includes proper validation to ensure data integrity

## Future Enhancements

1. Backend API implementation for actual resignation submission
2. Integration with approval workflow
3. Email notifications to HR and managers
4. Status tracking for submitted applications
5. Ability to view and manage existing resignation applications 

## 2024-XX-XX: Custom Backend API Integration

### Backend API Implementation
- **File:** `apps/hrms/hrms/api/resignation.py`
- **Function:** `save_resignation`
- **Purpose:** Saves resignation details (date, reason) directly to the Employee DocType using the employee ID, without requiring a Resignation Application doctype.
- **API Endpoint:** `hrms.api.resignation.save_resignation`
- **Parameters:**
  - `employee_id` (str): Employee ID (required)
  - `resignation_letter_date` (str): Date of resignation (required)
  - `reason_for_leaving` (str): Reason for resignation (optional)
- **Behavior:**
  - Updates the `resignation_letter_date` and `reason_for_leaving` fields in the Employee DocType.
  - Returns a success or error message.
  - Does not affect any other Employee fields or features.

### Frontend Integration
- **File:** `src/views/ResignationApplication.vue`
- **Change:**
  - The form now calls the custom API endpoint (`hrms.api.resignation.save_resignation`) on save, instead of the default DocType save logic.
  - Passes employee ID, resignation date, and reason to the backend.
  - Displays success or error toasts based on the API response.
  - Employee ID and name are shown as read-only fields in the form.

### Usage Instructions (Updated)

1. Open the "Resignation Application" form from the Profile section.
2. Employee ID and name are pre-filled and read-only.
3. Select a resignation date (minimum 30 days from today).
4. Optionally provide a reason for resignation.
5. Click "Save" to submit. The data is sent to the backend and saved in the Employee record.
6. Success or error feedback is shown.

### Notes
- No existing features or doctypes are affected.
- The change is modular and only impacts the resignation form logic.
- All changes follow Frappe UI and project coding standards. 

## 2024-XX-XX: Custom Standalone Resignation Form (No DocType Required)

### What Changed
- **New file:** `src/views/ResignationApplicationCustom.vue`
- **Purpose:** Provides a resignation form UI that does NOT use FormView and does NOT require a doctype.
- **Fields:** Employee ID (read-only), Employee Name (read-only), Resignation Date (min 30 days from today), Reason for Resignation (optional)
- **Validation:** Same as before (date must be at least 30 days from today)
- **Save Action:** Calls the custom backend API (`hrms.api.resignation.save_resignation`) directly on save button click.
- **UI:** Uses the same FormField component and styling as other HRMS forms for consistency.
- **No impact on existing features.**

### Usage
- Use `<ResignationApplicationCustom />` in place of the old resignation form where no doctype is available or needed.
- The form will show employee details, validate the date, and save to Employee doc via the API.

### Rationale
- The previous approach using FormView required a doctype, which caused errors since no `Resignation Application` doctype exists.
- This new standalone form is modular, does not require a doctype, and is fully decoupled from the DocType system.

### Files Added
- `src/views/ResignationApplicationCustom.vue` (new custom form view)

### Files Unchanged
- No changes to existing forms, components, or features. 

## 2024-XX-XX: Main Resignation Form View Update

### What Changed
- The main resignation form view (`src/views/ResignationApplication.vue`) now imports and renders the new custom form component, fully replacing the old FormView-based implementation.
- This change is modular and does not affect any other features or forms. 

## 2024-XX-XX: Employee Resignation DocType Implementation

### What Changed
- **Backend:** Updated `apps/hrms/hrms/api/resignation.py` to work with Employee Resignation DocType
- **Frontend:** Updated `src/views/ResignationApplication.vue` to use Employee Resignation DocType
- **New API Endpoints:**
  - `get_employee_resignations(employee_id)` - Get existing resignation documents
  - `create_resignation(employee_id, resignation_submission_date, last_working_date, reason_for_resignation)` - Create new resignation doc
  - `submit_resignation(doc_name)` - Submit resignation document

### Frontend Logic
- **Check for existing resignations:** On page load, checks if employee has previous resignation documents
- **Show list if exists:** Displays existing resignations with status (Draft/Submitted) and details
- **Create new option:** Button to create additional resignation if previous ones exist
- **Form fields:** All Employee Resignation DocType fields (Employee, Resignation Submission Date, Last Working Date, Reason for Resignation)
- **Validation:** Resignation submission date must be at least 30 days from today

### Backend Changes
- **DocType:** Uses Employee Resignation DocType instead of updating Employee directly
- **Document creation:** Creates new Employee Resignation documents
- **Document submission:** Supports submitting resignation documents
- **Query existing:** Fetches all resignation documents for an employee

### Files Modified
- `apps/hrms/hrms/api/resignation.py` - Updated API endpoints
- `src/views/ResignationApplication.vue` - Updated to use Employee Resignation DocType
- `frontend/docs/resignation-feature.md` - Updated documentation

### Files Unchanged
- No changes to existing forms, components, or other features 

## 2024-XX-XX: Standard HRMS Pattern Implementation

### What Changed
- **Form:** Updated `src/views/ResignationApplication.vue` to follow the same pattern as `AttendanceRequestForm.vue`
- **List:** Created `src/views/ResignationApplicationList.vue` following `AttendanceRequestList.vue` pattern
- **Backend:** Removed custom API endpoints, now uses standard HRMS form field API

### Implementation Details
- **Form Pattern:** Uses `createResource` to fetch form fields from backend API (`hrms.api.get_doctype_fields`)
- **FormView:** Uses standard `FormView` component with Employee Resignation doctype
- **ListView:** Uses standard `ListView` component for resignation history
- **Validation:** Custom validation for resignation submission date (minimum 30 days)
- **Field Filtering:** Automatically filters out system fields (employee, employee_name, status, company) for new documents

### Files Added/Modified
- `src/views/ResignationApplication.vue` - Updated to follow standard HRMS form pattern
- `src/views/ResignationApplicationList.vue` - New list view for resignation history
- `frontend/docs/resignation-feature.md` - Updated documentation

### Standard Features
- **Form:** Create and edit resignation documents
- **List:** View resignation history with filters
- **Validation:** Date validation and form field validation
- **Permissions:** Standard HRMS permission system
- **Workflow:** Submit/cancel documents

### Files Unchanged
- No changes to existing forms, components, or other features
- Uses standard HRMS patterns and components 

## 2024-XX-XX: Resignation Dashboard, List, and Modal Pattern

### What Changed
- **Dashboard:** Added `ResignationDashboard.vue` for listing recent resignation requests and a button to request new resignation (like attendance dashboard)
- **List:** Updated `ResignationApplicationList.vue` to use ListView and match attendance request list
- **Form/Modal:** Updated `ResignationApplication.vue` to be used as a modal for details, following attendance modal pattern
- **Routing:** Now supports navigation between dashboard, list, and modal form

### Implementation Details
- **Dashboard:** Uses `RequestList`, router-link, and a button for navigation
- **List:** Uses `ListView` with Employee Resignation doctype, proper fields, and filter config
- **Form/Modal:** Uses `FormView` in a modal, is submittable, and matches HRMS modal style
- **Consistent:** Follows the exact same pattern as attendance and leave requests

### Files Added/Modified
- `src/views/ResignationDashboard.vue` - New dashboard for resignation requests
- `src/views/ResignationApplicationList.vue` - Updated list view
- `src/views/ResignationApplication.vue` - Updated modal form view
- `frontend/docs/resignation-feature.md` - Updated documentation

### Files Unchanged
- No changes to existing forms, components, or other features
- All changes are modular and follow HRMS standards 