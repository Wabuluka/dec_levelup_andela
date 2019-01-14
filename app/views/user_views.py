from . import *
"""
    creating a new user
"""
class CreateNewUser(MethodView):
    
    def post(self, userId):
        data = request.get_json()
        
        user = UserModel(
          userid = data['userid'],
          firstname = data['firstname'],
          lastname = data['lastname'],
          othername = data['othernames'],
          email = data['email'],
          phonenumber = data['phonenumber'],
          username = data['username'],
          registeredOn = data['registeredOn'],
          isAdmin = data['isAdmin']
        )
        users.append(user)
        return jsonify({"data": user.usr_dictionary()})