# Flask-apiservices
==============================

## Setting up development environment

The development environment can be setup either like a pythonista
with the usual python module setup, or like a docker user.

### The pythonista way

Ensure that you have an updated version of pip

```
pip --version
```
```
pip install -U pip
```

This will install latest pip

Ensure that you are in virtualenv
if not install virtual env
```
sudo pip install virtualenv
```
This will make install all dependencies to the virtualenv
not on your root

From the module folder install the dependencies. This also installs
the module itself in a very pythonic way.

```
pip install -r requirements.txt
```

# Requirements:
```
  Postgresql
```

# Environment variables
```
export DB_NAME="db_name"
export DB_PASSWORD="db_password"
export DB_USERNAME="db_username"
export DB_HOST="localhost"
export DEBUG = False
```

Before begining you need to migrate tables

Perform migration by
```
python manage.py db init
python manage.py db migrate

```
Run app by
```
python manage.py runserver
```

## Functionality

 Registration
 Login
 GetUser

 [Documentaion](https://documenter.getpostman.com/view/4141499/SWLk355Z?version=latest)
