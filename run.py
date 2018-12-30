from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from engine import RedFlag

app = Flask(__name__)
api = Api(app)

red_flag_records = []

class RedFlagRecord(Resource):
    def get(self):
        return {'Red Flags': red_flag_records}


    def post(self, id):
        self.id = id
        if next(filter(lambda x: x['id'] == id, red_flag_records), None) is not None:
            return {'error': "Red Flad ID '{}' already exists" .format(id)}, 400

        data = request.get_json()

        red_flag_record = {
            "id": id,
            "createdBy": data['createdBy'],
            "title": data['title'],
            "location": data['location'],
            "comment": data['comment'],
            "status": data["status"],
            "createdOn": data['createdOn']
        }
        red_flag_records.append(red_flag_record)
        return jsonify({"status":200, "message":"Created red-flag record", "Red Flag": [red_flag_record]})







api.add_resource(RedFlagRecord, '/api/v1/redflags/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)