from flask import Flask
from flask_restful import Api

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
api = Api(app)


"""
    Importing views
"""
from app import views