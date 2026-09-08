# QA Test Case & Bug Tracking Management System

A small, college-level QA portfolio project built with Python and Django. It simulates a basic QA workflow where testers can manage projects, create test cases, execute tests, record results, and track bugs.

## Why This Project

This project was designed as a realistic QA Intern portfolio project rather than a large enterprise application.

The main focus is on practical software testing and QA concepts:

- Test case creation and management
- Test execution and result tracking
- Bug reporting and tracking
- Basic search and filtering
- Simple testing metrics
- User authentication
- Django automated testing

## Features

### Authentication

- Login and logout
- Protected QA pages using Django authentication
- Custom login page

### Projects

- Add projects
- View projects
- Edit projects
- Delete projects

### Test Cases

- Create test cases and associate them with projects
- Define test steps and expected results
- Record actual results
- Mark tests as **Not Tested**, **Pass**, or **Fail**
- Execute a test case and record the execution timestamp
- Search test cases by title
- Filter test cases by status
- Edit and delete test cases

### Bug Tracking

- Create, edit, and delete bugs
- Associate bugs with projects
- Optionally link bugs to test cases
- Set severity: Low, Medium, High, Critical
- Set priority: Low, Medium, High
- Track status: Open, In Progress, Fixed, Closed
- Search bugs by title
- Filter bugs by status, severity, and priority

### Dashboard

The dashboard provides simple testing metrics including:

- Total projects
- Total test cases
- Passed tests
- Failed tests
- Not tested cases
- Executed tests
- Test coverage
- Total bugs
- Open bugs
- Fixed bugs
- Critical bugs

### Django Admin

The built-in Django Admin interface is customized with:

- List displays
- Search fields
- Filters
- Ordering

### Automated Tests

The project includes Django automated tests covering important application functionality such as:

- Authentication
- Page access
- Project CRUD operations
- Test case CRUD operations
- Bug CRUD operations
- Test execution
- Search functionality
- Filtering
- Dashboard behaviour

The complete test suite contains **38 automated tests**, all of which pass successfully.

## Technology Stack

- Python 3.13
- Django 5.2
- SQLite
- HTML
- CSS
- Django Authentication
- Django Admin
- Django Test Framework

## Project Structure

```text
QA_Bug_Tracker_Final/

├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── bugtracker/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── testing/
    ├── migrations/
    ├── templates/
    │   └── testing/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py