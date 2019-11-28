from geopy import Nominatim
from libs.exceptions.geo_exception import GeoException
from libs.utilites.type_checker import isfloat
from libs.clients.celery_client import CELERY
from numbers import Integral


class GeoLocatorService(object):

    def __init__(self):
        self.locator = Nominatim(user_agent="geocoder_app")

    # @CELERY.task()
    def convert_address_to_coordinates(self, address: str) -> (dict, int):
        if not address:
            raise GeoException("Address must be passed")
        coordinate_data = self.locator.geocode(address)
        if not coordinate_data:
            return {"error": "Not proper address"}, 400
        _, (latitude, longitude) = self.locator.geocode(address)
        return {"latitude": latitude, "longitude": longitude}, 200

    # @CELERY.task()
    def convert_coordinates_to_address(self, *args) -> (str, int):
        if not (all(isfloat(elem) for elem in args) or all(isinstance(elem, Integral) for elem in args)):
            raise GeoException("Latitude or Longitude data type is not correct, must be integer or integer convertible")

        address = self.locator.reverse("{}, {}".format(str(args[0]), str(args[1])))
        if not address:
            return "Not proper coordinates", 400
        return address, 200
