# RSTL Appointment Portal - Product Requirements Document (PRD)

## 1. Project Overview

### Purpose
Develop an efficient and organized appointment scheduling portal for RSTL, managing appointments for three laboratories: Metrology Lab, Specimens (Microbiology) Lab, and Chemistry Lab. The platform streamlines appointment booking, client and company registration, and administrative management tasks.

### Scope

**Included:**
- Appointment scheduling interfaces for Metrology, Specimens, and Chemistry labs.
- Administrative interfaces for managing client data, appointments, and reporting.
- Specific pipelines for user interactions per laboratory.

**Excluded:**
- User registration/authentication (no client userbase; data entry via public forms).
- Payment processing unless specified explicitly.

### Objectives
- Automate appointment scheduling and management processes.
- Ensure data integrity and efficient administrative oversight.
- Maintain laboratory-specific constraints and requirements.

### Audience & Stakeholders
- **Clients/Users:** Company managers and truck drivers for Metrology; general clients for Specimens and Chemistry labs.
- **Admins:** Laboratory staff managing appointments and client data.
- **Developers:** Technical teams maintaining the system.

---

## 2. Core Functionalities

### Metrology Lab Pipeline

**User Pipeline:**
- **Company Registration (Manager):**
  - Form requiring company details, business permit, ORCR, and license plate information.
  - Data validation for submitted documents.
  - Registration data initially marked as "pending verification."

- **Truck Appointment Scheduling (Driver):**
  - Form includes truck license plate verification against registered plates.
  - Input for liquid carried (liters).
  - Appointment scheduling constrained by:
    - Maximum daily capacity (80,000 liters).
    - Slot limits per day (admin configurable).
    - First-booked, first-served logic.

**Admin Pipeline:**
- Comprehensive dashboard including:
  - Company and truck registration management.
  - Interface for verifying and approving/rejecting manager-submitted company data.
  - Daily appointment view and editing.
  - Configurable constraints management (slots, daily liter capacity).

### Specimens (Microbiology) & Chemistry Lab Pipeline

**User Pipeline:**
- Clients fill out public web forms for appointment scheduling and sample submission.
- Form responses logged with timestamps and mapped to the database.

**Admin Pipeline:**
- Centralized admin dashboard displaying:
  - Form responses (searchable, sortable).
  - Data management with editable fields.
  - Mapped values and relationships across tables.
  - Comprehensive reporting and export functionality.

---

## 3. Implementation Notes

### Technical Stack

- **Front End**
  - Flask (web framework)
  - WTForms (form handling and validation)
  - Jinja2 (templating and dynamic HTML)
  - Bootstrap (styling)
  - JavaScript (interactivity) + DataTables.js (interactive, editable tables)

- **Back End**
  - Flask (core framework)
  - SQLAlchemy (ORM for database interactions)
  - PostgreSQL (database)
  - Flask Micromodules:
    - Flask-Migrate
    - Flask-Login
    - Flask-WTF
    - Flask-SQLAlchemy
  - Others:
    - Pandas (data manipulation)
    - ReportLab (PDF generation)
    - OpenPyXL (Excel exports)

- **AJAX & APIs**
  - Flask routes handling AJAX requests and responding with JSON
  - RESTful CRUD API endpoints

- **Deployment**
  - Docker
  - Gunicorn
  - Nginx

### Assumptions & Constraints
- No client login required; all interactions via public forms.
- Document uploads (ORCR, business permits) securely stored.
- Maximum daily capacities and appointment constraints strictly enforced.
- Compliance with standard web security practices (OWASP, GDPR).

### Risks & Dependencies
- High concurrency handling required for daily bookings.
- Document verification and management system dependencies.
- Email notifications (SMTP) required for appointment confirmations.

---

## 4. User Stories

### Metrology Lab

**Manager User Story:**
- "As a company manager, I want to register my company and trucks easily by uploading required documents, so that our fleet can seamlessly schedule appointments."
  - **Acceptance Criteria:**
    - Document validation (business permit, ORCR).
    - Successful registration confirmation upon admin verification.

**Truck Driver User Story:**
- "As a truck driver, I want to schedule an appointment after confirming truck registration and specifying liquid carried, to efficiently secure an appointment."
  - **Acceptance Criteria:**
    - License plate verification.
    - Daily capacity and slot validation.
    - Immediate scheduling confirmation upon successful booking.

### Specimens & Chemistry Labs

**Client User Story:**
- "As a client, I want to conveniently fill out forms for appointments and sample submission, receiving immediate confirmation, so that my samples can be processed without delay."
  - **Acceptance Criteria:**
    - Accurate data logging and timestamp recording.
    - Email confirmation of appointment submission.

### Admin User Stories (All Labs)

- "As an admin, I need comprehensive dashboards to manage, view, verify, and edit appointments, registrations, and configurations efficiently."
  - **Acceptance Criteria:**
    - Interactive data management (view/edit via AJAX and DataTables).
    - Clear mapping and relationship management between tables.
    - Interface for verification of company registration data.

- "As an admin, I want comprehensive report generation capabilities, so I can analyze and export appointment data accurately."
  - **Acceptance Criteria:**
    - Reporting interfaces supporting filtering, sorting, and export to CSV/PDF formats.

## 5. Project Structure
```
rstl-appointment-portal/
│
├── 📂 app/
│   ├── 📂 static/
│   │   ├── 📂 css/
│   │   │   └── styles.css
│   │   └── 📂 js/
│   │       ├── scripts.js
│   │       └── datatables-init.js
│   │
│   ├── 📂 templates/
│   │   ├── 📂 metrology/
│   │   │   ├── register_company.html
│   │   │   └── schedule_appointment.html
│   │   ├── 📂 specimens/
│   │   │   └── schedule_appointment.html
│   │   ├── 📂 chemistry/
│   │   │   └── schedule_appointment.html
│   │   ├── 📂 admin/
│   │   │   ├── dashboard.html
│   │   │   └── verify_company.html
│   │   └── base.html
│   │
│   ├── 📂 routes/
│   │   ├── __init__.py
│   │   ├── metrology.py
│   │   ├── specimens.py
│   │   ├── chemistry.py
│   │   └── admin.py
│   │
│   ├── 📂 models/
│   │   ├── __init__.py
│   │   └── models.py
│   │
│   ├── 📂 forms/
│   │   └── forms.py
│   │
│   ├── 📂 api/
│   │   ├── __init__.py
│   │   └── endpoints.py
│   │
│   ├── 📂 utils/
│   │   ├── reports.py
│   │   └── validators.py
│   │
│   ├── config.py
│   └── __init__.py
│
├── 📂 migrations/ (Flask-Migrate files)
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── run.py
```