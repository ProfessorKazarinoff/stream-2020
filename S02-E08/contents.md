# S02-08 Contents

## Who am I? Why am I doing this?

 > Blog: https://pythonforundergradengineers.com/

 > Book: https://www.amazon.com/Problem-Solving-Python-3-7-open-source/dp/1693405415

## Review where the GitHub Repo for the stream can be found

 > https://github.com/ProfessorKazarinoff/stream-2020

Code of conduct: https://github.com/ProfessorKazarinoff/stream-2020/blob/master/code-of-conduct/code_of_conduct.md


## What is Django?

 > https://docs.djangoproject.com/en/3.1/

We'll sort of follow William Vincent's Django for Beginners Book:

 > https://djangoforbeginners.com/hello-world/

## What are we trying to replicate and improve?

 > https://www.pcc.edu/programs/engineering/course-plan/

 > https://www.pcc.edu/programs/engineering/course-plan/mechanical-engineering/

## Pull the project down from github

```
cd transfer-app
git pull origin master
source venv/bin/activate
```

## Run Migrate, load data and run the development server

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata courses/fixtures/database_data.json
python manage.py runserver
# Ctrl-c to cancel
```

## Add some data to the database using the Django Admin, See the site change

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

### Deploy with Heroku?

### Create a Digital Ocean Droplet

### Are we going to use Ansible?

### Follow Digital Ocean Tutorial

 > https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04

## Conclusion

That's the end of Season 2! Thanks for watching. I'm going to take some time off streaming and concentrate on book editing. I want to release the new edition of my book: Problem Solving with Python 3.8 Edition by Oct 1, 2020. 
