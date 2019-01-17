from flask import abort
from app import app

@app.errorhandler
def default_error_handler(error):
    """Returns Internal server error"""
    error = ServerError()
    return error.to_dict(), getattr(error, 'code', 500)

class BaseError(Exception):
    """Base Error Class"""

    def __init__(self, code=400, message='', status='', field=None):
        Exception.__init__(self)
        self.code = code
        self.message = message
        self.status = status
        self.field = field

    def to_dict(self):
        return {
            'code': self.code,
            'message': self.message,
            'status': self.status,
            'field': self.field, 
                }
class NotFoundError(BaseError):
    def __init__(self, message='Not found'):
        BaseError.__init__(self)
        self.code = 404
        self.message = message
        self.status = 'NOT_FOUND'


class NotAuthorizedError(BaseError):
    def __init__(self, message='Unauthorized'):
        BaseError.__init__(self)
        self.code = 401
        self.message = message
        self.status = 'NOT_AUTHORIZED'


class ValidationError(BaseError):
    def __init__(self, field, message='Invalid field'):
        BaseError.__init__(self)
        self.code = 400
        self.message = message
        self.status = 'INVALID_FIELD'
        self.field = field

class ServerError(BaseError):
    def __init__(self, message='Internal server error'):
        BaseError.__init__(self)
        self.code = 500
        self.message = message
        self.status = 'SERVER_ERROR'

@app.errorhandler(NotFoundError)
@app.errorhandler(NotAuthorizedError)
@app.errorhandler(ValidationError)
# @app.errorhandler(InvalidServiceError)
def handle_error(error):
    return error.to_dict(), getattr(error, 'code')