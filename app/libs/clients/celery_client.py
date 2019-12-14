from libs.utilites.config import Config
from celery import Celery
from flask import Flask

storage = Config().storage


def make_celery(app=None):
    broker_url = storage.get('CELERY_BROKER_URL')
    redis_url = storage.get('REDIS_URL')
    if not app:
        app = Flask(__name__)
    celery = Celery(app.import_name, broker=broker_url, backend=redis_url)
    celery.conf.update(app.config)
    TaskOrigin = celery.Task

    class ContextTask(TaskOrigin):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskOrigin.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


celery = make_celery()