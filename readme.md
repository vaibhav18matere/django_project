```
python3 -m venv .venv
source .venv/bin/activate
pip install uv
```
... Now add uv at start of installing anything
```
uv pip install Django 
django-admin startproject myproject
cd myproject
python manage.py runserver
```

- Templates
- Jinja
- Django apps
- Migrate
- Admin Panel

- Django Relationship Models
1. One to One
2. Many to Many
3. Many to One

- Cascade?

- Cascade on Delete: When you delete a record from a parent table, this action also deletes related records in child tables.
- Cascade on Update: When you update a record in a parent table, this update also applies to related records in child tables.