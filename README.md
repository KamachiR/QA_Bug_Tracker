# QA Test Case & Bug Tracking Management System

A small, college-level QA portfolio project built with Python and Django. It simulates the basic workflow a QA tester can use to manage projects, write test cases, execute tests, and track bugs.

## Why this project

This project was designed as a realistic QA Intern portfolio project rather than a large enterprise application. The focus is on practical QA concepts:

- Test case creation and management
- Test execution and result tracking
- Bug reporting and tracking
- Basic search and filtering
- Simple testing metrics
- Authentication
- Django automated tests

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
- Optionally link a bug to a test case
- Set severity: Low, Medium, High, Critical
- Set priority: Low, Medium, High
- Track status: Open, In Progress, Fixed, Closed
- Search bugs by title
- Filter by status, severity, and priority

### Dashboard
The dashboard shows simple testing metrics:

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
The built-in Django Admin is customized with:

- List displays
- Search fields
- Filters
- Ordering

### Automated Tests
The project includes Django tests covering authentication, page access, CRUD operations, test execution, searching, filtering, and dashboard behaviour.

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
QA_Bug_Tracker/
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
```

## How to Run Locally

### 1. Open a terminal in the project folder

```text
C:\Users\Kamachi R\QA_Bug_Tracker
```

### 2. Create and activate a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create an admin user

```bash
python manage.py createsuperuser
```

Follow the prompts to create the username and password.

### 6. Run the development server

```bash
python manage.py runserver
```

Open the local address shown by Django in your browser.

## Running Automated Tests

Run the complete test suite with:

```bash
python manage.py test
```

The project was previously verified with **38 passing Django tests**.

## Notes

- SQLite is used to keep the project simple and easy to run.
- `db.sqlite3` is ignored by Git so each developer can create their own local database.
- The development secret key can be supplied through the `DJANGO_SECRET_KEY` environment variable.
- This project intentionally does not include unnecessary enterprise features such as REST APIs, email notification systems, complex role management, file uploads, or advanced analytics.

## GitHub

Repository: `https://github.com/KamachiR/QA_Bug_Tracker`

## Portfolio / Interview Summary

A simple way to describe the project in an interview:

> "I built a Django-based QA Test Case and Bug Tracking System. It allows a tester to create projects, write and execute test cases, record Pass/Fail results, report and track bugs, and use basic search and filtering. I also added authentication, Django Admin customization, a dashboard with testing metrics, and automated tests for the main application functionality."

