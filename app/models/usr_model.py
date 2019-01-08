import datetime

class UserModel:

    # initialization
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.firstname = kwargs.get("firstname")
        self.lastname = kwargs.get("lastname")
        self.othernames = kwargs.get("othernames")
        self.email = kwargs.get("email")
        self.phonenumber = kwargs.get("phonenumber")
        self.username = kwargs.get("username")
        self.registeredOn = kwargs.get("registeredOn")
        self.isAdmin = kwargs.get("isAdmin")

    # convert user attributes to a dictionary
    def usr_dictionary(self):
        return {
            "id" : self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "othernames": self.othernames,
            "email":self.email, 
            "phoneNumber":self.phonenumber, 
            "username":self.username,
            "registeredOn":self.registeredOn.date.today(),
            "isAdmin":self.isAdmin
        }