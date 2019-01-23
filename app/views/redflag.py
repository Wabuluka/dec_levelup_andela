from flask import Blueprint, request, jsonify
from app.model.redflag import RedFlag

redflagmodel = RedFlag()

redflag = Blueprint('redflag', __name__)

@redflag.route('/red-flags', methods=['POST'])
def create_redflag():
    if request.content_type != 'application/json':
        return jsonify({ "status": "404", "message": "Change content_type to json" })
        
    data = request.get_json()
    
    createdby = data['createdby']
    casetype = 'red-flag'
    location = data['location']
    status = data['status']
    comment = data['comment']
    
    
    new_record = RedFlag(createdby=createdby, casetype=casetype, location=location, status=status, comment=comment)

    redflagmodel.create_redflag(new_record)
    return jsonify({"status": 200, "message": "Created success"})


@redflag.route('/red-flags', methods=["GET"])
def get_all():
    get_all = redflagmodel.get_all()
    return jsonify({"status": 200, "data":[get_all]})

@redflag.route('/red-flags/<int:id>', methods=["GET"])
def get_one(id):
    get_one = redflagmodel.get_one(id)
    return jsonify({"status": 200, "data":[get_one]})

@redflag.route('/red-flags/<int:id>', methods=["DELETE"])
def delete_one(id):
    redflagmodel.delete_one(id)
    return jsonify({"status": 200, "message": "Deleted "})

@redflag.route('/red-flags/<int:id>/location', methods = ["PATCH"])
def edit_location(id):
    data = request.get_json()
    location = data["location"]
    edit = redflagmodel.patch_location(id, location)
    if edit:
        return jsonify({"status": 200,"data": location, "message": "Updated intervention location" })
    return jsonify({"status": 400, "Error": "Failed redflag location" }),400

@redflag.route('/red-flags/<int:id>/comment', methods = ["PATCH"])
def edit_comment(id):
    data = request.get_json()
    comment = data["comment"]
    edit = redflagmodel.patch_comment(id, comment)
    if edit:
        return jsonify({"status": 200,"data": comment, "message": "Updated intervention location" })
    return jsonify({"status": 400, "Error": "Failed redflag location" }),400