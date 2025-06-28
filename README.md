# 📊 Django Expense Tracker

A simple, user-friendly expense tracker built with Django and MySQL, featuring login/logout authentication and personal expense management.

## 🔐 Features
- User authentication (login/logout)
- Add, edit, delete expenses
- Categorize and filter by date
- Personal dashboards for each user
- View total and categorized expenses

## 🛠 Tech Stack
- Backend: Django (Python)
- Database: MySQL
- Frontend: HTML, CSS, JavaScript,  Bootstrap

## 🚀 Setup
```bash
git clone https://github.com/your-username/expense-tracker-django.git
cd expense-tracker-django
python -m venv env
env\Scripts\activate     # or source env/bin/activate
pip install -r requirements.txt

Update settings.py with your MySQL credentials:

python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

python manage.py migrate
python manage.py runserver
Visit: http://127.0.0.1:8000
