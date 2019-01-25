from flask import Blueprint, request, jsonify
from app.model.user import UserModel
from app.model.intervention import Intervention
from app.model.redflag import RedFlag

admin = Blueprint('admin', __name__)
usermodel = UserModel()
interventionmodel = Intervention()
redflagmodel = RedFlag()

@admin.route('/red-flags/<int:id>/status', methods=["PATCH"])
def redflag_edit_status(id):
    
    data = request.get_json()
    status = data["status"]
    edit = redflagmodel.patch_redflag_status(id, status)
    if edit:
        return jsonify({"status": 200,"data": status, "message": "Updated intervention comment" })
    return jsonify({"status": 400, "Error": "Failed redflag location" }),400

@admin.route('/interventions/<int:id>/status', methods=["PATCH"])
def intervention_edit_status(id):
    data = request.get_json()
    status = data["status"]
    edit = interventionmodel.patch_redflag_status(id, status)
    if edit:
        return jsonify({"status": 200,"data": status, "message": "Updated intervention comment" })
    return jsonify({"status": 400, "Error": "Failed redflag location" }),400