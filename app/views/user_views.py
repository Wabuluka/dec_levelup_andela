from . import *
"""
    creating a new user
"""
usermodel = UserModel()
class CreateNewUser(MethodView):
    
    def post(self):
        if request.content_type != 'application/json':
          return jsonify({ "status": "404", "message": "Change content_type to json" })
        data = request.get_json()
        
        firstname = data['firstname'],
        lastname = data['lastname'],
        othernames = data['othernames'],
        email = data['email'],
        phonenumber = data['phonenumber'],
        username = data['username'],
        password = data['password']

        new_user = UserModel(firstname=firstname,lastname=lastname, othernames=othernames, email=email, phonenumber=phonenumber,username= username, password=password)
        usermodel.create_user(new_user)
        return jsonify({"status": 200, "message": "Created success"})

    def post_user(self):
        if request.content_type != 'application/json':
          return jsonify({ "status": "404", "message": "Change content_type to json" })
        data = request.get_json()

        email= data.get("email")
        password = data.get("password")

        chech_user = usermodel.get_userby_email(email)

        if chech_user:
            password = chech_user['password']
            return jsonify({"message": "logged in successfully"})

        return jsonify({"message": "first loggin"})

        
