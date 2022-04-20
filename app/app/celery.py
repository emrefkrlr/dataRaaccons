from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

app = Celery("app")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-5-seccond-helloTask': {
        'task': 'core.tasks.helloTask',
        'schedule': 5,
    },

}

app.autodiscover_tasks()


