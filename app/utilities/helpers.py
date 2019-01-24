import jwt
from functools import wraps
from flask import request
import datetime


def create_token(email):
    token = jwt.encode({'email': email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, 'wabuluka', algorithm='HS256').decode('utf-8')
    return token


def decode_token(token):
    decoded_token = jwt.decode(token, 'wabuluka', algorithm='HS256')
    return decode_token

def token_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # if token is valid
        try:
            token = request.headers.get('access_token')
            return function(*args, *kwargs)

        except (jwt.exceptions.InvalidTokenError, jwt.exceptions.ExpiredSignatureError, jwt.exceptions.InvalidKeyError):
            return jsonify({"error": "invalid token, login to get a valid token"})   
    return wrapper