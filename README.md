# covid-19-statistics

# INTRODUCTION
This is a devops Project about using jenkins to query a flask service

The project includes 2 parts-

First part- Service: The server have 4 endpoint return a JSON response. 

This part includes a connection with an external API (https://corona.lmao.ninja/docs/).

Second part- JenkinsFile: that runs my flask-app and test its by using an input list of countries from the jenkins Input part.

This part includes 

- clones this repository - https://github.com/noashabtay/covid-19-statistics.git
- runs the flask app
- waits for input (list of countries)
- query the flask app with curl commands


# INFO
Project name: covid-19-statistics


- Python version: 2.7 / 3.8
- pip version: 20.2.3
- flask version: 20.2.3
- requests version: 2.24.0


this project assumes that python with flask and requests packages install on your computer

first, please make sure the follows are installed:

- pip install flask
- pip install requests



# OPERATIONS
in your local jenkins run jenkinsfile as you like
- if you run with Pipline script from SCM -

  - change the 'Branch Specifier (blank for 'any')' to */*main* 
  - change the 'Script Path' to *jenkinsfile*


After build you will have to insert a list of countries in the input session

