from . import *

"""
    creating a red flag incident
"""
incidentmodel = CorruptionCase()

class IncidentViewMap(MethodView):
     
    def post(self):
        # if request.content_type != 'application/json':
        #     return jsonify({ "status": "404", "message": "Change content_type to json" })
        
        data = request.get_json()
        
        createdby = data['createdby']
        casetype = 'red-flag'
        location = data['location']
        status = data['status']
        comment = data['comment']
        
        
        new_record = CorruptionCase(createdby=createdby, casetype=casetype, location=location, status=status, comment=comment)

        incidentmodel.create_incident(new_record)
        return jsonify({"status": 200, "message": "Created success"})