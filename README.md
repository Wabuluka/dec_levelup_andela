# iReporter - Andela
[![Build Status](https://travis-ci.org/Wabuluka/dec_levelup_andela.svg?branch=challenge_two_flask_api)](https://travis-ci.org/Wabuluka/dec_levelup_andela) [![Maintainability](https://api.codeclimate.com/v1/badges/2f70fe6afecdcb5b79c5/maintainability)](https://codeclimate.com/github/Wabuluka/dec_levelup_andela/maintainability) [![Coverage Status](https://coveralls.io/repos/github/Wabuluka/dec_levelup_andela/badge.svg?branch=develop)](https://coveralls.io/github/Wabuluka/dec_levelup_andela?branch=develop)


In this API, I have put together a simple way in which you can create, retrieve, update and delete data from a list. The API further immitates how one can report corruption cases in their communities and also bring to notice of the relevent governments about the occurance of interventions that may need urgent attention. 
This API takes advantage of persistent data as a form of datastructure meaning that a database has been used. This makes it possible to store your details for further use.
## Getting Started
To get start with this API, you will need to set up a few prerequists as I am going to guide below.
### Prerequisites
This api must work on any operating system with minimal requirements that is connected to the internet and has an updated  browser.

### Python versions supported
Make sure you have python version
```
python 2.7 and above
```
But to be sure of what you are doing, I strongly recommend python 3.7.6 as it is the one I have used to develop this API

### Installing
After setting up the Python Version, follow the instructions below to setup the virtual environment
In the root folder of the API, create a virtual environment, but first make sure the virtual enviroment dependency is installed by 
```
pip install virtualenv
```
Then create a virtual environment
```
virtualenv venv
```

#### Downloading and setting up PostgreSQL
Postgres is the database being used in this API so to be able to use it offline, one may need to down it and set it up first.
After the setting up, create two databases 
```
createdb ireporter_db
```
and also
```
createdb ireporter_test_db
```
The database ```ireporter_db``` is for actual development purposes or production if used offline and the ```ireporter_test_db is for testing purposes.

#### Activating the virtual environment
For Windows OS
```
. /venv/Script/activate
```
For Linux Systems
```
. /venv/bin/activate
```
#### Installing the dependencies in the virtual environment created
To add all the dependencies as required for the API, install the requirements file
```
pip install -r requirements.txt
```
After  the dependencies are installed the API should work following the endpoints below

## Running the API offline
It is possible to run the API offline by executing 
```
py run.py
```
in the root of the application
Make sure you are in a virtual environment for this to work

## Endpoints in the API
Theses are the endpoint that have been implemented in this API
|REQUEST TYPE| URL | DESCRIPTION |
|------------|-----|-------------|
|POST| /api/v2/red-flags| Add a new red flag incident|
|GET| /api/v2/red-flags| Retrieves all the available red flag incidents|
|GET| /api/v2/red-flags/<int:id>| Retrives a specified red flag incident|
|PATCH| /api/v2/red-flags/<int:id>|comment| Edit a specific red flag comment|
|PATCH| /api/v2/red-flags/<int:id>|location| Edit a specific red flag location|
|DELETE| /api/v2/red-flags/<int:id>| Deletes a red flag incident|
|POST| /api/v2/interventions| Add a new interventions incident|
|GET| /api/v2/interventions| Retrieves all the available interventions incidents|
|GET| /api/v2/interventions/<int:id>| Retrives a specifiedinterventions incident|
|PATCH| /api/v2/interventions/<int:id>|comment| Edit a specific interventions comment|
|PATCH| /api/v2/interventions/<int:id>|location| Edit a specific interventions location|
|DELETE| /api/v2/interventions/<int:id>| Deletes a interventions incident|
|POST| /api/v2/auth/signup| registering a new user|
|POST| /api/v2auth/signin| login a user|
|PATCH|/api/v2/admin//red-flags/<int:id>/status| allows admin to edit a status of the red flag specified|
|PATCH|/api/v2/admin//interventions/<int:id>/status| allows admin to edit a status of the intervention specified|



## Running the tests

It only needs one code statement to run the test for this simple application

Run the following command in your terminal or cmd
Although at the moment my tests are not fully functional, am still learning how to make them better and all the feedback is welcome.

```
pytest
```
## Deployment
This API has been hosted with [heroku](https://ireporterthree.herokuapp.com/api/v2/red-flags)

## Authors

* **Davies Wabuluka**  - [Github](https://github.com/Wabuluka)
