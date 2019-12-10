from time import sleep

from geopy import Nominatim
from libs.exceptions.geo_exception import GeoException
from libs.utilites.type_checker import isfloat
from tasks.addresser_task import AddresserTask
from app_settings import celery
from numbers import Integral



class GeoLocatorService(object):

    def __init__(self):
        self.locator = Nominatim(user_agent="geocoder_app")

    @staticmethod
    def convert_address_to_coordinates(address: str) -> dict:
        if not address:
            raise GeoException("Address must be passed")
        address_task = AddresserTask()
        coordinates_data = address_task.delay(address)
        if not coordinates_data.get():
            return {"error": "Not proper address"}
        _, (latitude, longitude) = coordinates_data
        return {"latitude": latitude, "longitude": longitude}

    @celery.task(bind=True, name='GeoLocatorService.convert_coordinates_to_address')
    def convert_coordinates_to_address(self, *args) -> dict:
        if not (all(isfloat(elem) for elem in args) or all(isinstance(elem, Integral) for elem in args)):
            raise GeoException("Latitude or Longitude data type is not correct, must be integer or integer convertible")

        address = self.locator.reverse("{}, {}".format(str(args[0]), str(args[1])))
        if not address:
            return {"error": "Coordinates are not valid"}
        return {"address": address}
