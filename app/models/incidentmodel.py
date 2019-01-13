from datetime import datetime
from flask import jsonify

class IncidentModel:
    """
        a model for the incidents created
    """
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.createdby = kwargs.get('createdby')
        self.incident = kwargs.get('incident')
        self.incidenttype = kwargs.get('type')
        self.incidentlocation = kwargs.get('incidentlocation')
        self.incidentcomment = kwargs.get('incidentcomment')
        self.createdon = kwargs.get(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.status = "unresolved"

    def incident_classification(self):
        if self.incidenttype == 'redflag':
            redflag = {
                "id" : self.id,
                "createdby" : self.createdby,
                "incident" : self.incident,
                "incidenttype" : "redflag",
                "incidentlocation" : self.incidentlocation,
                "createdon" : self.createdon,
                "status" : self.status
            }
            return redflag
        elif self.incidenttype == 'intervention':
            intervention = {
                "id" : self.id,
                "createdby" : self.createdby,
                "incident" : self.incident,
                "incidenttype" : "intervention",
                "incidentlocation" : self.incidentlocation,
                "createdon" : self.createdon,
                "status" : self.status  
            }
            return intervention
        else:
            return jsonify(
                {
                    "status": 400, 
                    "message": "the incident provided is not correct."
                    }
                    )

        