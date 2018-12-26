from flask import jsonify
from .create_red_flag import RedFlagModel

class AllValidators:
    def validate_content_type(self, contentType):
        if contentType == 'application/json':
            return True
        return jsonify({"status":400, "error":"The content type must be json"}), 400