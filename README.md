# covid-19-statistics

# INTRODUCTION
This is a devops-test Project about using jenkins to query a flask service

The project includes 2 parts-

First part- Service: The server have 4 endpoint return a JSON response. 

This part includes a connection with an external API (https://corona.lmao.ninja/docs/).

Second part- JenkinsFile: that runs my flask-app and test its by using an input list of countries from the jenkins Input part.

This part includes 

- clone with this repository - https://github.com/noashabtay/covid-19-statistics.git
- running the flask app
- watting for input - list of countries
- query the flask app with curl command 


# INFO
Project name: covid-19-statistics

this project assumes that python with flask and requests packages install on your computer
first please make sure the follows are install :

- pip install flask
- pip install requests



# OPERATIONS
in your local jenkins run jenkinsfile as you like
- if you run with Pipline script from SCM -

  - change branch name to "*/*main*" 
  - change script path to "*jenkinsfile*"


After build you will have to insert a list of countries in the input session

