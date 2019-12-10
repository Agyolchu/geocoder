from celery import Task


class TaskBase(Task):
    def __init__(self, *args, **kwargs):
        super(TaskBase, self).__init__(*args, **kwargs)

    def run(self, *args, **kwargs):
        raise NotImplementedError
