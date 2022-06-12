from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

app = Celery("app")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.timezone = 'Europe/Istanbul'

app.autodiscover_tasks()

app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-15-minute-helloTask': {
        'task': 'core.tasks.helloTask',
        'schedule': crontab(minute='*/15'),
    },
    'add-every-45-minute-getir_getir_crawler_task': {
        'task': 'crawlers.tasks.getir_getir_crawler_task',
        'schedule': crontab(minute='*/45'),
    },
    'add-every-20-minute-iste_gelsin_crawler_task': {
        'task': 'crawlers.tasks.iste_gelsin_crawler_task',
        'schedule': crontab(minute='*/20'),
    },
    

}




