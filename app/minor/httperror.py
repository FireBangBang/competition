from flask import jsonify
from . import minor


class HttpError400(Exception):
    status_code = 400  # Bad Request

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


#  捕捉全局状态码
@minor.app_errorhandler(HttpError400)
def handle_default_http_err_400(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


class HttpError404(Exception):
    status_code = 404  # Not Found

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@minor.app_errorhandler(HttpError404)
def handle_default_http_err_404(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


class HttpError500(Exception):
    status_code = 500  # Internal Server Error

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@minor.app_errorhandler(HttpError500)
def handle_default_http_err_500(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
