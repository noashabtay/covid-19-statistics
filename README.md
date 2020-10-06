# covid-19-statistics

# INTRODUCTION
This is a Devops-test Project about Recipes website.

The project includes 2 parts-

First part- Service: The server have 4 endpoint return a JSON response. 

This part includes a connection with external API (https://corona.lmao.ninja/docs/)

Second part- JenkinsFile: I create a jenkinsfile that runs my flask-app and test its by using an input list of countries from the jenkins Input part

# OPERATIONS
enter your local jenkins and run jenkinsfile as you like,
but if you running with Pipline script from SCM - notice to change branch name to "/*/*main*/" 
and to change script path to "/*jenkinsfile*/"


After build - you will have to insert list of countries in the Input Session


# INFO
Project name: covid-19-statistics

python: 3
please install first:

pip install flask
pip install requests

