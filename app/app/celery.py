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
        'schedule': crontab(minute=25, hour='15'),
    },

    'add-every-16-hours-market_iste_gelsin_task': {
        'task': 'crawlers.tasks.market_iste_gelsin_task',
        'schedule': crontab(minute=0, hour='20'),
    },

    'add-every-17-hours-market_getir_getir_task': {
        'task': 'crawlers.tasks.market_getir_getir_task',
        'schedule': crontab(minute=0, hour='21'),
    },

    'add-every-18-hours-market_trendyol_task': {
        'task': 'crawlers.tasks.market_trendyol_task',
        'schedule': crontab(minute=0, hour='22'),
    },

    # Firefox Browser

    'add-every-15-hours-market_hepsiburada_task': {
        'task': 'crawlers.tasks.market_hepsiburada_task',
        'schedule': crontab(minute=0, hour='19'),
    },

    'add-every-16-hours-market_sok_market_task': {
        'task': 'crawlers.tasks.market_sok_market_task',
        'schedule': crontab(minute=0, hour='20'),
    },

    'add-every-17-hours-market_a101_task': {
        'task': 'crawlers.tasks.market_a101_task',
        'schedule': crontab(minute=0, hour='21'),
    },

    'add-every-18-hours-carrefoursa_crawler_tasks': {
        'task': 'crawlers.tasks.carrefoursa_crawler_tasks',
        'schedule': crontab(minute=0, hour='22'),
    },


    #-------------------------------------------------------------#

    ## Activity: Furniture
    
    # Chrome Browser

    'add-every-15-hours-furniture_istikbal_task': {
        'task': 'crawlers.tasks.furniture_istikbal_task',
        'schedule': crontab(minute=0, hour='23'),
    },

    'add-every-16-hours-furniture_trendyol_task': {
        'task': 'crawlers.tasks.furniture_trendyol_task',
        'schedule': crontab(minute=0, hour='0'),
    },

    'add-every-16-hours-furniture_enzahome_task': {
        'task': 'crawlers.tasks.furniture_enzahome_task',
        'schedule': crontab(minute=0, hour='1'),
    },

    'add-every-16-hours-furniture_ikea_task': {
        'task': 'crawlers.tasks.furniture_ikea_task',
        'schedule': crontab(minute=0, hour='2'),
    },

    'add-every-16-hours-furniture_kelebek_mobilya_task': {
        'task': 'crawlers.tasks.furniture_kelebek_mobilya_task',
        'schedule': crontab(minute=0, hour='3'),
    },

    'add-every-16-hours-furniture_modalife_task': {
        'task': 'crawlers.tasks.furniture_modalife_task',
        'schedule': crontab(minute=0, hour='4'),
    },

    'add-every-16-hours-furniture_ocasso_task': {
        'task': 'crawlers.tasks.furniture_ocasso_task',
        'schedule': crontab(minute=0, hour='5'),
    },

    'add-every-16-hours-furniture_ruum_store_task': {
        'task': 'crawlers.tasks.furniture_ruum_store_task',
        'schedule': crontab(minute=0, hour='6'),
    },

    # Firefox Browser

    'add-every-15-hours-furniture_bellona_task': {
        'task': 'crawlers.tasks.furniture_bellona_task',
        'schedule': crontab(minute=0, hour='23'),
    },

    'add-every-16-hours-furniture_hepsiburada_task': {
        'task': 'crawlers.tasks.furniture_hepsiburada_task',
        'schedule': crontab(minute=0, hour='0'),
    },

    'add-every-16-hours-furniture_dogtas_task': {
        'task': 'crawlers.tasks.furniture_dogtas_task',
        'schedule': crontab(minute=0, hour='1'),
    },

    'add-every-16-hours-furniture_ider_mobilya_task': {
        'task': 'crawlers.tasks.furniture_ider_mobilya_task',
        'schedule': crontab(minute=0, hour='2'),
    },

    'add-every-16-hours-furniture_kilim_mobilya_task': {
        'task': 'crawlers.tasks.furniture_kilim_mobilya_task',
        'schedule': crontab(minute=0, hour='3'),
    },

    'add-every-16-hours-furniture_koctas_task': {
        'task': 'crawlers.tasks.furniture_koctas_task',
        'schedule': crontab(minute=0, hour='4'),
    },

    'add-every-16-hours-furniture_mudo_task': {
        'task': 'crawlers.tasks.furniture_mudo_task',
        'schedule': crontab(minute=0, hour='5'),
    },

    'add-every-16-hours-furniture_normod_task': {
        'task': 'crawlers.tasks.furniture_normod_task',
        'schedule': crontab(minute=0, hour='6'),
    },

    'add-every-16-hours-furniture_vivense_task': {
        'task': 'crawlers.tasks.furniture_vivense_task',
        'schedule': crontab(minute=0, hour='7'),
    },

    #-------------------------------------------------------------#


    ## Products

    'add-every-19-hours_insert_new_products_task': {
        'task': 'products.tasks.insert_new_products_task',
        'schedule': crontab(minute=0, hour='8'),
    },

    'add-every-20-hours_product_matches_task': {
        'task': 'products.tasks.product_matches_task',
        'schedule': crontab(minute=30, hour='8'),
    },


    #-------------------------------------------------------------#



}




