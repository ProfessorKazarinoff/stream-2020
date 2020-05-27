# S01-E06 Contents

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

 - GitHub OAuth
 - Can log in with GitHub usernames and passwords

## Log into server, change prompt

```
PS1="\u@jhserver: \w\n$ "
```

## Google OAuth

 - Google Developer Console
 - Google OAuth credentials in json
 - Modify ```jupyterhub_config.py```
 - Log in with Google username and password

## Cull Idle Servers Script

The cull_idle_servers.py script shuts down user's servers when they have not used JupyterHub in a while. This opens up computational resources for other users that are actively using JupyterHub.

 - copy the ```cull_idle_servers.py``` script to ```/etc/jupyterhub/```
 - add a little configuration to ```jupyterhub_config.py```

```
import sys
...

c.JupyterHub.services = [
        {
            'name': 'cull-idle',
            'admin': True,
            'command': [sys.executable,
                        '/etc/jupyterhub/cull_idle_servers.py',
                        '--timeout=3000',
                        '--url=http://127.0.0.1:8081/hub/api'
                        ],
        }
    ]
```


## Shut down JupyterHub, Nginx, and the server.

## Add files to git, commit and push

 - locally:

```
git add .
git commit -m "end of S01-E06"
git push origin master
```

## Review and Preview Next Episode
