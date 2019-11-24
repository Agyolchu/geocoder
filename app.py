from services.geolocator_service import GeoLocatorService


geolocator = GeoLocatorService()
lat, long = geolocator.convert_address_to_coordinates("H. C. Andersens Blvd. 27, 1553 København V, Denmark")
address = geolocator.convert_coordinates_to_address(lat, long)
print(address)
print(lat, long)
