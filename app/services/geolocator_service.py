from libs.exceptions.geo_exception import GeoException
from libs.utilites.type_checker import isfloat
from tasks import tasks


class GeoLocatorService(object):
    @staticmethod
    def convert_address_to_coordinates(address: str) -> dict:
        if not address:
            raise GeoException("Address must be passed")
        task = tasks.addresser_task.apply_async(kwargs={"address": address}, queue="celery")
        result = task.get()
        if not result:
            return {"error": "Not proper address"}
        return {"latitude": result.get("lat"), "longitude": result.get("lon")}

    @staticmethod
    def convert_coordinates_to_address(lat: float, long: float) -> dict:
        if not isfloat(lat) or not isfloat(long):
            raise GeoException("Latitude or Longitude data type is not correct, must be integer or integer convertible")
        task = tasks.coordinate_task.apply_async(kwargs={"lat": lat, "long": long}, queue="celery")
        result = task.get()
        if not result:
            return {"error": "Coordinates are not valid"}
        return {"address": result.get("display_name")}
