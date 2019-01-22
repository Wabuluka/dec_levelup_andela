from flask import Flask, jsonify, request, json

from app.validation.input_validation import Validator
from flask.views import MethodView
from datetime import date

from app.models.corrupt_model import CorruptionCase
from app.models.usr_model import UserModel

incidentmodel = CorruptionCase()
usermodel = UserModel()