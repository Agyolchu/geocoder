from libs.exceptions.geo_exception import GeoException
from libs.utilites.type_checker import isfloat
from tasks.addresser_task import AddresserTask
from tasks.coordinator_task import CordinateTask
from numbers import Integral


class GeoLocatorService(object):

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

    @staticmethod
    def convert_coordinates_to_address(*args) -> dict:
        if not (all(isfloat(elem) for elem in args) or all(isinstance(elem, Integral) for elem in args)):
            raise GeoException("Latitude or Longitude data type is not correct, must be integer or integer convertible")
        coordinate_task = CordinateTask()
        address = coordinate_task.delay(*args)
        if not address.get():
            return {"error": "Coordinates are not valid"}
        return {"address": address}
