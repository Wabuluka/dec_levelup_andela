from flask import Blueprint, request, jsonify
import jwt
from functools import wraps
from app.model.redflag import RedFlag, ValidationRedFlags
from app.utilities.helpers import token_required

redflagmodel = RedFlag()
valid = ValidationRedFlags()

def token_req(end_point):
    @wraps(end_point)
    def check(*args, **kwargs):
        if 'token' in request.headers:
            tk = request.headers['token']
        else:
            return jsonify({'message': 'you should login'})
        try:
            jwt.decode(tk, 'wabuluka')
        except:
            return jsonify({'message': 'user not authenticated'})
        return end_point(*args, **kwargs)
    return check


redflag = Blueprint('redflag', __name__)

@redflag.route('/red-flags', methods=['POST'])
@token_req
def create_redflag():
    if request.content_type != 'application/json':
        return jsonify({ "status": "404", "message": "Change content_type to json" })

    keys = ("createdby","location","status","comment")
    if not set(keys).issubset(set(request.json)):
        return jsonify({"message":"all fields are required"})
        
    data = request.get_json()
    
    createdby = data['createdby']
    casetype = 'red-flag'
    location = data['location']
    status = data['status']
    comment = data['comment']
    
    val = valid.validate_redflag(createdby,casetype,location,status,comment)
    if val:
        return val
    
    new_record = RedFlag(createdby=createdby, casetype=casetype, location=location, status=status, comment=comment)

    redflagmodel.create_redflag(new_record)
    return jsonify({"status": 201, "message": "Created success"}), 201


@redflag.route('/red-flags', methods=["GET"])
@token_req
def get_all():
    get_all = redflagmodel.get_all()
    if get_all:
        return jsonify({"status": 200, "message":"success", "data":[get_all]})
    return jsonify({"message":"there are no redflags"})

@redflag.route('/red-flags/<int:id>', methods=["GET"])
@token_req
def get_one(id):
    get_one = redflagmodel.get_one(id)
    if get_one:
        return jsonify({"status": 200, "message":"success", "data":[get_one]}), 200
    return jsonify({"message":"first post redflags"}), 404

@redflag.route('/red-flags/<int:id>', methods=["DELETE"])
@token_req
def delete_one(id):
    redflagmodel.delete_one(id)
    return jsonify({"status": 200, "message": "Deleted"})

@redflag.route('/red-flags/<int:id>/location', methods = ["PATCH"])
@token_req
def edit_location(id):
    data = request.get_json()
    location = data["location"]
    edit = redflagmodel.patch_location(id, location)
    if edit:
        return jsonify({"status": 200,"data": location, "message": "Updated intervention location" })
    return jsonify({"status": 400, "Error": "Failed redflag location" }),400

@redflag.route('/red-flags/<int:id>/comment', methods=["PATCH"])
@token_req
def edit_comment(id):
    data = request.get_json()
    
    comment = data["comment"]
    edit = redflagmodel.patch_comment(id, comment)
    if edit:
        return jsonify({"status": 200,"data": comment, "message": "Updated intervention location" })
    return jsonify({"status": 400, "Error": "Failed redflag location" }),400