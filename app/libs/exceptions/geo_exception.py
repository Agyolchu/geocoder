class GeoException(Exception):

    def __init__(self, message, code=500):
        super(GeoException, self).__init__(message)
        self.message = message
        self.code = code

    def to_dict(self) -> [dict, int]:
        return {'message': self.message}, self.code
