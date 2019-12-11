from geopy import Nominatim

from tasks.tasks_base import TaskBase
from app_settings import celery


class CordinateTask(TaskBase):
    def __init__(self, *args, **kwargs):
        super(CordinateTask, self).__init__(*args, **kwargs)
        self.locator = Nominatim(user_agent="geocoder_app")

    def run(self, *args):
        coordinate_address = self.locator.reverse("{}, {}".format(str(args[0]), str(args[1])))
        return coordinate_address


celery.register_task(CordinateTask())
