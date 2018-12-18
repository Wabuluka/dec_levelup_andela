from app import app
from flask import request, jsonify
from flask_restful import Resource, Api

api = Api(app)

@app.route('/hello', methods=['GET'])
def hello():
    return 'hello'