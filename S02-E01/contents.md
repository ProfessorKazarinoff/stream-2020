# S02-E01 Contents

## Who am I? Why am I doing this?

 > Blog: https://pythonforundergradengineers.com/

 > Book: https://www.amazon.com/Problem-Solving-Python-3-7-open-source/dp/1693405415

## Review where the GitHub Repo for the stream can be found

 > https://github.com/ProfessorKazarinoff/stream-2020

Code of conduct: https://github.com/ProfessorKazarinoff/stream-2020/blob/master/code-of-conduct/code_of_conduct.md

## Voila Overview

Voila Docs: https://voila.readthedocs.io/en/stable/

Voila Deployment Docs: https://voila.readthedocs.io/en/stable/deploy.html

## GitHub Repo for a Simple Voila App

 > https://github.com/ProfessorKazarinoff/voila-app

## Run notebook and Voila Locally

Run the Jupyter notebook locally

```
jupyter notebook
```

Run voila locally

```
voila app.ipynb
```

## Heroku Account

Create a new account on Heroku: https://signup.heroku.com

## Heroku CLI install

Install the Heroku Command Line Interface (CLI): https://devcenter.heroku.com/articles/heroku-cli#download-and-install

Once installed, confirm the installation and login

```
heroku --version
heroku login
```

## Run Volia on Heroku

Create requirements.txt file, runtime.txt file and Procfile. Make sure the name of the notebook is in the Procfile. Make sure the dashes are regular dashes in the Procfile. Use Python 3.7.8 in runtime.txt

```
git add .
git commit -m "ready to run on Heroku"
git push origin master
heroku create
git push heroku master
heroku open
```

## See if we can solve a problem on stack overflow

Fork the repo, create a new local directory and link to the forked repo. Pull the repo down from GitHub

Create a virtual environment locally. pip install the packages listed in requirements.txt. Then save a new requirements.txt file that contains all of the packages that were installed with pip.

Add to the .gitignore file to make sure that the virtual environment and .ipynb-checkpoint files are ignored by git.

## Conclusion

That's all for today. Next week we'll explore a different Python web technology.
