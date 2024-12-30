# Django

This is the usage of django.

We are making a simple Polls app.

## Commands:
### Make a Directory
```
mkdir djangotutorial
```

### Make a Django project
```
django-admin startproject mysite djangotutorial
```

### Run the project
```
python manage.py runserver
```
### Make a new app
```
python manage.py startapp <app_name>
```
### Make the tables in database
```
python manage.py migrate
```
### After adding an app in settings.py (INSTALLED_APPS)
```
python manage.py makemigrations <app_name>
```

## Endpoints

/polls

/polls/test

