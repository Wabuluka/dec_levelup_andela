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
        
        firstname = data['firstname']
        lastname = data['lastname']
        othernames = data['othernames']
        email = data['email']
        phonenumber = data['phonenumber']
        username = data['username']
        password = data['password']

       
        val = validate_user_details(firstname, lastname, othernames, email, phonenumber,  username, password)
        if val:
            return val

        new_user = UserModel(firstname=firstname,lastname=lastname, othernames=othernames, email=email, phonenumber=phonenumber,username= username, password=password)
        # input_check(new_user)
        usermodel.create_user(new_user)
        return jsonify({"status": 200, "message": "Created success"})

        # def validate_input(self):
      

        check_uaername = re.compile("^[A-Za-z\s]{4,30}$")
        if not check_username.match(self.username):
            return "enter correct credentials"
        return None

class SigninUser(MethodView):
    def post(self):
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
            my_identity = dict(
                user_id=check_user.get('user_id')
            # user_role=check_user.get('role')
            )
            
            return jsonify({"access_token": create_access_token(identity=my_identity, expires_delta=timedelta(hours=3)),
            "message": "logged in successfully"}), 200

        return jsonify({"message": "first loggin"})

        
