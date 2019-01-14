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
        self.videos = kwargs.get("videos")
        self.images = kwargs.get("images")
        self.comment = kwargs.get("comment")


    # convert to dictionary
    def case_dictionary(self):
        return {
            "id": self.id, 
            "createdOn":self.createdOn,
            "createdBy":self.createdBy,
            "caseTypes":self.caseType,
            "location":self.location,
            "status":self.status,
            "images":self.images,
            "videos":self.videos,
            "comment":self.comment
            }

   