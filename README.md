# FlowTask — Django Todo App

A minimal Django Todo application with a glassmorphic, modern dark UI and PostgreSQL persistence.

## Features
- Add tasks with optional descriptions
- Mark tasks complete/incomplete
- Delete tasks
- Live totals for total, pending, and completed tasks
- SQLite database
- Responsive glassmorphism UI
- Django admin support

## PostgreSQL setup

Create the database and user in PostgreSQL, or use an existing PostgreSQL database. Django will create the application tables when migrations are run. Copy `.env.example` to `.env` and set your PostgreSQL credentials.

Example:

```sql
CREATE DATABASE todo_db;
```

The project uses Django’s PostgreSQL backend with Psycopg 3. Django officially supports PostgreSQL and recommends Psycopg 3 for current versions.

## Run locally

```bash
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

pip install -r requirements.txt
# Set the POSTGRES_* environment variables first
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Admin

```bash
python manage.py createsuperuser
```

Then open `/admin/`.
