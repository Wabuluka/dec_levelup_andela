from flask import Flask, jsonify, request, json
from flask.views import MethodView

from app.models.corrupt_model import CorruptionCase
from app.models.usr_model import UserModel
red_flag_records = []
count = 0

class GetAllCorruptionMap(MethodView):
    def get(self, id):
        if id is None:
            if len(red_flag_records) < 1:
                return jsonify({"status":404,"message":"Not Found" }),404
            else:
                return jsonify({"status":200 ,"data": red_flag_records}),200
    
        else:
            for index in range(len(red_flag_records)):
                if red_flag_records[index]["id"] == id:
                     return jsonify({"status":200,"data":red_flag_records[index] }),200
                elif index == (len(red_flag_records) -1):
                    return jsonify({"status": 404, "message": "Not Found"}), 404

            if len(red_flag_records) < 1:
                return jsonify({"status": 404, "message": "Not Found"})