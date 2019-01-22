from . import *
"""
    creating an intervention red flag incident
"""
incidentmodel = CorruptionCase()
class InterventionViewMap(MethodView):

    def post(self):
        data = request.get_json()
        
        createdby = data['createdby']
        casetype = 'intervention'
        location = data['location']
        status = data['status']
        comment = data['comment']
        
        
        new_record = CorruptionCase(createdby=createdby, casetype=casetype, location=location, status=status, comment=comment)

        incidentmodel.create_intervention(new_record)
        return jsonify({"status": 200, "message": "Created success"})

    def get(self, id = None):
        if id:
            get_one = incidentmodel.get_one_intervention(id)
            return jsonify({"status": 200, "data":[get_one]})
        get_all = incidentmodel.get_all_interventions()
        return jsonify({"status": 200, "data":[get_all]})

    def delete(self, id):
        incidentmodel.delete_intervention(id)
        return jsonify({"status": 200, "message": "Deleted "})

    def patch(self, id, comment, location):
        data = request.get_json()
        if comment:
            patched_comment = data[incidentmodel.patch_comment_intervention(id, comment)]
            return jsonify({"status": 200,"data": [patched_comment] })
        elif location:
            patched_location = incidentmodel.patch_location_intervention(id, location)
            return jsonify({"status": 200, "data": [patched_location]})