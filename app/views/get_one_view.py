from . import *


class GetOneCorruptionMap(MethodView):
    
    def get(self):
        for index in range(len(red_flag_records)):
            if red_flag_records[index]["id"] == id:
                return jsonify({"status": 200, "data": red_flag_records[index]}), 200
            elif index == (len(red_flag_records) -1):
                return jsonify({"status": 404, "message": "Red flag was not found"}), 404