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

    def get(self, id=None):
        if id:
            get_one = incidentmodel.get_one_incident(id)
            return jsonify({"status": 200, "data":[get_one]})
        get_all = incidentmodel.get_all_incidents()
        return jsonify({"status": 200, "data":[get_all]})

    def delete(self, id):
        incidentmodel.delete_incident(id)
        return jsonify({"status": 200, "message": "Deleted "})

    def patch_comment(self, id):
        patched_comment = data[incidentmodel.patch_comment_intervention(id, comment)]
        return jsonify({"status": 200,"data": [patched_comment] })

    def patch_location(self, id):
        patched_location = data[incidentmodel.patch_comment_intervention(id, location)]
        return jsonify({"status": 200,"data": [patched_location] })