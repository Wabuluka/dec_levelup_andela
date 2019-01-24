from flask import Blueprint, request, jsonify
# import jwt
# import datetime
# from functools import wraps
from app.utilities.helpers import create_token
from app.model.user import UserModel

user = Blueprint('users', __name__)
usermodel = UserModel()

# def token_req(end_point):
#     @wraps(end_point)
#     def check(*args, **kwargs):
#         if 'token' in request.headers:
#             tk = request.headers['token']
#         else:
#             return jsonify({'message': 'you should login'})
#         try:
#             jwt.decode(tk, 'jghbjg_scretekey')
#         except:
#             return jsonify({'message': 'user not authenticated'})
#         return end_point(*args, **kwargs)
#     return check

@user.route('/signup', methods=["POST"])
def create_user():

    data = request.get_json()
    
    firstname = data['firstname']
    lastname = data['lastname']
    othernames = data['othernames']
    email = data['email']
    phonenumber = data['phonenumber']
    username = data['username']
    password = data['password']

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
        # tk = jwt.encode({
        #     'username': user['username'],
        #     'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10)}, 'jghbjg_scretekey')
        
        return jsonify({"message": "you are now logged in", "token": token})

    return jsonify({"message": "first loggin"})


