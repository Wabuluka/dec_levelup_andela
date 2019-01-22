# iReporter - Andela
[![Build Status](https://travis-ci.org/Wabuluka/dec_levelup_andela.svg?branch=challenge_two_flask_api)](https://travis-ci.org/Wabuluka/dec_levelup_andela) [![Maintainability](https://api.codeclimate.com/v1/badges/2f70fe6afecdcb5b79c5/maintainability)](https://codeclimate.com/github/Wabuluka/dec_levelup_andela/maintainability) [![Coverage Status](https://coveralls.io/repos/github/Wabuluka/dec_levelup_andela/badge.svg?branch=challenge_two_flask_api)](https://coveralls.io/github/Wabuluka/dec_levelup_andela?branch=challenge_two_flask_api)


In this API, I have put together a simple way in which you can create, retrieve, update and delete data from a list. The API further immitates how one can report corruption cases in their communities
## Getting Started
To get start with this API, you will need to set up a few prerequists as I am going to guide below.
### Prerequisites
This api must work on any operating system with minimal requirements

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
## Endpoints in the API
|REQUEST TYPE| URL | DESCRIPTION |
|------------|-----|-------------|
|POST| /api/v1/redflagrecords| Add a new red flag record|
|POST| /api/v1//api/v1/user| Register new user|
|GET| /api/v1/redflagrecords| Gets all the available red flag records in the list|
|GET| /api/v1/redflagrecords/<int:id>| Get a specific incident by id|
|PUT| /api/v1/redflagrecords/edit-status/<int:id>| Edit a specific incident's status|
|DELETE| /api/v1/redflagrecords/<int:id>| Deletes a red flag record|
|PUT| /api/v1/redflagrecords/edit-location/<int:id>| Edit a specific incident's location|
|PUT| /api/v1/redflagrecords/edit-comment/<int:id>| Edit a specific incident's comment|


## Running the tests

It only needs one code statement to run the test for this simple application

Run the following command in your terminal or cmd
Although at the moment my tests are not fully functional, am still learning how to make them better

```
python -m unittest
```
## Deployment
This API has been hosted with [heroku](https://andela35dwabuluka.herokuapp.com/api/v1/redflagrecords)

## Authors

* **Davies Wabuluka**  - [Github](https://github.com/Wabuluka)
