Healthcare Management API
```
Project Description: A Django REST Framework-based healthcare management system with JWT authentication, allowing secure management of patients, doctors, and patient-doctor mappings using PostgreSQL.
```
Features
```
User authentication with JWT tokens.

CRUD operations for Patients and Doctors.

Assign doctors to patients and retrieve mappings.

Secure endpoints with permission checks.

PostgreSQL database integration.

Environment variables for sensitive data.
```
Tech Stack
```
Backend: Django 6.x, Django REST Framework

Authentication: JWT via djangorestframework-simplejwt

Database: PostgreSQL

Environment management: python-decouple
```
Setup Instructions

Clone the repository:
```
git clone https://github.com/keertiG-1296/Healthcare.git
cd healthcare
```
Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
Install dependencies:
```
pip install -r requirements.txt
```
Create a .env file in the project root with:
```
SECRET_KEY=<your_secret_key>
DB_NAME=<your_db_name>
DB_USER=<your_db_user>
DB_PASSWORD=<your_db_password>
DB_HOST=<your_db_host>
DB_PORT=<your_db_port>
```
Apply migrations:
```
python manage.py makemigrations
python manage.py migrate
```
Run the development server:
```
python manage.py runserver
```
Test API endpoints using Postman or any API client.
