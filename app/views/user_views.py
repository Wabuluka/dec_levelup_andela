from . import *
"""
    creating a new user
"""
class CreateNewUser(MethodView):
    
    def post(self):
        data = request.get_json()
        
        user = UserModel(
          userid = len(users) + 1,
          firstname = data['firstname'],
          lastname = data['lastname'],
          othername = data['othernames'],
          email = data['email'],
        #   phonenumber = data['phonenumber'],
          username = data['username'],
        #   registeredOn = data['registeredOn'],
        #   isAdmin = data['isAdmin']
        )
        users.append(user.usr_dictionary())
        return jsonify({"data": user.usr_dictionary()})