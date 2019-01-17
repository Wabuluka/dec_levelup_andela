from . import *

"""
    creating a red flag incident
"""
class CreateRedFlagMap(MethodView):
    
    def post(self):
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
        
        red_flag_records.append(red_flag_record.incident_to_dictionary())
        return jsonify({"data": red_flag_record.incident_to_dictionary()})

class GetAllCorruptionMap(MethodView):

    def get(self):
        return jsonify({"data": red_flag_records})

class GetOneCorruptionMap(MethodView):
    
    def get(self, id):
        for record in range(len(red_flag_records)):
            if red_flag_records[record]["id"] == id:
                return jsonify({"status": 200, "data": red_flag_records[record]}), 200
            elif red_flag_records[record]["id"] != id:
                return jsonify({"status": 404, "message": "Red flag was not found"}), 404
            elif record == (len(red_flag_records) -1):
                return jsonify({"status": 404, "message": "Red flag was not found"}), 404

class DeleteRedFlag(MethodView):
    
     def delete(self, id):
        if len(red_flag_records) <1:
            return jsonify({"status":404,"message":"Not Found"  }),404    
        for record in range(len(red_flag_records)):
            if red_flag_records[record]["id"] == id:
                del red_flag_records[record]
                return jsonify({"status": 200, "data": [{"id":id,"message": "Deleted"}] }),200
        return jsonify({"status": 404, "message": "not found"})

class EditStatusMap(MethodView):

    def put(self, id):
        data = request.get_json()
        record = next(filter(lambda x: x['id'] == id, red_flag_records), None)
        if len(red_flag_records) <1:
            return jsonify({"status":404,"message":"Not Found"  }),404    
        for record in range(len(red_flag_records)):
            if red_flag_records[record]["id"] == id:
                red_flag_records[record].update({"status":data["status"]})
                return jsonify({"status": 200, "data": [{"id":id,"message": "edited"}] }),200
        return jsonify({"status": 404, "message": "not found"})

class EditLocationMap(MethodView):

    def put(self, id):
        data = request.get_json()
        record = next(filter(lambda x: x['id'] == id, red_flag_records), None)
        if len(red_flag_records) <1:
            return jsonify({"status":404,"message":"Not Found"  }),404    
        for record in range(len(red_flag_records)):
            if red_flag_records[record]["id"] == id:
                red_flag_records[record].update({"location":data["location"]})
                return jsonify({"status": 200, "data": [{"id":id,"message": "edited"}] }),200
        return jsonify({"status": 404, "message": "not found"})
        

class EditCommentMap(MethodView):

    def put(self, id):
        data = request.get_json()
        record = next(filter(lambda x: x['id'] == id, red_flag_records), None)
        if len(red_flag_records) <1:
            return jsonify({"status":404,"message":"Not Found"  }),404    
        for record in range(len(red_flag_records)):
            if red_flag_records[record]["id"] == id:
                red_flag_records[record].update({"comment":data["comment"]})
                return jsonify({"status": 200, "data": [{"id":id,"message": "edited"}] }),200
        return jsonify({"status": 404, "message": "not found"})