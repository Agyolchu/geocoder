from functools import wraps
from libs.utilites.config import Config
from flask import request


class CoordinateDecorator:
    config = Config()

    @staticmethod
    def validate_coordinate_request(func):
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            params = request.get_json()
            keys = params.keys()
            if not list(keys) == CoordinateDecorator.config.storage.get('CoordinateRequestParams'):
                return {"message": "please pass only two parameters latitude and longitude with number parameters"}, 500
            return func(*args, **kwargs)

        return wrapped_func

    @staticmethod
    def validate_address_request(func):
        @wraps(func)
        def wrapped_f(*args, **kwargs):
            params = request.get_json()
            keys = params.keys()
            if not list(keys) == CoordinateDecorator.config.storage.get('AddressRequestParams'):
                return {"message": "please pass only single parameters address"}, 500
            return func(*args, **kwargs)

        return wrapped_f
