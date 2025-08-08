# Asset Request Feature Implementation

## Overview

This document describes the implementation of the Asset Request feature in the HRMS frontend application. The feature allows employees to request assets through a user-friendly interface, following the same pattern as the existing resignation request feature.

## Feature Components

### 1. Backend API (`apps/hrms/hrms/api/asset_request.py`)

**Purpose**: Provides the backend API endpoints for asset request functionality.

**Key Functions**:
- `get_asset_requests()`: Retrieves asset requests for a specific employee
- Supports filtering by approval status
- Includes workflow state field support
- Returns formatted data for frontend consumption

**Parameters**:
- `employee`: Employee ID to filter requests
- `for_approval`: Boolean to filter requests for approval
- `limit`: Maximum number of records to return

### 2. Frontend Data Layer (`apps/hrms/frontend/src/data/asset_request.js`)

**Purpose**: Manages asset request data on the frontend.

**Key Features**:
- Uses Frappe UI's `createResource` for data management
- Automatic caching with key `hrms:my_asset_requests`
- Transforms data to include doctype information
- Integrates with employee resource for current user

### 3. Configuration (`apps/hrms/frontend/src/data/config/requestSummaryFields.js`)

**Purpose**: Defines the fields to display in asset request summaries.

**Added Fields**:
- `ASSET_REQUEST_FIELDS`: Array of field configurations for asset requests
- Includes all relevant fields from the Asset Request doctype
- Supports proper field type formatting

### 4. UI Components

#### AssetRequestItem.vue
**Purpose**: Displays individual asset request items in lists.

**Features**:
- Shows requested item name or asset item
- Displays request date and truncated reason
- Status badges with color coding
- Consistent styling with other request items

#### AssetRequestDashboard.vue
**Purpose**: Main dashboard for asset request management.

**Features**:
- "Request Asset" button for creating new requests
- Recent requests list (limited to 5 items)
- Modal support for viewing request details
- Edit functionality for draft requests

#### AssetRequestApplication.vue
**Purpose**: Form view for creating and editing asset requests.

**Features**:
- Dynamic form field loading
- Employee auto-population
- Read-only mode for non-owner requests
- Form validation support

#### AssetRequestApplicationList.vue
**Purpose**: List view for viewing all asset request history.

**Features**:
- Filterable list view
- Configurable fields display
- Search and filter capabilities

### 5. Router Integration (`apps/hrms/frontend/src/router/index.js`)

**Added Routes**:
- `/asset-request-dashboard`: Main dashboard
- `/asset-request-list`: History list view
- `/asset-request-form/:id?`: Form view (create/edit)
- `/asset-request/:id?`: Detail view

### 6. Profile Integration (`apps/hrms/frontend/src/views/Profile.vue`)

**Changes**:
- Added "Asset Request" option to profile links
- Integrated with existing navigation system
- Consistent styling with other profile options

## Implementation Details

### Data Flow

1. **User clicks "Asset Request" in Profile**
   - Navigates to AssetRequestDashboard
   - Loads recent asset requests via `myAssetRequests` resource

2. **Creating New Request**
   - User clicks "Request Asset" button
   - Navigates to AssetRequestApplication form
   - Form loads with employee pre-populated
   - User fills required fields and submits

3. **Viewing Request Details**
   - User clicks on request item in list
   - Opens RequestActionSheet modal
   - Shows all request details with action buttons

4. **Editing Requests**
   - Available for draft requests only
   - Opens form view with existing data
   - Maintains data integrity

### Field Mapping

The asset request feature uses the following fields from the Asset Request doctype:

- `name`: Request ID
- `employee`: Employee making the request
- `request_date`: Date of request (auto-populated)
- `requested_item_name`: Custom item name
- `reason_for_request`: Detailed reason
- `docstatus`: Request status (Draft/Submitted)

**Note**: The `asset_item` field is managed from the desk and is not available in the frontend form.

### Status Management

The feature supports multiple status types:
- **Draft**: Initial state, editable
- **Submitted**: Awaiting approval
- **Approved**: Request approved
- **Rejected**: Request rejected
- **Workflow States**: Custom workflow states if configured

### Security Considerations

- Employee can only view their own requests
- Form validation ensures data integrity
- Read-only mode for non-owner requests
- Proper permission checks in backend API

## Usage Instructions

### For Employees

1. **Access Asset Requests**:
   - Go to Profile page
   - Click on "Asset Request" option
   - View dashboard with recent requests

2. **Create New Request**:
   - Click "Request Asset" button
   - Fill in required fields:
     - Requested Item Name
     - Reason for Request
   - Submit the request

3. **View Request History**:
   - Click "View List" to see all requests
   - Filter and search through requests
   - Click on any request to view details

4. **Edit Requests**:
   - Only draft requests can be edited
   - Click on draft request to open edit form
   - Make changes and resubmit

### For Administrators

1. **Monitor Requests**:
   - Use backend API to retrieve all requests
   - Filter by employee, status, or date
   - Process approvals through existing workflow

2. **Configuration**:
   - Asset Request doctype is submittable
   - Supports workflow states
   - Configurable permissions

## Technical Notes

### Dependencies
- Frappe UI components
- Ionic Vue for mobile interface
- Existing HRMS infrastructure

### Browser Compatibility
- Modern browsers with ES6+ support
- Mobile-responsive design
- Progressive Web App features

### Performance Considerations
- Lazy loading of components
- Efficient data caching
- Minimal API calls

## Future Enhancements

1. **Advanced Filtering**: Add more filter options in list view
2. **Bulk Operations**: Support for bulk request creation
3. **Notifications**: Real-time notifications for status changes
4. **Attachments**: Support for file attachments in requests
5. **Approval Workflow**: Enhanced approval process with multiple levels

## Testing

### Manual Testing Checklist

- [ ] Profile navigation to Asset Request
- [ ] Creating new asset request
- [ ] Viewing request details in modal
- [ ] Editing draft requests
- [ ] List view with filters
- [ ] Form validation
- [ ] Status updates
- [ ] Mobile responsiveness

### Automated Testing

- Unit tests for API functions
- Component testing for Vue components
- Integration tests for data flow
- E2E tests for complete user journeys

## Maintenance

### Regular Tasks
- Monitor API performance
- Update field configurations as needed
- Review and update permissions
- Test with new Frappe versions

### Troubleshooting
- Check browser console for errors
- Verify API endpoint availability
- Confirm doctype field configurations
- Validate user permissions

## Conclusion

The Asset Request feature provides a complete solution for employees to request assets through the HRMS application. The implementation follows established patterns and maintains consistency with existing features while providing a user-friendly interface for asset management. 