from app.model.db import DatabaseConnection
import datetime
import json

cursor = DatabaseConnection().cursor

class Intervention:

   # initialization
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.casetype = kwargs.get("casetype")
        self.createdby = kwargs.get("createdby")
        self.location = kwargs.get("location")
        self.status = kwargs.get("status")
        self.comment = kwargs.get("comment")
        self.cursor = cursor


    # creating the intervention
    def create_intervention(self, flag):
        self.cursor.execute("INSERT INTO intervention(casetype, createdby, location, comment, status)"
                            " VALUES(%s,%s,%s,%s, %s)", (flag.casetype, flag.createdby, flag.location,
                                                                flag.comment, flag.status
                                                                ))
    # get all interventions
    def get_all(self):
        self.cursor.execute("SELECT * FROM intervention")
        return self.cursor.fetchall()


    # gets a specific intervention by id regardless of the casetype
    def get_one(self, id):
        self.cursor.execute("SELECT * FROM intervention WHERE id =%s", (id,))
        return self.cursor.fetchone()


    # deletes a specific intervention regardless of the casetype
    def delete_one(self, id):
        self.cursor.execute("DELETE FROM intervention WHERE id = %s", (id,))


    # edits a comment of the incident regardless of the casetype 
    def patch_comment_intervention(self, id, comment):
        self.cursor.execute(f"UPDATE intervention SET comment = '{comment}' WHERE id = {id}")
        return True


    # edits a location of the incident regardless of the casetype
    def patch_location_intervention(self, id, location):
        self.cursor.execute(f"UPDATE intervention SET location='{location}' WHERE id = {id}")
        return True


class InvertentionValidation:
    pass