#  Employee Management System (Django + DRF)

A RESTful web application built with Django and Django REST Framework to manage employees, their attendance, performance ratings, and departments. This project was developed as part of an internship challenge, focusing on API design, data modeling, authentication, and clean backend architecture.

---

##  Features

- CRUD operations for Employees, Departments, Attendance, and Performance
- Token-based Authentication using DRF's TokenAuth
- Pagination, Filtering, and Sorting on API endpoints
- API documentation via Swagger UI
- Seed script for populating the database with fake data using `Faker`
- Modular Django app structure with best practices


##  Tech Stack

- **Backend:** Python 3.x, Django 4.x, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** DRF TokenAuth
- **Tools:** Faker, drf-yasg (Swagger UI), django-filter


###  Configure environment variables

Copy the example `.env.example` file to `.env` and update with your PostgreSQL database credentials


