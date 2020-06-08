# S01-E08 Contents

## Digital Ocean, create a new droplet, link domain name to droplet

## Who am I? Why am I doing this?

 > Blog: https://pythonforundergradengineers.com/

 > Book: https://www.amazon.com/Problem-Solving-Python-3-7-open-source/dp/1693405415

## Review where the GitHub Repo for the stream can be found

 > https://github.com/ProfessorKazarinoff/stream-2020

Code of conduct: https://github.com/ProfessorKazarinoff/stream-2020/blob/master/code-of-conduct/code_of_conduct.md

## Review what JupyterHub is, the JupyterHub Docs, and the docs we are following in this series

 > https://jupyterhub.readthedocs.io/en/stable/

 > https://professorkazarinoff.github.io/jupyterhub-ENGR114-2019Q4/

## Review what we did last time

 - Put users and admin users names in a json file, auto load into JuyterHub config
 - Cutomize the login page

## What is Ansible?

## Add git submodule that contains the ansible playbooks

```
git submodule add https://username/reponame submodule/path
git submodule --init
git submodule update --init --recursive
```

## Installing Ansible

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Ensure server is created, ensure domain name is linked to server. https://whatsmydns.net

## Copy hosts and default.yml variable files

## Check server connection with ping

## Ansible Playbook to create a non-root sudo user, enable ufw and SSH

## Other Ansible Playbooks

 - install miniconda
 - install jupyterhub
 - SSL cert
 - Google OAuth

# Shut down servers, delete servers, save locally, push up to GitHub

# Wrap-up S01
