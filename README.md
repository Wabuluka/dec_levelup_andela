# iReporter - Andela
[![Build Status](https://travis-ci.com/Wabuluka/dec_levelup_andela.svg?branch=chore-162694106-setting-up-api-development)](https://travis-ci.com/Wabuluka/dec_levelup_andela) [![Maintainability](https://api.codeclimate.com/v1/badges/2f70fe6afecdcb5b79c5/maintainability)](https://codeclimate.com/github/Wabuluka/dec_levelup_andela/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/2f70fe6afecdcb5b79c5/test_coverage)](https://codeclimate.com/github/Wabuluka/dec_levelup_andela/test_coverage)

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
|POST| /api/v1/redflags/<int:id>| Add a new red flag record|

## Running the tests

It only needs one code statement to run the test for this simple application

Run the following command in your terminal or cmd
Although at the moment my tests are not fully functional, am still learning how to make them better

```
python -m unittest
```
## Deployment

You can find a demo view of how this application works from heroku
(still working on deployment)
## Authors

* **Davies Wabuluka**  - [Github](https://github.com/Wabuluka)
