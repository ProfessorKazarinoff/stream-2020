# S01-E04 Contents

## Who am I? Why am I doing this?

 > Blog: https://pythonforundergradengineers.com/

 > Book: https://www.amazon.com/Problem-Solving-Python-3-7-open-source/dp/1693405415

## Review where the GitHub Repo for the stream can be found

 > https://github.com/ProfessorKazarinoff/stream-2020

Code of conduct: https://github.com/ProfessorKazarinoff/stream-2020/blob/master/code-of-conduct/code_of_conduct.md

## Review what JupyterHub is, the JupyterHub Docs, and the docs we are following in this series

 > https://jupyterhub.readthedocs.io/en/stable/

 > https://professorkazarinoff.github.io/jupyterhub-ENGR114-2019Q4/

## Start up the server and update

 - Startup the server from the Linode Dashboard

## Review what we did last time

 - Routed our domain name to Linode name servers
 - Added an A record in the Linode domains dashboard to link our domain name to our server IP address
 - Installed Miniconda, created a conda virtual environment
 - Installed conda packages (NumPy, Pandas, etc), JupyterHub
 - Ran JupyterHub in a very unsecure (no SSL, regular http) fashion
 - Aquired an SSL cert using Certbot

## Create files for security

 - The JupyterHub docs state where to put certain files: https://jupyterhub.readthedocs.io/en/stable/installation-basics.html
 - Note: run ```# starting S01-E04``` as first command. Put ```# generate proxy auth token``` before typing sets of commands

 - cookie secret

 ```
 # create cookie secret
cd /srv
sudo mkdir jupyterhub
cd jupyterhub
sudo touch jupyterhub_cookie_secret
sudo chown :sudo jupyterhub_cookie_secret
sudo chmod g+rw jupyterhub_cookie_secret
sudo openssl rand -hex 32 > jupyterhub_cookie_secret
sudo chmod 600 jupyterhub_cookie_secret
```

 - proxy auth token

```
# create proxy_auth_token
pwd
sudo touch proxy_auth_token
sudo chown :sudo proxy_auth_token
sudo chmod g+rw proxy_auth_token
sudo openssl rand -hex 32 > proxy_auth_token
sudo chmod 600 proxy_auth_token
```
 - dhparams.pem

```
# create dhparam.pem
pwd
sudo touch dhparam.pem
sudo chown :sudo dhparam.pem
sudo chmod g+rw dhparam.pem
sudo openssl dhparam -out /srv/jupyterhub/dhparam.pem 2048
sudo chmod 600 dhparam.pem
```

## Install Nginx and configure

 - install Nginx

```
# Nginx install
sudo apt-get -y install nginx
sudo ufw allow 'Nginx Full'
sudo ufw status
sudo systemctl status nginx
```

 - create Nginx configuration (maybe mess around locally and move it with ftp and FileZilla) see: https://github.com/ProfessorKazarinoff/ansible-jupyterhub/blob/master/templates/sites-available.j2

 - Link sites-available to sites-enabled

```
# Nginx configuration
cd /etc/nginx
sudo nano nginx.conf
cd sites-available
sudo rm default
sudo ln -s /etc/nginx/sites-available/engr101lab.org /etc/nginx/sites-enabled/
sudo nginx -t
cd sites-enabled/
sudo rm default
sudo nginx -t
sudo systemctl stop nginx
sudo systemctl status nginx
sudo systemctl start nginx
sudo systemctl status nginx
```

## JupyterHub config to use cookie secret and proxy auth token

 - ```jupyterhub_config.py``` file in ```/etc/jupyterhub/```

```
cd /etc
sudo mkdir jupyterhub
sudo chown -R root:peter jupyterhub/
sudo chmod -R g+rwx jupyterhub/
cd jupyterhub/
conda activate jupyterhubenv
jupyterhub --generate-config
jupyterhub
```

## JupyterHub as a system service

 - systemd config file ```jupyterhub.service``` in ```/etc/systemd/system```

```
# jupyterhub as a system service
cd /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl start jupyterhub
sudo systemctl status jupyterhub
sudo systemclt status nginx
```

## Test JupyterHub running in SSL with Nginx as a reverse proxy

Browse to:

 > https://engr101lab.org

## Save History, Shut down server

```
# shut everything down
sudo systemctl stop jupyterhub
sudo systemctl status jupyterhub
sudo systemctl stop nginx
sudo systemctl status nginx
sudo shutdown -h now
```

 - shut down server on the Linode dashboard


## Add files to git, commit and push

```
# locally
git add .
git commit -m "End of S01-E04"
git push origin master
```

## Review and Preview Next Episode
