from app.model.db import DatabaseConnection
from flask import request
import datetime
import json
import re

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


    # sign up query
    def create_user(self, user):
        cursor.execute("INSERT INTO users(firstname, lastname, othernames, email, phonenumber, username, password )"
                            " VALUES(%s,%s,%s,%s, %s,%s, %s)", (user.firstname, user.lastname, user.othernames,
                                                                user.email, user.phonenumber, user.username, user.password
                                                                ))
    
    # login query
    def get_userby_email(self , email):
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        return cursor.fetchone()

    # edit redflag status
    # edits a location of the incident regardless of the casetype
    def patch_redflag_status(self, id, status):
        self.cursor.execute(f"UPDATE redflag SET status='{status}' WHERE id = {id}")
        return True


    # edit intervention status
    # edits a location of the incident regardless of the casetype
    def patch_intervention_status(self, id, status):
        self.cursor.execute(f"UPDATE intervention SET status='{status}' WHERE id = {id}")
        return True

"""
    Validators for the user sign up
"""
class UserValidation:
    pass
