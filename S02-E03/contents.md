# S02-E03 Contents

## Who am I? Why am I doing this?

 > Blog: https://pythonforundergradengineers.com/

 > Book: https://www.amazon.com/Problem-Solving-Python-3-7-open-source/dp/1693405415

## Review where the GitHub Repo for the stream can be found

 > https://github.com/ProfessorKazarinoff/stream-2020

Code of conduct: https://github.com/ProfessorKazarinoff/stream-2020/blob/master/code-of-conduct/code_of_conduct.md


## What is Zappa? Why are we using Zappa

 > https://github.com/Miserlou/Zappa

## Blog Post

 > https://pythonforundergradengineers.com/deploy-serverless-web-app-aws-lambda-zappa.html

## Virtual Environment

```
cd ~/Documents
mkdir zappa_app_flask
cd zappa_app_flask
python -m venv venv
source venv/bin/activate
python -m pip install flask zappa
python -m pip freeze > requirements.txt
```

## Simple Flask App

## AWS Credentails

 - Create a group
 - Attach inline policy to group
 - Create a user and user to the group
 - copy aws access key id and aws secret access key

## Deploy Zappa on AWS Lambda

```
zappa init
zappa deploy dev
# make changes to the app
zappa update dev
```

## Conclusion

That's all for today. Next week we'll explore a different Python web technology.
