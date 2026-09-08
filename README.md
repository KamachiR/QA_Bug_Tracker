# QA Test Case & Bug Tracking Management System

A web-based QA management application built using Python and Django to manage software testing activities, test cases, and bugs.

## Project Overview

This project simulates a basic Quality Assurance management system where testers can:

- Manage software projects
- Create and manage test cases
- Execute test cases
- Track test results
- Report and manage bugs
- Filter and search test cases and bugs
- Monitor testing statistics through a dashboard
- Secure the application using user authentication

## Features

### Project Management
- Add new projects
- View all projects
- Edit project details
- Delete projects

### Test Case Management
- Create test cases
- Assign test cases to projects
- Define testing steps
- Define expected results
- Record actual results
- Track test status
- Execute test cases
- Record execution time
- Search test cases
- Filter test cases by status

### Bug Management
- Report bugs
- Link bugs to projects and test cases
- Set severity
- Set priority
- Track bug status
- Edit bugs
- Delete bugs
- Search bugs
- Filter bugs by status, severity and priority

### Dashboard
The dashboard provides an overview of:

- Total projects
- Total test cases
- Passed tests
- Failed tests
- Not tested cases
- Test coverage
- Total bugs
- Open bugs
- Fixed bugs
- Critical bugs

### Authentication
- User login
- Logout
- Protected QA management pages
- Django authentication system

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- Django Authentication
- Django Admin
- Automated Testing

## Database Models

The application contains three main models:

### Project
Stores project information such as:

- Project name
- Description
- Creation date

### TestCase
Stores:

- Project
- Test case title
- Test steps
- Expected result
- Actual result
- Status
- Execution time

### Bug
Stores:

- Project
- Related test case
- Bug title
- Description
- Severity
- Priority
- Status
- Creation date

## Project Structure

```text
QA_Bug_Tracker/
│
├── manage.py
│
├── bugtracker/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── testing/
    ├── migrations/
    ├── templates/
    │   └── testing/
    │       ├── home.html
    │       ├── projects.html
    │       ├── test_cases.html
    │       ├── bugs.html
    │       ├── add_project.html
    │       ├── edit_project.html
    │       ├── delete_project.html
    │       ├── add_test_case.html
    │       ├── edit_test_case.html
    │       ├── delete_test_case.html
    │       ├── execute_test_case.html
    │       ├── add_bug.html
    │       ├── edit_bug.html
    │       ├── delete_bug.html
    │       └── login.html
    │
    ├── admin.py
    ├── models.py
    ├── views.py
    └── tests.py
