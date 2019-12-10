from libs.utilites.config import Config
from celery import Celery

storage = Config().storage


def make_celery(app):
    celery = Celery(app.import_name, broker=storage.get('CELERY_BROKER_URL'), backend=storage.get('REDIS_URL'))
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery
