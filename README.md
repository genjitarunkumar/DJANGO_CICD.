# Django REST Application

A clean, modern Django REST Framework (DRF) application setup.

## Project Structure
- `core/`: Project configuration (settings, urls, wsgi).
- `app/`: Main application logic (views, urls, models).
- `manage.py`: Django administrative tasks.

## Setup & Running
1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```
3. **Start Server**:
   ```bash
   python manage.py runserver
   ```

## API Endpoints
- **Root**: `http://127.0.0.1:8000/` (Redirects to Hello)
- **Hello World**: `http://127.0.0.1:8000/app/hello/`
- **Admin**: `http://127.0.0.1:8000/admin/`
