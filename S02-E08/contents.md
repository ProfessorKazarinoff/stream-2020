# S02-08 Contents

## Who am I? Why am I doing this?

 > Blog: https://pythonforundergradengineers.com/

 > Book: https://www.amazon.com/Problem-Solving-Python-3-7-open-source/dp/1693405415

## Review where the GitHub Repo for the stream can be found

 > https://github.com/ProfessorKazarinoff/stream-2020

Code of conduct: https://github.com/ProfessorKazarinoff/stream-2020/blob/master/code-of-conduct/code_of_conduct.md

## What are we trying to replicate and improve?

 > https://www.pcc.edu/programs/engineering/course-plan/

 > https://www.pcc.edu/programs/engineering/course-plan/mechanical-engineering/

## Pull the project down from GitHub

```
cd transfer-app
git pull origin master
source venv/bin/activate
```

## Run Migrate, load data and run the development server

```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata courses/fixtures/database_data.json
python manage.py runserver
# Ctrl-c to cancel
```

## Mess around with link color and links in the Majors pages and course listing pages

## Stash the data from the database for use later

```
python manage.py dumpdata courses > courses/fixtures/database_data.json
```

## Add, commit and push.

```
git add .
git commit -m "ready for production"
git push origin master
```

## Deployment Time!

### Deploy with Heroku

#### Docs

 > https://devcenter.heroku.com/articles/deploying-python

 > https://devcenter.heroku.com/categories/working-with-django

#### Extra Files

runtime.txt with ```python-3.8.5```

Procfile with ```web: gunicorn myproject.wsgi```

#### Install Packages

install gunicorn, django-heroku, whitenoise and add to requirements.txt ```pip install gunicorn django-heroku whitenoise``` and ```pip freeze > requirements.txt```

#### Django_heroku Package

Modify settings.py with ```import django_heroku``` at top and ```django_heroku.settings(locals())``` at the bottom

#### Static Files Setup

 > https://devcenter.heroku.com/articles/django-assets

Static file setup. In settings.py

```
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
```

#### Add, commit, push

#### Log into Heroku CLI

#### Create and run Heroku app

### Digital Ocean Deployment?

 > https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04

## Conclusion

That's the end of Season 2! Thanks for watching. I'm going to take some time off streaming and concentrate on book editing. I want to release the new edition of my book: Problem Solving with Python 3.8 Edition by Oct 1, 2020. 
