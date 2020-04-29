# S01-E02 Contents

## Who am I? Why am I doing this?

 > Blog: https://pythonforundergradengineers.com/

 > Book: https://www.amazon.com/Problem-Solving-Python-3-7-open-source/dp/1693405415

## Review where the GitHub Repo for the stream can be found.

 > https://github.com/ProfessorKazarinoff/stream-2020

## Review the Code of Conduct for the Stream

 > https://github.com/ProfessorKazarinoff/stream-2020/blob/master/code-of-conduct/code_of_conduct.md

Follows Project Jupyter's Governance Model [https://github.com/jupyter/governance](https://github.com/jupyter/governance)

## Review what JupyterHub is, the JupyterHub Docs, and the docs we are following in this series.

 > https://jupyterhub.readthedocs.io/en/stable/

 > https://professorkazarinoff.github.io/jupyterhub-ENGR114-2019Q4/

## Review what tools we need in place and what services we will use.

 - Windows 10 (or MacOS, Linux) computer with internet access
 - Anaconda Distribution of Python
 - VS Code
 - PuTTY and PuTTY Gen
 - FileZilla
 - GitHub.com account
 - Google account
 - Linode account
 - Domain name

## Talk SSH keys and use PuTTY Gen to create an SSH key

public key will be stored on the cloud server

private key will be store on our local computer and we'll use it to remote into our server over SSH

## Talk Virtual Private Servers, log into Linode and create a new server

for creating a random password with Python: https://gist.github.com/ProfessorKazarinoff/1271e56f1ed3243a1f4d397d61d23dcc

## Talk SSH and log into the server over SSH

Use the SSH and PuTTY to log into the server as root. Then run

```
apt-get -y update && apt-get -y upgrade
```

## Create a non-root sudo user on the server and copy over SSH keys into the non-root sudo user's account, modify ufw firewall, save history

```
adduser peter
usermod -aG sudo peter
su - peter
# exit to leave the peter user and go back to root
rsync --archive --chown=peter:peter ~/.ssh /home/peter
```

Enable to uwf firewall. Allow OpenSSH past the firewall

```
apt-get install ufw
ufw allow OpenSSH
ufw enable
ufw status
```

## Log into the server as non-root sudo user, save history

Log into the server using the peter username and the same SSH key. Make sure you can run commands as ```sudo```

```
sudo apt-get -y update && sudo apt-get -y upgrade
```

## Add files to git, commit and push

## Review and Preview Next Episode
