from geopy import Nominatim

from libs.clients.celery_client import celery


@celery.task()
def addresser_task(address: str):
    """Address -> Coordinates."""
    locator = Nominatim(user_agent="geocoder_app")
    coordinate_data = locator.geocode(address)
    return coordinate_data.raw


@celery.task()
def coordinate_task(lat, long):
    """Coordinates -> Address."""
    locator = Nominatim(user_agent="geocoder_app")
    coordinate_address = locator.reverse(f"{lat}, {long}")
    return coordinate_address.raw
