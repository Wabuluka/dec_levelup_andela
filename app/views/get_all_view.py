from . import *


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