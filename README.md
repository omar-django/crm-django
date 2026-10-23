# CRM — Customer Records Manager

A Django-based Customer Relationship Management (CRM) application that allows users to manage customer records in a private workspace. Each user can access and manage only their own customer data.

## Features

- **User Authentication:** User registration, login, and logout using Django session authentication.
- **Private User Workspaces:** Enforces per-user data isolation to prevent unauthorized access to other users' customer records.
- **Customer Management (CRUD):** Create, view, update, and delete customer records.
- **Customer Search:** Search customer records efficiently.
- **Customer Status Tracking:** Track customers through four statuses: `New`, `Contacted`, `Won`, and `Lost`.
- **Customer Information:** Store customer names, email addresses, phone numbers, and notes.
- **Egyptian Phone Number Validation:** Validates Egyptian mobile phone numbers.
- **Secure Deletion:** Uses POST-only deletion with CSRF protection.
- **Automated Testing:** Includes 11 tests covering access control and form validation.

## Tech Stack

- **Language:** Python
- **Framework:** Django
- **Database:** PostgreSQL
- **Forms:** django-crispy-forms with Bootstrap 4
- **Environment Configuration:** django-environ
- **Authentication:** Django session authentication

## Screenshots

### Dashboard

View and manage customer records from the dashboard.

![CRM Dashboard](https://github.com/omar-django/crm-django/raw/main/screenshots/dashboard.png)

### Customer Record Details

View detailed information about an individual customer.

![Customer Record Details](https://github.com/omar-django/crm-django/raw/main/screenshots/view-record.png)

## Getting Started

Follow these steps to run the project locally.

### Prerequisites

- Python installed
- PostgreSQL installed and running
- Git installed

### 1. Clone the Repository

```bash
git clone https://github.com/omar-django/crm-django.git
cd crm-django
```

### 2. Create and Activate a Virtual Environment

On Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy `.env.example` to `.env` and update the values according to your local environment.

Configure the required settings, including:

- `SECRET_KEY`
- Database name
- Database username
- Database password
- Database host and port, if required

**Important:** Keep your `.env` file private. Never commit secret keys or database credentials to GitHub.

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create an Administrator Account

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open the following URL in your browser:

`http://127.0.0.1:8000/`

## Running Tests

Run the automated test suite with:

```bash
python manage.py test
```

The project includes 11 tests focused on access control and form validation.

## Security Considerations

- Customer records are restricted to their respective owners.
- Access control is enforced through the application's views.
- Customer deletion requires a POST request.
- CSRF protection is used for form submissions.
- Environment variables are used to configure sensitive settings.

## Project Goals

This project demonstrates practical backend development skills, including:

- Django application development
- Authentication and authorization
- User-specific data access control
- CRUD operations and search
- Form validation
- PostgreSQL integration
- Automated testing
- Basic web application security

## Future Improvements

Potential enhancements include:

- REST API integration using Django REST Framework
- Pagination for customer lists
- Advanced search and filtering
- Additional test coverage for customer creation, editing, and deletion

## Author

**Mohamed Omar**

GitHub: [@omar-django](https://github.com/omar-django)
