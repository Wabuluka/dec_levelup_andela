from flask import Flask, jsonify, request, json
from flask.views import MethodView

from app.models.corrupt_model import CorruptionCase
from app.models.usr_model import UserModel

red_flag_records = []
users = []
count = 0