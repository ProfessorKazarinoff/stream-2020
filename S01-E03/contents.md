# S01-E03 Contents

## Who am I? Why am I doing this?

 > Blog: https://pythonforundergradengineers.com/

 > Book: https://www.amazon.com/Problem-Solving-Python-3-7-open-source/dp/1693405415

## Review where the GitHub Repo for the stream can be found.

 > https://github.com/ProfessorKazarinoff/stream-2020

Code of conduct: https://github.com/ProfessorKazarinoff/stream-2020/blob/master/code-of-conduct/code_of_conduct.md

## Review what JupyterHub is, the JupyterHub Docs, and the docs we are following in this series.

 > https://jupyterhub.readthedocs.io/en/stable/

 > https://professorkazarinoff.github.io/jupyterhub-ENGR114-2019Q4/

## Review what we did last time

 - SSH keys
 - Created a virtual private server on Linode
 - Non-root sudo user, ufw firewall

## Route domain name to Linode DNS servers

 - in Google Domains, route domain name to Linode DNS servers
 - add domain name to Linode dashboard
 - in Linode, route domain name to server IP. Create A name record
 - Wait...
 - https://www.whatsmydns.net can be used to check the NS and A records of our domain and see if the domain name is getting through

## Install Miniconda on server, set up jupyterhubenv conda env

 - install miniconda, modify permissions

 - create a jupyterhubenv conda environment

 - install conda packages: jupyter, numpy, pandas, xlrd, matplotlib, sympy, requests, bokeh, altair, jupyterhub

## Try to run JupyterHub for the first time

## Save history

## Check if domain name routing is complete

## Work on SSL security? Certbot or cookie secret, proxy auth token, dhparams

## Shut down server

## Add files to git, commit and push

## Review and Preview Next Episode
