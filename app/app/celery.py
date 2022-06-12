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
    # CHROME
    #'add-every-0-18-21-hours-getir_getir_crawler_task': {
    #    'task': 'crawlers.tasks.getir_getir_crawler_task',
    #    'schedule': crontab(minute=0, hour='0,6,12,20,23'),
    #},
    'add-every-0-18-21-hours-migros_sanal_market_crawler_task': {
        'task': 'crawlers.tasks.migros_sanal_market_crawler_task',
        'schedule': crontab(minute=0, hour='1,8,15,18,21,22,23'),
    },
     'add-every-0-19-21-hours-trendyol_crawler_task': {
        'task': 'crawlers.tasks.trendyol_crawler_task',
        'schedule': crontab(minute=0, hour='4,9,12,16,21,22,23'),
    },

    # FIREFOX
    #'add-every-0-18-21-hours-iste_gelsin_crawler_task': {
    #    'task': 'crawlers.tasks.iste_gelsin_crawler_task',
    #    'schedule': crontab(minute=0, hour='1,3,9,13,22'),
    #},
    #'add-every-0-18-21-hours-sok_market_crawler_task': {
    #    'task': 'crawlers.tasks.sok_market_crawler_task',
    #    'schedule': crontab(minute=0, hour='2,6,8,15,23'),
    #},
    'add-every-0-18-21-hours-a101_crawler_task': {
        'task': 'crawlers.tasks.a101_crawler_task',
        'schedule': crontab(minute=0, hour='0,5,12,17,21,22,23'),
    },

}




