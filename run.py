from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

red_flag_records = []

class RedFlagRecord(Resource):
    def get(self):
        return {'Red Flags': red_flag_records}


    def post(self, red_flag_id):
        self.red_flag_id = red_flag_id
        if next(filter(lambda x: x['red_flag_id'] == red_flag_id, red_flag_records), None) is not None:
            return {'error': "Red Flad ID '{}' already exists" .format(red_flag_id)}, 400

        data = request.get_json()

        red_flag_record = {
            "red_flag_id": red_flag_id,
            "red_flag_reporter": data['red_flag_reporter'],
            "red_flag_headline": data['red_flag_headline'],
            "red_flag_location": data['red_flag_location'],
            "red_flag_description": data['red_flag_description'],
            "red_flag_status": data["red_flag_status"],
            "red_flag_date_reported": data['red_flag_date_reported']
        }
        red_flag_records.append(red_flag_record)
        return red_flag_record, 201







api.add_resource(RedFlagRecord, '/<int:red_flag_id>')

if __name__ == '__main__':
    app.run(debug=True)