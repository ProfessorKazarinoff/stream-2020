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
 - add domain name to Linode domains dashboard
 - in Linode, route domain name to server IP. Create A name record
 - Wait...
 - https://www.whatsmydns.net can be used to check the NS and A records of our domain and see if the domain name is getting through

## Install Miniconda on server, set up jupyterhubenv conda env

 - install miniconda, modify permissions

 - create a jupyterhubenv conda environment

 - install conda packages: jupyter, numpy, pandas, xlrd, matplotlib, sympy, requests, bokeh, altair, jupyterhub

## Try to run JupyterHub for the first time

 - open port 8000 on the ufw firewall

## Check if domain name routing is complete

See if the domain name is successfully routed over to Linode

 > https://www.whatsmydns.net/

## Use Certbot to generate an SSL certificut

Certbot saved the SSL cert in

```
/etc/letsencrypt/live/engr101lab.org/fullchain.pem
/etc/letsencrypt/live/engr101lab.org/privkey.pem
```

## Save History

```
sudo apt-get -y update && sudo apt-get -y upgrade
clear
cd /tmp
pwd
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
ls
clear
ls
sudo bash Miniconda3-latest-Linux-x86_64.sh
cd ~
ls -la
source .bashrc
python
clear
cd /opt
ls
ls -la
sudo chmod -R g+w miniconda3/
ls -la
sudo chown -R root:peter miniconda3/
ls -la
conda --version
cd ~
clear
conda create -y -n jupyterhubenv python=3.7
conda activate jupyterhubenv
clear
conda install -y numpy matplotlib pandas xlrd scipy sympy jupyter notebook bokeh seaborn pyserial
python
clear
conda install -y -c conda-forge pint altair jupyterlab
clear
conda install -y requests
clear
conda list
clear
conda install -y -c conda-forge jupyterhub
python
clear
sudo ufw status
sudo ufw allow 8000
sudo ufw status
clear
jupyterhub --no-ssl
clear
sudo ufw status
sudo ufw deny 8000
sudo ufw status
clear
sudo ufw status
sudo ufw allow 80
sudo ufw status
cd ~
clear
mkdir certbot
cd certbot
wget https://dl.eff.org/certbot-auto
ls
ls -la
chmod a+x certbot-auto
ls -la
clear
./certbot-auto certonly --standalone -d engr101lab.org
sudo ufw status
sudo ufw deny 80
sudo ufw status

```

## Shut down server

## Add files to git, commit and push

## Review and Preview Next Episode
