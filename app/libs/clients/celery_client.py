from libs.utilites.config import Config
from celery import Celery

storage = Config().storage
CELERY = Celery('tasks',
                backend=storage.get('RedisUrl'),
                broker=storage.get('BrokerUrl')
                )
