# Employee Certificate Request Feature

## Overview

The Employee Certificate Request feature allows employees to request various types of certificates through the HRMS mobile application. This feature follows the same pattern as the Leave Resumption feature but without approval workflow, as certificates are typically informational documents.

## Features

### 1. Profile Integration
- Added "Employee Certificate" option in the Profile section
- Uses award icon to represent certificate requests
- Positioned between Leave Resumption and Resignation Application

### 2. Dashboard View
- **EmployeeCertificateDashboard.vue**: Main dashboard showing recent requests and create new request button
- Displays up to 5 recent certificate requests
- "View List" button to see all historical requests
- Modal view for request details

### 3. Request Management
- **EmployeeCertificateApplication.vue**: Form for creating/editing certificate requests
- **EmployeeCertificateApplicationList.vue**: List view of all certificate requests with filtering
- Support for draft and submitted states
- Form validation and employee auto-assignment

### 4. Request Display
- **EmployeeCertificateItem.vue**: Component for displaying certificate requests in lists
- Shows purpose, certificate date, and reason
- Status badges (Draft/Submitted)
- Consistent styling with other request types

## Technical Implementation

### Backend API
- **employee_certificate.py**: API endpoint for fetching certificate requests
- Supports filtering by employee and limit parameters
- Returns standardized request format for frontend compatibility

### Frontend Data Layer
- **employee_certificate.js**: Data resource for certificate requests
- Caches requests for performance
- Transforms data to include doctype information

### Configuration
- **requestSummaryFields.js**: Added EMPLOYEE_CERTIFICATE_FIELDS configuration
- Defines fields to display in request summary modals
- Includes: ID, Employee, Purpose, Reason, Certificate Date, Status

### Routing
- Added routes for dashboard, list, form, and detail views
- Consistent naming convention with other features
- Proper route parameter handling

## File Structure

```
frontend/src/
├── components/
│   └── EmployeeCertificateItem.vue
├── views/
│   ├── EmployeeCertificateDashboard.vue
│   ├── EmployeeCertificateApplication.vue
│   └── EmployeeCertificateApplicationList.vue
├── data/
│   └── employee_certificate.js
└── data/config/
    └── requestSummaryFields.js (updated)

hrms/api/
└── employee_certificate.py
```

## Usage Flow

1. **Access**: User clicks "Employee Certificate" in Profile section
2. **Dashboard**: Shows recent requests and "Request Employee Certificate" button
3. **Create**: Click button to open form for new certificate request
4. **Edit**: Click on existing request to view/edit details
5. **List**: View all historical requests with filtering options
6. **Submit**: Form validation and submission to backend

## Key Differences from Leave Resumption

- **No Approval Workflow**: Certificates are informational, no approval process
- **Different Fields**: Uses purpose, reason, certificate_date instead of join_date, comment
- **Icon**: Uses "award" icon instead of "corner-up-right"
- **Purpose Field**: Links to Employee Certificate Purpose doctype

## Integration Points

- **Profile.vue**: Added certificate option in profile links
- **RequestList.vue**: Added mapping for Employee Certificate doctype
- **RequestActionSheet.vue**: Added routing for certificate form views
- **Router**: Added all necessary routes for certificate feature

## Future Enhancements

- Support for certificate templates
- PDF generation for approved certificates
- Email notifications for certificate completion
- Integration with document management system
