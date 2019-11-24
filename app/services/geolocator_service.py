from geopy import Nominatim


class GeoLocatorService(object):

    def __init__(self):
        self.locator = Nominatim(user_agent="geocoder_app")

    def convert_address_to_coordinates(self, address: str) -> (int, int):
        _, (latitude, longitude) = self.locator.geocode(address)
        return latitude, longitude

    def convert_coordinates_to_address(self, latitude: int, longitude: int) -> str:
        address = self.locator.reverse("{}, {}".format(latitude, longitude))
        return address
