from . import *

"""
    creating a red flag incident
"""
class CreateRedFlagMap(MethodView):
    
    def post(self, id):
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
        # redflag = [flag.__dict__ for flag in red_flag_records if flag.__dict__['id']==int(id)]
        # redflag[0]['comment'] = request.get_json['comment']
        # return jsonify({"message":"editted successfully"})
        # data = request.get_json()
        # if len(red_flag_records) <1:
        #     return jsonify({"status":404,"message":"Not Found"  }),404    
        # for record in range(len(red_flag_records)):
        #     if red_flag_records[record]["id"] == id:
        #         # record[0]['comment'] = data['comment']
        #         record.comment = data['comment']
        #         return jsonify({"status": 200, "data": [{"id":id,"message": "edited"}] }),200
        # return jsonify({"status": 404, "message": "not found"})

        data = request.get_json()
        record = next(filter(lambda x: x['id'] == id, red_flag_records), None)
        if len(red_flag_records) <1:
            return jsonify({"status":404,"message":"Not Found"  }),404    
        for record in range(len(red_flag_records)):
            if red_flag_records[record]["id"] == id:
                # record[0]['comment'] = data['comment']
                record.comment = data['comment']
                return jsonify({"status": 200, "data": [{"id":id,"message": "edited"}] }),200
        return jsonify({"status": 404, "message": "not found"})

class EditLocationMap(MethodView):

    def put(self, id):
        # redflag = [flag.__dict__ for flag in red_flag_records if flag.__dict__['id']==int(id)]
        # redflag[0]['comment'] = request.get_json['comment']
        # return jsonify({"message":"editted successfully"})
        # data = request.get_json()
        # if len(red_flag_records) <1:
        #     return jsonify({"status":404,"message":"Not Found"  }),404    
        # for record in range(len(red_flag_records)):
        #     if red_flag_records[record]["id"] == id:
        #         # record[0]['comment'] = data['comment']
        #         record.comment = data['comment']
        #         return jsonify({"status": 200, "data": [{"id":id,"message": "edited"}] }),200
        # return jsonify({"status": 404, "message": "not found"})

        data = request.get_json()
        record = next(filter(lambda x: x['id'] == id, red_flag_records), None)
        if len(red_flag_records) <1:
            return jsonify({"status":404,"message":"Not Found"  }),404    
        for record in range(len(red_flag_records)):
            if red_flag_records[record]["id"] == id:
                # record[0]['comment'] = data['comment']
                record.location = data['location']
                return jsonify({"status": 200, "data": [{"id":id,"message": "edited"}] }),200
        return jsonify({"status": 404, "message": "not found"})