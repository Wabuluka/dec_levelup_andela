from flask import jsonify, request, json
from flask.views import MethodView
from app.models.incidentmodel import IncidentModel

incidents = []

class CreateViews(MethodView):
    
    def create_incident(self):
        data = request.get_json()

        incident = IncidentModel(
            id = data['id'],
            createdby = data['createdby'],
            incident = data['incident'],
            incidenttype = data['redflag'],
            incidentlocation = data['incidentlocation'],
            createdon = data['createdon'],
            status = data['status']
        )
        incidents.append(incident.incident_classification())
        return jsonify({"status": 200, "message": "created a new incident", "data": incident})

