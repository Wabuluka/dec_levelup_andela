from flask import Blueprint, request, jsonify
from app.model.intervention import Intervention
from app.utilities.helpers import token_required

interventionmodel = Intervention()

intervention = Blueprint('intervention', __name__)


@token_required
@intervention.route('/interventions', methods=['POST'])
def create_intervention():

    data = request.get_json()
    
    createdby = data['createdby']
    casetype = 'intervention'
    location = data['location']
    status = data['status']
    comment = data['comment']
    
    
    new_record = Intervention(createdby=createdby, casetype=casetype, location=location, status=status, comment=comment)

    interventionmodel.create_intervention(new_record)
    return jsonify({"status": 200, "message": "Created success"}),200

@intervention.route('/interventions', methods=["GET"])
@token_required
def get_all():
    get_all = interventionmodel.get_all()
    if get_all:
        return jsonify({"status": 200, "message": "success", "data":[get_all]}),200
    return jsonify({"status": 404, "message": "there are no interventions"}),404

@intervention.route('/interventions/<int:id>', methods=["GET"])
@token_required
def get_one(id):
    if id:
        get_one = interventionmodel.get_one(id)
        return jsonify({"status": 200, "message": "success","data":[get_one]}),200
    return jsonify({"status": 404, "message": "not found"}),404

@intervention.route('/interventions/<int:id>', methods=["DELETE"])
@token_required
def delete_one(id):
    interventionmodel.delete_one(id)
    return jsonify({"status": 200, "message": "Deleted "})

@intervention.route('/interventions/<int:id>/location', methods = ["PATCH"])
@token_required
def edit_location(id):
    data = request.get_json()
    location = data["location"]
    edit = interventionmodel.patch_location_intervention(id, location)
    if edit:
        return jsonify({"status": 200,"data": location, "message": "Updated intervention location" })
    return jsonify({"status": 400, "Error": "Failed redflag location" }),400

@intervention.route('/interventions/<int:id>/comment', methods=["PATCH"])
@token_required
def edit_comment(id):
    data = request.get_json()
    comment = data["comment"]
    edit = interventionmodel.patch_comment_intervention(id, comment)
    if edit:
        return jsonify({"status": 200,"data": comment, "message": "Updated intervention comment" })
    return jsonify({"status": 400, "Error": "Failed redflag location" }),400