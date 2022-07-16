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

    ## Activity: Market

    # Chrome Browser

    'add-every-16-hours-market_migros_sanal_market_task': {
        'task': 'crawlers.tasks.market_migros_sanal_market_task',
        'schedule': crontab(minute=0, hour='16'),
    },

    'add-every-19-hours-market_iste_gelsin_task': {
        'task': 'crawlers.tasks.market_iste_gelsin_task',
        'schedule': crontab(minute=0, hour='19'),
    },

    'add-every-20-hours-market_getir_getir_task': {
        'task': 'crawlers.tasks.market_getir_getir_task',
        'schedule': crontab(minute=0, hour='20'),
    },

    'add-every-21-hours-market_trendyol_task': {
        'task': 'crawlers.tasks.market_trendyol_task',
        'schedule': crontab(minute=0, hour='21'),
    },

    # Firefox Browser

    'add-every-22-hours-market_hepsiburada_task': {
        'task': 'crawlers.tasks.market_hepsiburada_task',
        'schedule': crontab(minute=0, hour='22'),
    },

    'add-every-17-hours-market_sok_market_task': {
        'task': 'crawlers.tasks.market_sok_market_task',
        'schedule': crontab(minute=0, hour='17'),
    },

    'add-every-18-hours-market_a101_task': {
        'task': 'crawlers.tasks.market_a101_task',
        'schedule': crontab(minute=0, hour='18'),
    },


    #-------------------------------------------------------------#

    ## Activity: Furniture
    
    # Chrome Browser

    'add-every-16-hours-furniture_istikbal_task': {
        'task': 'crawlers.tasks.furniture_istikbal_task',
        'schedule': crontab(minute=0, hour='16', day_of_week='*/2'),
    },

    'add-every-19-hours-furniture_trendyol_task': {
        'task': 'crawlers.tasks.furniture_trendyol_task',
        'schedule': crontab(minute=0, hour='19', day_of_week='*/2'),
    },

    # Firefox Browser

    'add-every-17-hours-furniture_bellona_task': {
        'task': 'crawlers.tasks.furniture_bellona_task',
        'schedule': crontab(minute=0, hour='17', day_of_week='*/2'),
    },

    'add-every-18-hours-furniture_hepsiburada_task': {
        'task': 'crawlers.tasks.furniture_hepsiburada_task',
        'schedule': crontab(minute=0, hour='18', day_of_week='*/2'),
    },

    #-------------------------------------------------------------#


    ## Products

    'add-every-22-hours_insert_new_products_task': {
        'task': 'products.tasks.insert_new_products_task',
        'schedule': crontab(minute=0, hour='23'),
    },

    'add-every-0-hours_product_matches_task': {
        'task': 'products.tasks.product_matches_task',
        'schedule': crontab(minute=0, hour='0'),
    },


    #-------------------------------------------------------------#



}




