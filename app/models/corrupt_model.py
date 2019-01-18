import datetime
import json

class CorruptionCase:

    # initialization
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.caseType = kwargs.get("caseType")
        self.createdOn = kwargs.get("createOn")
        self.createdBy = kwargs.get("createdBy")
        self.location = kwargs.get("location")
        self.status = kwargs.get("status")
        self.comment = kwargs.get("comment")


    # convert to dictionary
    def incident_to_dictionary(self):
        return {
            "id": self.id, 
            "createdOn":datetime.datetime.now(),
            "createdBy":self.createdBy,
            "caseType" : self.caseType,
            "location":self.location,
            "status":self.status,
            "comment":self.comment
        }