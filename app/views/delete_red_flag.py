from . import *

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