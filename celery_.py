# -*- coding: utf8 -*-

import time
from celery import Celery, Task, shared_task
from flask import Flask


def celery_init_app(flask_app: Flask) -> Celery:

    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with flask_app.app_context():
                return self.run(*args, **kwargs)

    app = Celery(flask_app.name, task_cls=FlaskTask)
    app.config_from_object(flask_app.config["CELERY"])
    app.set_default()

    app.conf.beat_schedule = {
        'task-debug-every-seconds': {
            'task': 'celery_.task_debug',
            'schedule': 1,
        },
    }

    flask_app.extensions["celery"] = app

    return app


@shared_task(ignore_result=False)
def task_debug() -> int:
    return int(time.time())
