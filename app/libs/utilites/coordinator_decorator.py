from functools import wraps
from libs.utilites.config import Config
from flask import request


class CoordinateDecorator:
    config = Config()

    @classmethod
    def validate_coordinate_request(cls, func):
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            params = request.args
            keys = params.keys()
            coordinate_parameters = cls.config.storage.get('COORDINATE_REQUEST_PARAMS')
            if not all(item in coordinate_parameters for item in list(keys)):
                return {"message": "please pass only two parameters latitude and longitude with number parameters"}, 500
            return func(*args, **kwargs)

        return wrapped_func

    @classmethod
    def validate_address_request(cls, func):
        @wraps(func)
        def wrapped_f(*args, **kwargs):
            params = request.args
            keys = params.keys()
            address_parameters = cls.config.storage.get('ADDRESS_REQUEST_PARAMS')
            if not all(item in address_parameters for item in list(keys)):
                return {"message": "please pass only single parameter: 'address' "}, 500
            return func(*args, **kwargs)

        return wrapped_f
