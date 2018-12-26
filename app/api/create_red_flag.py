from flask import jsonify

class RedFlagModel:
    def __init__(self, **kwargs):
        self.flag_id = kwargs['flag_id']
        self.flag_reporter = kwargs['flag_reporter']
        self.headline = kwargs['headline']
        self.description = kwargs['description']
        self.location = kwargs['location']
        self.status = kwargs['status']
        self.dateCreated = kwargs['dateCreated']

class RedFlagModelValidators(RedFlagModel):
    pass