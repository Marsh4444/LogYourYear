# LogYourYear

LogYourYear is a Django web app that helps users track learning topics and log entries as they learn throughout the year.

## Features
- User authentication (login/logout)
- Topic and entry management
- Global navigation
- Bootstrap-styled UI

## Tech Stack
- Django
- Python
- Bootstrap
- SQLite (local) / Postgres (production)
- Heroku

## Local Setup

```bash
git clone https://github.com/your-username/logyouryear.git
cd logyouryear
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Visit: http://127.0.0.1:8000/

Authentication

Django built-in auth is used

Login template path:
users/templates/registration/login.html

Logout uses POST (no logout page)

Deployment (Heroku)
heroku create logyouryear
git push heroku main
heroku run python manage.py migrate

Author

Holyfield Nwadike