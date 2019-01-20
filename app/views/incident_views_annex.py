from . import *
"""
    creating a red flag incident
"""
class IncidentViewMap(MethodView):
    def post(self):
        if request.content_type != 'application/json':
            return jsonify({ "status": "404", "message": "Change content_type to json" })
        
        # data = json_fetcher()
        data = request.get_json()
        global count

        count +=1
        red_flag_record = CorruptionCase(
            id = len(red_flag_records) + 1,
            createdBy = data['createdBy'],
            caseType = data['caseType'],
            location = data['location'],
            status = data['status'],
            createdon = date.today(),
            comment = data['comment']
        )
        # red_flag_record.createdBy = str()
        if not red_flag_record.createdBy or not red_flag_record.caseType or not red_flag_record.location or not red_flag_record.status or not red_flag_record.comment:
            return jsonify({
                "status": 400,
                "message": "No specified field can be left open(bad request)"
            }), 400
        if not isinstance(red_flag_record.comment, str):
            return jsonify({
                "status": 400,
                "message": "The comment should be of type string"
            }), 400

        if not isinstance(red_flag_record.createdBy, str):
            return jsonify({
                "status": 400,
                "message": "The username should be of type string"
            }), 400


        red_flag_records.append(red_flag_record.incident_to_dictionary())
        return jsonify({"status": 200, "message": "Created red-flag record" , "data" : [red_flag_record.incident_to_dictionary()]}), 200

    def get(self):
        """
            retrieve incidents or an incident as defined by the url
        """
        if len(red_flag_records) ==0:
            return jsonify({"status": 200, "message": "Your API is working well but we did not find any records that match your request"})
        else:
            return jsonify({"status": 404, "data": [red_flag_records]})

    def delete(self, id):
        """
            delete a specified incident by Id
        """
        if len(red_flag_records) <1:
            return jsonify({"status":404,"message":"Not Found"  }),404    
        for record in range(len(red_flag_records)):
            if red_flag_records[record]["id"] == id:
                del red_flag_records[record]
                return jsonify({"status": 200, "data": [{"id":id,"message": "Deleted"}] }),200
        return jsonify({"status": 404, "message": "not found"})