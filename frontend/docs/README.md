# HRMS Frontend Documentation

This folder contains documentation for features and changes made to the HRMS frontend application.

## Available Documentation

### [Resignation Feature](./resignation-feature.md)
- Implementation details for the resignation application feature
- Technical specifications and usage instructions
- Backend integration requirements
- **2024-XX-XX:** Now uses a custom backend API to save resignation details directly to the Employee DocType. No Resignation Application doctype is required. See documentation for details.

### [Asset Request Feature](./asset-request-feature.md)
- Implementation details for the asset request feature
- Complete employee asset request workflow
- Backend API integration and frontend components
- **2025-01-XX:** New feature allowing employees to request assets through the HRMS interface. Includes dashboard, form views, and list management.

## Documentation Standards

When adding new features or making significant changes to the HRMS frontend, please:

1. Create a new markdown file in this folder
2. Follow the existing documentation structure
3. Include:
   - Overview of the feature
   - Changes made
   - Technical implementation details
   - Usage instructions
   - Future enhancements (if applicable)

## File Naming Convention

- Use kebab-case for file names
- Include the feature name in the filename
- Example: `resignation-feature.md`, `attendance-tracking.md` 