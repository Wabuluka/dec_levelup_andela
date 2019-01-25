import os
import jwt
from functools import wraps
from flask import request
# from app.utilities.helper_functions import Helper_Functions


# def admin_required(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         access_token = get_token()
#         if access_token:
#             status = decode_admin_status(access_token)
#             if status == 'True':
#                 if isinstance(status, str):
#                     return Helper_Functions.the_return_method(401, status)
#                 return f(*args, **kwargs)
#             else:
#                 return Helper_Functions.the_return_method(403, "Access not authorized.")
#         else:
#             return Helper_Functions.the_return_method(
#                 401, "A Resource Token is required. Sign-in or log-in")       
#     return wrap


def token_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        access_token = get_token()
        if access_token:
            user_id = decode_token(access_token)
            if isinstance(user_id, str):
                return Helper_Functions.the_return_method(401, user_id)
            current_user = user_id
            return f(current_user, *args, **kwargs)
        else:
            return Helper_Functions.the_return_method(
                401, "A Resource Token is required. Sign-in or log-in")       
    return wrap



def get_token():
    auth_header = request.headers.get('Authorization')
    access_token = str(auth_header).split(" ")[1]
    return access_token

def decode_token(token):
        try:
            payload = jwt.decode(
                token, str(
                    os.getenv('SECRET')), algorithms='HS256')
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return "Expired token. Please login to get a new token"
        except jwt.InvalidTokenError:
            return "Invalid token. Please register or login"
        return None

# def decode_admin_status(token):
#     payload = jwt.decode(token, str(
#         os.getenv('SECRET')), algorithms='HS256')
#     return payload['adn']

