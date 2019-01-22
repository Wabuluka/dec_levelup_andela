from app.models.db_conn import DatabaseConnection
import datetime
import json

cursor = DatabaseConnection().cursor

class UserModel:

    # initialization
    def __init__(self, **kwargs):
        self.userid = kwargs.get("id")
        self.firstname = kwargs.get("firstname")
        self.lastname = kwargs.get("lastname")
        self.othernames = kwargs.get("othernames")
        self.email = kwargs.get("email")
        self.phonenumber = kwargs.get("phonenumber")
        self.username = kwargs.get("username")
        self.registeredOn = kwargs.get("registeredOn")
        self.isAdmin = kwargs.get("isAdmin")
        self.password = kwargs.get("password")

    # convert user attributes to a dictionary
    def usr_dictionary(self):
        return {
            "userid" : self.userid,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "othernames": self.othernames,
            "email":self.email, 
            "phoneNumber":self.phonenumber, 
            "username":self.username,
            "registeredOn":self.registeredOn.date.today(),
            "isAdmin":self.isAdmin,
            "password": self.password
        }

    def create_user(self, user):
        cursor.execute("INSERT INTO users(firstname, lastname, othernames, email, phonenumber, username, password )"
                            " VALUES(%s,%s,%s,%s, %s,%s, %s)", (user.firstname, user.lastname, user.othernames,
                                                                user.email, user.phonenumber, user.username, user.password
                                                                ))
    

    def get_userby_email(self , email):
        cursor.execute("SELECT * FROM users WHERE email = %s", (email))
        return cursor.fetchone()