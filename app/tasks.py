from io import BytesIO
from celery import Celery, current_task
from celery.result import AsyncResult

REDIS_URL = 'redis://redis:6379/0'
BROKER_URL = 'amqp://admin:mypass@rabbit//'

CELERY = Celery('tasks', backend=REDIS_URL, broker=BROKER_URL)


@CELERY.task
def add(x, y):
    return x + y
