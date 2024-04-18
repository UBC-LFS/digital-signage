# Dairy Digital Signage

This project is a web-based digital signange app, running on Django and Apache with PostgreSQL. It is a fork of https://github.com/jbittel/django-signage and uses the BSD-3 License.

### Features
- Upload media to an online database.
- Display media in an automatically rotating slideshow format.
- Manage serveral displays at once, each able to show different slides.
- Set slides to enable and disable at certain times.
- Set slides weights so that they are displayed in a desired order. 

# Installation Guide

### Linux Container's Environment
- Ubuntu 22.04
- Python 3.10.12
- Django 5.0

### Install prerequisites for Ubuntu

#### 1. Install the latest stable version of Git first if it does not exist

```
# https://git-scm.com/download/linux
$ sudo apt install software-properties-common
$ sudo add-apt-repository ppa:git-core/ppa
$ sudo apt update
$ sudo apt install git
```

#### 2. Clone this repository

```
$ git clone https://github.com/UBC-LFS/digital-signage
```

#### 3. Install the python3 virtual environment and activate it

```
$ sudo apt update
$ sudo apt install python3-venv

$ python3 -m venv venv
$ source venv/bin/activate
```

#### 4. Install pip3

```
$ sudo apt update
$ sudo apt install python3-pip
$ pip3 install --upgrade pip
```

#### 5. Install requirements

```
$ cd digital-signage
$ pip3 install -r requirements.txt

# errors might occur in some packages, then install the following packages
$ sudo apt-get install python3-setuptools python3-dev libxml2-dev libxmlsec1-dev libxmlsec1-openssl
```


## Summary of Deployment
0. Rename *digital_signage/settings.py.example* to *digital_signage/settings.py*

1. Clone this Github repository
```
$ git clone https://github.com/UBC-LFS/digital-signage
```

2. Install requirement dependencies
```
$ pip install -r requirements.txt
```

3. Set Environment Variables in your machine:
```

ENGINE = os.environ["DAIRY_SIGNAGE_DB_ENGINE"]
NAME = os.environ["DAIRY_SIGNAGE_DB_NAME"]
USER = os.environ["DAIRY_SIGNAGE_DB_USERNAME"]
PASSWORD = os.environ["DAIRY_SIGNAGE_DB_PASSWORD"]
HOST = os.environ["DAIRY_SIGNAGE_DB_HOST"]
PORT = os.environ["DAIRY_SIGNAGE_DB_PORT"]

SECRET_KEY = os.environ["DAIRY_SIGNAGE_SECRET_KEY"]
```

4. Switch *DEBUG* to **False** in a *settings.py* file
```
DEBUG = False
LOCAL_LOGIN = False
```

5. Add a Media root directory to store certificate files
```
MEDIA_ROOT = 'your_media_root'
```

6. Add your allowed_hosts in *settings.py*
```
ALLOWED_HOSTS = ['YOUR_HOST']
```

7. Create staticfiles in your directory
```
$ python manage.py collectstatic --noinput

# References
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# https://devcenter.heroku.com/articles/django-assets
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment
```

8. Create a database in Postgresql

9. Create database tables, and migrate
```
$ python manage.py migrate
```

10. Load data for local testing
```
TBD
```

11. Update *settings.json* and *advanced_settings.json* files in the **saml** folder

12. See a deployment checklist and change your settings
```
$ python manage.py check --deploy


# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_SSL_REDIRECT = True
# X_FRAME_OPTIONS = 'DENY'
```

13. Now, it's good to go. Run this web application in your production!
```
$ python manage.py runserver
```

14. Timezone in settings.py
https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

```
# Choose the timezone where you live
TIME_ZONE = 'America/Vancouver'
```

15. Test
```
TBD
```

## Login locally
1. Create a superuser
```
# Reference: https://docs.djangoproject.com/en/2.2/topics/auth/default/
$ python manage.py createsuperuser --username=joe --email=joe@example.com
```

2. Run this app
```
$ python manage.py runserver

For scheduling tasks
$ python manage.py runserver --noreload

```


3. If you would like to log in through the local login, please change **LOCAL_LOGIN** to **True** in settings.py.
```
LOCAL_LOGIN=True
```
Open a new window with an URL ``` http://localhost:8000/accounts/local_login/ ```


**Upgrade Django**
```
pip install --upgrade django==new_version (e.g., 2.2.19)
```

Happy coding!
Thank you.