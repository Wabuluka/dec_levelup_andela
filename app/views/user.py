from flask import Blueprint, request, jsonify
from app.model.user import UserModel

user = Blueprint('users', __name__)
usermodel = UserModel()

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
        return jsonify({"message":"first signup"})
    check_psw = check_user['password']
    if check_psw:
        return jsonify({"message": "logged in successfully"}), 200

    return jsonify({"message": "first loggin"})


