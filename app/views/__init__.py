from flask import Flask, jsonify, request, json
import re
from flask_jwt_extended import create_access_token, jwt_required
from datetime import timedelta
from app.validation.input_validation import validate_user_details
# from app.validation.input_validation import Validator
from flask.views import MethodView
from datetime import date
from app.models.corrupt_model import CorruptionCase 
from flask_jwt_extended import (jwt_required, get_jwt_identity)

from app.models.usr_model import UserModel
