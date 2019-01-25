from flask import Blueprint, request, jsonify
# from app.model.user import validate_user_details
import jwt
import datetime
from functools import wraps
from app.utilities.helpers import create_token
from app.model.user import UserModel, Validation

user = Blueprint('users', __name__)
usermodel = UserModel()
valid = Validation()

# def token_req(end_point):
#     @wraps(end_point)
#     def check(*args, **kwargs):
#         print('hello')
#         if request.headers.get("Authorization"):
#             tk = request.headers.get("Authorization")
#             print(tk)
#         else:
#             return jsonify({'message': 'you should login'})
#         try:
#             jwt.decode(tk, 'wabuluka')
#         except:
#             return jsonify({'message': 'user not authenticated'})
#         return end_point(*args, **kwargs)
#     return check

@user.route('/signup', methods=["POST"])
def create_user():

    keys = ("firstname","lastname","othernames","email", "phonenumber", "username", "password")
    if not set(keys).issubset(set(request.json)):
        return jsonify({"message":"all fields are required"})

    data = request.get_json()
    
    firstname = data['firstname']
    lastname = data['lastname']
    othernames = data['othernames']
    email = data['email']
    phonenumber = data['phonenumber']
    username = data['username']
    password = data['password']

    user = usermodel.get_userby_email(email)
    if user:
        return jsonify({"message": "user already exists just login"})

    val = valid.validate_user_details(firstname, lastname, othernames, email, phonenumber, username, password)

    if val:
        return val

    new_user = UserModel(firstname=firstname,lastname=lastname, othernames=othernames, email=email, phonenumber=phonenumber,username= username, password=password)
    usermodel.create_user(new_user)
    return jsonify({"status": 200, "message": "Created success"})

@user.route('/signin', methods = ["POST"])
def signin_user():
    if request.content_type != 'application/json':
        return jsonify({ "status": "404", "message": "Change content_type to json" })
    data = request.get_json()

    email= data.get("email")
    password = data.get("password")

    check_user = usermodel.get_userby_email(email)
    # print(chech_user)
    if not check_user:
        return jsonify({"message":"Invalid email or password"})
    check_psw = check_user['password']
    if check_psw == password:
        token = create_token(email)
        tk = jwt.encode({
            'username': check_user['username'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10)}, 'wabuluka')
        
        return jsonify({"message": "you are now logged in", "token": token})

    return jsonify({"message": "first loggin"})
