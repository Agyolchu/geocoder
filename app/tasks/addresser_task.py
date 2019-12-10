from geopy import Nominatim

from tasks.tasks_base import TaskBase
from app_settings import celery


class AddresserTask(TaskBase):
    def __init__(self, *args, **kwargs):
        super(AddresserTask, self).__init__(*args, **kwargs)
        self.locator = Nominatim(user_agent="geocoder_app")

    def run(self, address: str):
        coordinate_data = self.locator.geocode(address)
        return coordinate_data


celery.register_task(AddresserTask())
