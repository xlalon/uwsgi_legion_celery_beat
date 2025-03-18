# -*- coding: utf8 -*-

from flask import Flask

from celery_ import celery_init_app


def create_app(init_apps=None) -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(
        CELERY=dict(
            broker_url="redis://redis:6379",
            result_backend="redis://redis:6379",
            task_ignore_result=False,
            timezone="Asia/Shanghai",
        ),
    )
    app.config.from_prefixed_env()
    if init_apps:
        for init_app in init_apps:
            init_app(app)
    return app


flask_app = create_app([celery_init_app])
celery_app = flask_app.extensions["celery"]
