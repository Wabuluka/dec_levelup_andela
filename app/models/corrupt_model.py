import datetime
import json

class CorruptionCase:

    # initialization
    def __init__(self, **kwargs):
        # self.id = kwargs[0]
        # self.caseType = kwargs[1]
        # self.createdOn = kwargs[2]
        # self.createdBy = kwargs[3]
        # self.location = kwargs[4]
        # self.status = kwargs[5]
        # self.comment = kwargs[6]
        self.id = kwargs.get("id")
        self.caseType = kwargs.get("caseType")
        self.createdOn = kwargs.get("createOn")
        self.createdBy = kwargs.get("createdBy")
        self.location = kwargs.get("location")
        self.status = kwargs.get("status")
        self.comment = kwargs.get("comment")


    # convert to dictionary
    def incident_to_dictionary(self):
        # if self.caseType == 'redflag':
        #     incident = {
        #         "redflag": [
        #             {
        #                 "id": self.id, 
        #                 "createdOn":datetime.datetime.now(),
        #                 "createdBy":self.createdBy,
        #                 "location":self.location,
        #                 "status":self.status,
        #                 "comment":self.comment
        #             }
        #         ]
        #     }
        #     return incident
                
            
        # elif self.caseType == 'intervention':
        #     incident = {
        #         "intervention": [
        #             {
        #                 "id": self.id, 
        #                 "createdOn":datetime.datetime.now(),
        #                 "createdBy":self.createdBy,
        #                 "location":self.location,
        #                 "status":self.status,
        #                 "comment":self.comment
        #             }
        #         ]
        #     }
        #     return incident
        return {
            "id": self.id, 
            "createdOn":datetime.datetime.now(),
            "createdBy":self.createdBy,
            "caseType" : self.caseType,
            "location":self.location,
            "status":self.status,
            "comment":self.comment
        }