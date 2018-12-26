from app import app
from flask import request, jsonify
from flask_restful import Resource, Api

from .api import AllValidators
from .api.create_red_flag import RedFlagModel


api = Api(app)

red_flag_records = []

@app.route('/hello', methods=['GET'])
def hello():
    return 'hello'

class RedFlagRecords():
    def get(self):
        if red_flag_records == None:
            return  jsonify({
            'message': 'There are no red flags yet.'
            }), 400
        else:
            return jsonify({
                'Records': [red_flag_record for red_flag_record in red_flag_records]
            }), 201


api.add_resource(RedFlagRecords, '/')