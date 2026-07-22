# Django Job Portal

A simple Job Portal REST API built using **Django** and **Django REST Framework**. This project allows basic management of jobs, users, and job applications.

## Features

- Create and manage job listings
- User model
- Job application model
- REST API endpoints
- Django Admin support
- SQLite database

## Tech Stack

- Python 3
- Django 6
- Django REST Framework
- SQLite
- Git & GitHub

## Project Structure

```
jobportal/
│
├── jobportal/          # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── jobs/               # Django application
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── manage.py
├── db.sqlite3
└── .gitignore
```

## Installation

### Clone the repository

```bash
git clone https://github.com/Sourav-jp/Day4.git
cd Day4
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install django djangorestframework
```

### Apply migrations

```bash
python manage.py migrate
```

### Run the development server

```bash
python manage.py runserver
```

The server will start at:

```
http://127.0.0.1:8000/
```

## API

The project provides REST API endpoints for managing jobs.

Example endpoint:

```
/jobs/
```

## Future Improvements

- User Authentication
- JWT Authentication
- Search and Filtering
- Pagination
- Company Profiles
- Resume Upload
- Email Notifications

## Author

**Sourav J. Prakash**

GitHub: https://github.com/Sourav-jp

---

This project was created as part of Django learning and practice.
