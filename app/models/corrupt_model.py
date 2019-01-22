from app.models.db_conn import DatabaseConnection
import datetime
import json

cursor = DatabaseConnection().cursor

class CorruptionCase:

    # initialization
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.casetype = kwargs.get("casetype")
        self.createdby = kwargs.get("createdby")
        self.location = kwargs.get("location")
        self.status = kwargs.get("status")
        self.comment = kwargs.get("comment")
        self.cursor = cursor


    # convert to dictionary
    def incident_to_dictionary(self):
        return {
            "id": self.id, 
            "createdon":datetime.datetime.now(),
            "createdBy":self.createdby,
            "casetype" : self.casetype,
            "location":self.location,
            "status":self.status,
            "comment":self.comment
        }
    # -------------------------------------------redflag-----------------------------------------------_
    def create_incident(self, flag):
        self.cursor.execute("INSERT INTO redflag(casetype, createdby, location, comment, status)"
                            " VALUES(%s,%s,%s,%s, %s)", (flag.casetype, flag.createdby, flag.location,
                                                                flag.comment, flag.status
                                                                ))


    # gets all the incidents regardless of the casetype
    def get_all_incidents(self):
        self.cursor.execute("SELECT * FROM redflag")
        return self.cursor.fetchall()


    # gets a specific incident by id regardless of the casetype
    def get_one_incident(self, id):
        self.cursor.execute("SELECT * FROM redflag WHERE id =%s", (id,))
        return self.cursor.fetchone()


    # deletes a specific incident regardless of the casetype
    def delete_incident(self, id):
        self.cursor.execute("DELETE FROM redflag WHERE id = %s", (id,))


    # edits a comment of the incident regardless of the casetype 
    def patch_comment(self, id, comment):
        self.cursor.execute("UPDATE comment FROM redflag WHERE id %s", (id, comment))
        self.cursor.execute("SELECT * FROM redflag WHERE id=%s", (id,))
        return self.cursor.fetchone()


    # edits a location of the incident regardless of the casetype
    def patch_location(self, id, location):
        self.cursor.execute("UPDATE location FROM redflag WHERE id %s", (id, location))
        self.cursor.execute("SELECT * FROM redflag WHERE id=%s", (id,))
        return self.cursor.fetchone()

    # ---------------------------------------------intervention---------------------------------------------
    def create_intervention(self, flag):
        self.cursor.execute("INSERT INTO intervention(casetype, createdby, location, comment, status)"
                            " VALUES(%s,%s,%s,%s, %s)", (flag.casetype, flag.createdby, flag.location,
                                                                flag.comment, flag.status
                                                                ))
    # get all interventions
    def get_all_interventions(self):
        self.cursor.execute("SELECT * FROM intervention")
        return self.cursor.fetchall()

    # gets a specific intervention by id regardless of the casetype
    def get_one_intervention(self, id):
        self.cursor.execute("SELECT * FROM intervention WHERE id =%s", (id,))
        return self.cursor.fetchone()

    # deletes a specific intervention regardless of the casetype
    def delete_intervention(self, id):
        self.cursor.execute("DELETE FROM intervention WHERE id = %s", (id,))

    # edits a comment of the incident regardless of the casetype 
    def patch_comment_intervention(self, id, comment):
        self.cursor.execute("UPDATE comment FROM intervention WHERE id %s", (id, comment))
        self.cursor.execute("SELECT * FROM intervention WHERE id=%s", (id,))
        return self.cursor.fetchone()


    # edits a location of the incident regardless of the casetype
    def patch_location_intervention(self, id, location):
        self.cursor.execute("UPDATE location FROM intervention WHERE id %s", (id, location))
        self.cursor.execute("SELECT * FROM intervention WHERE id=%s", (id,))
        return self.cursor.fetchone()