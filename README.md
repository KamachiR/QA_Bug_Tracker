# QA Test Case & Bug Tracking Management System

A small Django-based QA portfolio project for managing test cases, test execution, and software bugs.

## Why This Project?

This project demonstrates basic software testing and QA workflow concepts through a simple web application.

It was developed as a college-level portfolio project to practice:

- Test case management
- Test execution
- Bug reporting and tracking
- Search and filtering
- Basic dashboard reporting
- Automated testing using Django

## Features

### Authentication

- User login and logout
- Protected application pages
- Django authentication system

### Project Management

- Create projects
- View projects
- Edit projects
- Delete projects

### Test Case Management

- Create test cases
- Assign test cases to projects
- Add test steps
- Add expected results
- Edit and delete test cases
- Search test cases
- Filter test cases by status

### Test Execution

- Execute test cases
- Record actual results
- Mark test cases as:
  - Not Tested
  - Pass
  - Fail
- Store execution date and time

### Bug Tracking

- Create bugs
- Link bugs to projects
- Optionally link bugs to test cases
- Set severity
- Set priority
- Track bug status
- Edit and delete bugs
- Search bugs
- Filter bugs by status, severity, and priority

### Dashboard

The dashboard provides a simple summary of:

- Total projects
- Total test cases
- Passed test cases
- Failed test cases
- Not tested test cases
- Executed test cases
- Test execution coverage
- Total bugs
- Open bugs
- Fixed bugs
- Critical bugs

### Django Admin

The project includes a customized Django Admin interface for managing:

- Projects
- Test cases
- Bugs

### Automated Tests

The project includes Django automated tests covering important application functionality.

The current test suite contains **38 automated tests**.

## Technology Stack

- **Python 3.13**
- **Django 5.2**
- **SQLite**
- **HTML**
- **CSS**
- **Django Authentication**
- **Django Admin**
- **Django Test Framework**

## Project Structure

```text
QA_Bug_Tracker/
│
├── manage.py
├── README.md
├── requirements.txt
├── .gitignore
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
    │       ├── login.html
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
    │       └── delete_bug.html
    │
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    └── tests.py