from flask import Flask, jsonify, request, json
from flask.views import MethodView

from app.models.corrupt_model import CorruptionCase
from app.models.usr_model import UserModel
red_flag_records = []
count = 0

class PostCorruptionMap(MethodView):
    def post(self):
        data = request.get_json()
        red_flag_record = CorruptionCase(
            id = data['id'],
            caseType = data['caseType'],
            createdOn = data['createdOn'],
            createdBy = data['createdBy'],
            location = data['location'],
            status =data['status'],
            videos =data['videos'],
            images =data['images'],
            comment =data['comment']
        )
        red_flag_records.append(red_flag_record)
        return jsonify({"data": red_flag_record.case_dictionary()})
