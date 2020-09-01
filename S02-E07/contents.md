# S02-07 Contents

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

## Run Django

```
python manage.py runserver
# Ctrl-c to cancel
```

## Create A Courses Model

 - Model
 - Admin
 - View
 - url
 - template

## Create a custom user model

 - Model

## Migrate

```
python manage.py makemigrations
python manage.py migrate
```

## Add some data to the database using the Django Admin

## Stash the data from the database for use later

 > https://docs.djangoproject.com/en/3.1/howto/initial-data/

## Add, commit and push. Watch the site change

```
git add .
git commit -m "end of stream"
git push origin master
```

## Conclusion

That's all for today. Next week we'll explore how to deploy the Django Web App on Digital Ocean.
