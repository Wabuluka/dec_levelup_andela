from functools import wraps
import jwt
import datetime
from flask import current_app as app 
from flask import jsonify, request
from app.model.user import UserModel

usermodel =UserModel()

class ProtectedRoutes:
    SECRET = "1234wabuluka"

    def tok_enconder(self, email):
        data = {
            'email' : email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)

        }
        return jwt.encode(data, '1234wabuluka', algorithm='HS256')

protect_jwt = ProtectedRoutes()

def protected(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        access_token = None
        if 'Authorization' in request.headers:
            access_token = request.headers['Authorization']
            # print("1\n")
            # print(access_token)
            # print("2\n")
        if not access_token:
            return jsonify({'status': 401, 'error': 'there is no token'}), 401
        try:
            data = jwt.decode(access_token, '1234wabuluka', algorithm='HS256')
            # print(data['email'])
            active_user = usermodel.get_userby_email(data['email'])
        except jwt.ExpiredSignatureError:
            return jsonify({'status': 401, 'error': 'seems like your access token has expired'}), 401
        return f(active_user, *args, **kwargs)
    return decorator