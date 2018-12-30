from flask import Flask, jsonify
class RedFlag():
    
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.createdBy = kwargs['createdBy']
        self.title = kwargs['title']
        self.location = kwargs['location']
        self.comment = kwargs['comment']
        self.status = kwargs['status']
        self.createdOn = kwargs['createdOn']

    def splitName(self, lastName, firstName):
        pass

    def validate_id(self, id):
        try:
            convert_id = int(id)
            
        except:
            return jsonify({"status": 400, "error":"The id must be a non negative integer"}),400

        if convert_id < 0:
            return jsonify({"status": 400, "error":"The id cannot be negative"}),400
        return True