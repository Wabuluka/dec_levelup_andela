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
        red_flag_records.append(red_flag_record.case_dictionary())
        return jsonify({"data": red_flag_record.case_dictionary()})

class GetAllCorruptionMap(MethodView):

    def get(self):
        return jsonify({"data": red_flag_records})

class GetOneCorruptionMap(MethodView):
    
    def get(self, id):
        for record in range(len(red_flag_records)):
            if red_flag_records[record]["id"] == id:
                return jsonify({"status": 200, "data": red_flag_records[record]}), 200
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