from flask import Flask, jsonify, request, json
from flask.views import MethodView

from app.models.corrupt_model import CorruptionCase
from app.models.usr_model import UserModel
red_flag_records = []
count = 0

class PostCorruptionMap(MethodView):
    def post(self):
        data = request.get_json()
        global count
        verify = CorruptionCase.created_by_validation(data['createdBy'])
        print(verify)
        if verify == True:
            count +=1
            red_flag_record = CorruptionCase(count,data["id"],data["createdBy"],data["caseType"],data["location"],data["status"],data["images"],data["videos"],data["comment"])
            red_flag_records.append(red_flag_record.case_dictionary())
            return jsonify({"status": 201,"data":[{"id":red_flag_record.id,"message":"Created red-flag record"}] }) ,201
        
        else:
            return jsonify({"status":400,"message": "No input provided"}),400