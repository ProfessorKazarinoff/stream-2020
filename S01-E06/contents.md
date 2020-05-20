# S01-E05 Contents

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

 - Created files for security
 - Installed and configured Nginx

Note: Check https://ssl-config.mozilla.org/#server=nginx&version=1.17.7&config=intermediate&openssl=1.1.1d&guideline=5.4 to see how the nginx configuration compares

 - Ran JupyterHub as a System service

## Log into server, change prompt

```
PS1="\u@jhserver: \w\n$ "
```

## Google OAuth

 - GitHub app registration
 - Install package for GitHub OAuth (already installed when we did GitHub OAuth)
 - Customize JupyterHub config to use GitHub OAuth (domains has to be a list, not a string)

## Cull Idle Servers Script

## Save History, Shut down server

## Add files to git, commit and push

## Review and Preview Next Episode
