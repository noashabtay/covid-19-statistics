# covid-19-statistics

# INTRODUCTION
This is a devops-test Project about using jenkins to query a flask service

The project includes 2 parts-

First part- Service: The server have 4 endpoint return a JSON response. 

This part includes a connection with external API (https://corona.lmao.ninja/docs/)

Second part- JenkinsFile: that runs my flask-app and test its by using an input list of countries from the jenkins Input part
This part includes a connection with this repository - https://github.com/noashabtay/covid-19-statistics.git
running the flask app and query it with curl command 

# OPERATIONS
in your local jenkins run jenkinsfile as you like
- if you running with Pipline script from SCM -

  - notice to change branch name to "*/*main*" 
  - and to change script path to "*jenkinsfile*"


After build - you will have to insert list of countries in the Input Session


# INFO
Project name: covid-19-statistics

python: 3
please install first:

pip install flask
pip install requests

