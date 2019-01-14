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
            id = data['id'],
            createdBy = data['createdBy'],
            caseType = data['caseType'],
            location = data['location'],
            status = data['status'],
            image = data['image'],
            video = data['video'],
            comment = data['comment']
        )
        red_flag_records.append(red_flag_record.case_dictionary())
        return jsonify({"data": red_flag_record.case_dictionary()})

class GetAllCorruptionMap(MethodView):
    def get(self, id):
        if id is None:
            if len(red_flag_records) < 1:
                return jsonify({"status":404,"message":"Resource does not exist" }),404
            data =red_flag_records
            return jsonify({"status":200 ,"data": data}),200
        else:
            for index in range(len(red_flag_records)):
                if red_flag_records[index]["id"]== id: 
                    return jsonify({"status":200,"data":red_flag_records[index] }),200
                elif index == (len(red_flag_records) -1):
                    return jsonify({"status":404,"message":"Resource does not exist" }) ,404

    
            if len(red_flag_records) <1:
                return jsonify({"status":404,"message":"Resource does not exist"  }),404
        # data = red_flag_records
        # return jsonify({"data": data})

class GetOneCorruptionMap(MethodView):
    
    def get(self):
        for index in range(len(red_flag_records)):
            if red_flag_records[index]["id"] == id:
                return jsonify({"status": 200, "data": red_flag_records[index]}), 200
            elif index == (len(red_flag_records) -1):
                return jsonify({"status": 404, "message": "Red flag was not found"}), 404

class DeleteRedFlag(MethodView):
    
     def get(self, id):
        if len(red_flag_records) <1:
            return jsonify({"status":404,"message":"Not Found"  }),404    


        for index in range(len(red_flag_records)):
            if  red_flag_records[index]["id"]== id: 
                del red_flag_records[red_flag_records.index(red_flag_records[index])]
                return jsonify({"status":200,"data": [{"id":id,"message": "Deleted"}] }),200
            elif index == (len(red_flag_records) -1):
                return jsonify({"status":404,"message":"Not Found" }),404