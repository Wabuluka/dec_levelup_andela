from app.model.db import DatabaseConnection
import datetime
import json

cursor = DatabaseConnection().cursor

class RedFlag:

    # initialization
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.casetype = kwargs.get("casetype")
        self.createdby = kwargs.get("createdby")
        self.location = kwargs.get("location")
        self.status = kwargs.get("status")
        self.comment = kwargs.get("comment")
        self.cursor = cursor

    # -------------------------------------------redflag-----------------------------------------------_
    def create_redflag(self, flag):
        self.cursor.execute("INSERT INTO redflag(casetype, createdby, location, comment, status)"
                            " VALUES(%s,%s,%s,%s, %s)", (flag.casetype, flag.createdby, flag.location,
                                                                flag.comment, flag.status
                                                                ))


    # gets all the incidents regardless of the casetype
    def get_all(self):
        self.cursor.execute("SELECT * FROM redflag")
        return self.cursor.fetchall()


    # gets a specific incident by id regardless of the casetype
    def get_one(self, id):
        self.cursor.execute("SELECT * FROM redflag WHERE id =%s", (id,))
        return self.cursor.fetchone()


    # deletes a specific incident regardless of the casetype
    def delete_one(self, id):
        self.cursor.execute("DELETE FROM redflag WHERE id = %s", (id,))


    # edits a comment of the incident regardless of the casetype 
    def patch_comment(self, id, comment):
        self.cursor.execute(f"UPDATE redflag SET comment = '{comment}' WHERE id = {id}")
        return True


    # edits a location of the incident regardless of the casetype
    def patch_location(self, id, location):
        self.cursor.execute(f"UPDATE redflag SET location='{location}' WHERE id = {id}")
        return True
    
# validation for the redflags
class ValidationRedFlags:
    pass