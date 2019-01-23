from flask import Blueprint, request, jsonify
from app.model.user import UserModel

admin = Blueprint('users', __name__)
usermodel = UserModel()

@admin.route('/red-flags/<int:id>/status')
def redflag_edit_status():
   pass