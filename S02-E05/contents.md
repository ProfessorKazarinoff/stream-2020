# S02-05 Contents

## Who am I? Why am I doing this?

 > Blog: https://pythonforundergradengineers.com/

 > Book: https://www.amazon.com/Problem-Solving-Python-3-7-open-source/dp/1693405415

## Review where the GitHub Repo for the stream can be found

 > https://github.com/ProfessorKazarinoff/stream-2020

Code of conduct: https://github.com/ProfessorKazarinoff/stream-2020/blob/master/code-of-conduct/code_of_conduct.md


## What is MkDocs? What are static sites? Why MkDocs and no Sphinx?

 > https://www.mkdocs.org/

## Create a GitHub Repo on GitHub.com

Add a .gitignore file for Python and a LICENSE

## Pull Locally, Virtual Environment, Install MkDocs

```
mkdir mkdocs-github-pages
cd mkdocs-github-pages
git init
git remote add origin https://github.com/ProfessorKazarinoff/mkdocs-github-pages.git
git pull origin master
```
## Create a Virtual environment and install MkDocs

```
python -m venv venv
source venv/bin/activate
python -m pip install mkdocs mkdocs-material
```

## A simple MkDocs site, run locally

```
mkdocs new .
mkdocs build
mkdocs serve
```

## Apply the MkDocs Material theme

After mkdocs-material is pip installed, add the theme name to mkdocs.yml

## Deploy to GitHub Pages

```
mkdocs gh-deploy
```

## GitHub Actions to deploy to GitHub Pages

Create a .github/workflows/ci.yml file

## Add, commit and push. Watch the site change

```
git add .
git commit -m "added page to Mkdocs site"
git push origin master
```

## Conclusion

That's all for today. Next week we'll explore a different Python web technology.
