# S02-06 Contents

## Who am I? Why am I doing this?

 > Blog: https://pythonforundergradengineers.com/

 > Book: https://www.amazon.com/Problem-Solving-Python-3-7-open-source/dp/1693405415

## Review where the GitHub Repo for the stream can be found

 > https://github.com/ProfessorKazarinoff/stream-2020

Code of conduct: https://github.com/ProfessorKazarinoff/stream-2020/blob/master/code-of-conduct/code_of_conduct.md


## What is Django?

 > https://www.mkdocs.org/

## What are we trying to replicate and improve?

 > https://pcc.edu/engineering

## Create a GitHub Repo on GitHub.com

Add a .gitignore file for Python and a LICENSE

## Pull Locally, Virtual Environment, Install Djanog

```
mkdir college-transfer
cd college-transfer
git init
git remote add origin https://github.com/ProfessorKazarinoff/college-transfer.git
git pull origin master
python -m venv venv
source venv/bin/activate
python -m pip install django
python -m pip freeze > requirements.txt
```

## Run Django

```
python manage.py runserver
# Ctrl-c to cancel
```

## Create Pages App and a home page

 - create app
 - urls
 - views
 - templates

## Bootstrap

- Add bootstrap cdn
- Build out templates

## Add, commit and push. Watch the site change

```
git add .
git commit -m "added 3 pages"
git push origin master
```

## Conclusion

That's all for today. Next week we'll explore how to add a database instead of hard-coding the tables
