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

    'add-every-15-hours-market_migros_sanal_market_task': {
        'task': 'crawlers.tasks.market_migros_sanal_market_task',
        'schedule': crontab(minute=0, hour='20'),
    },

    'add-every-16-hours-market_iste_gelsin_task': {
        'task': 'crawlers.tasks.market_iste_gelsin_task',
        'schedule': crontab(minute=0, hour='23'),
    },

    'add-every-17-hours-market_getir_getir_task': {
        'task': 'crawlers.tasks.market_getir_getir_task',
        'schedule': crontab(minute=0, hour='2'),
    },

    'add-every-18-hours-market_trendyol_task': {
        'task': 'crawlers.tasks.market_trendyol_task',
        'schedule': crontab(minute=0, hour='5'),
    },

    # Firefox Browser

    'add-every-15-hours-market_hepsiburada_task': {
        'task': 'crawlers.tasks.market_hepsiburada_task',
        'schedule': crontab(minute=0, hour='19'),
    },

    'add-every-16-hours-market_sok_market_task': {
        'task': 'crawlers.tasks.market_sok_market_task',
        'schedule': crontab(minute=0, hour='22'),
    },

    'add-every-17-hours-market_a101_task': {
        'task': 'crawlers.tasks.market_a101_task',
        'schedule': crontab(minute=0, hour='1'),
    },

    'add-every-18-hours-carrefoursa_crawler_tasks': {
        'task': 'crawlers.tasks.carrefoursa_crawler_tasks',
        'schedule': crontab(minute=0, hour='4'),
    },


    #-------------------------------------------------------------#

    ## Activity: Furniture
    
    
    
    #-------------------------------------------------------------#


    ## Products

    'add-every-19-hours_insert_new_products_task': {
        'task': 'products.tasks.insert_new_products_task',
        'schedule': crontab(minute=0, hour='7'),
    },

    'add-every-20-hours_product_matches_task': {
        'task': 'products.tasks.product_matches_task',
        'schedule': crontab(minute=30, hour='9'),
    },


    #-------------------------------------------------------------#



}




