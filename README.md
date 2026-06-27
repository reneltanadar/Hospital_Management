# Hospital Management System

## Project Overview

The Hospital Management System is a backend application developed using Django REST Framework and PostgreSQL. It allows doctors to manage their availability and patients to book appointments. The system prevents double booking using database transactions and sends email notifications through a Serverless email service. Google Calendar OAuth integration has also been implemented as part of the project.

---

## Features

* User Authentication (Doctor & Patient)
* Custom User Model with Roles
* Doctor Availability Management
* Appointment Booking
* Double Booking Prevention using `transaction.atomic()` and `select_for_update()`
* Serverless Email Notifications
* Google Calendar OAuth Integration
* PostgreSQL Database
* REST APIs using Django REST Framework

---

## Tech Stack

* Python 3.13
* Django
* Django REST Framework
* PostgreSQL
* Serverless Framework
* Gmail SMTP
* Google Calendar API
* Node.js
* AWS Lambda (Serverless Structure)
* Git & GitHub

---

## Project Structure

```text
hospital-management-system/
│
├── hms/
│   ├── accounts/
│   ├── bookings/
│   ├── calendar_service/
│   ├── config/
│   ├── doctors/
│   ├── patients/
│   ├── utils/
│   ├── manage.py
│   └── requirements.txt
│
├── email-service/
│   ├── handler.py
│   ├── serverless.yml
│   └── requirements.txt
│
├── README.md
└── .gitignore
```

---

## Setup & Run

### Clone Repository

```bash
git clone <repository-url>
cd hospital-management-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure PostgreSQL

Create a PostgreSQL database and update the following in `config/settings.py`:

* Database Name
* Username
* Password
* Host
* Port

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Django

```bash
python manage.py runserver
```

### Run Serverless Email Service

```bash
cd email-service

npm install

serverless offline
```

---

## API Endpoints

### Authentication

| Method | Endpoint   | Description   |
| ------ | ---------- | ------------- |
| POST   | `/signup/` | Register User |
| POST   | `/login/`  | Login         |

### Doctor

| Method | Endpoint                    | Description          |
| ------ | --------------------------- | -------------------- |
| POST   | `/doctors/availability/`    | Add Availability     |
| GET    | `/doctors/available-slots/` | View Available Slots |

### Booking

| Method | Endpoint          | Description      |
| ------ | ----------------- | ---------------- |
| POST   | `/bookings/book/` | Book Appointment |

### Google Calendar

| Method | Endpoint           | Description        |
| ------ | ------------------ | ------------------ |
| GET    | `/google/login/`   | Google OAuth Login |
| GET    | `/oauth2callback/` | OAuth Callback     |

---

## System Architecture

```
Patient / Doctor
        │
        ▼
Django REST API
        │
        ├──────────────► PostgreSQL
        │
        ├──────────────► Serverless Email Service
        │                      │
        │                      ▼
        │                 Gmail SMTP
        │
        └──────────────► Google Calendar API
```

---

## Design Decisions

* Implemented a custom User model to support multiple user roles.
* Used Django REST Framework for building RESTful APIs.
* PostgreSQL was selected as the relational database.
* Implemented database-level concurrency control using `transaction.atomic()` and `select_for_update()` to prevent double booking.
* Email notifications were implemented as a separate Serverless service to keep the application modular.
* Google Calendar integration was implemented using OAuth 2.0.

---

## Limitations

* Google Calendar integration currently requires OAuth authorization before creating events.
* Email service currently uses Gmail SMTP for development.
* Authentication is session-based for development and can be extended with JWT for production.
* Additional validation and security measures can be added for production deployment.

---

All generated code was reviewed, modified, tested, and integrated manually.

---

## Future Improvements

* JWT Authentication
* Docker Deployment
* AWS Deployment
* CI/CD Pipeline
* SMS Notifications
* Video Consultation Support
* Admin Dashboard
* Automated Appointment Reminders

---

## Author

**Renelta Nadar**
