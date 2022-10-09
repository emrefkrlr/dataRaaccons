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

    'add-every-9-hours-market_meyve_ve_sebze_chrome_task': {
        'task': 'crawlers.tasks.market_meyve_ve_sebze_chrome_task',
        'schedule': crontab(minute=0, hour='9'),
    },

    'add-every-11-hours-market_et_tavuk_balik_chrome_task': {
        'task': 'crawlers.tasks.market_et_tavuk_balik_chrome_task',
        'schedule': crontab(minute=0, hour='11'),
    },

    'add-every-13-hours-market_sut_ve_sut_urunleri_chrome_task': {
        'task': 'crawlers.tasks.market_sut_ve_sut_urunleri_chrome_task',
        'schedule': crontab(minute=0, hour='13'),
    },

    'add-every-15-hours-market_kahvaltilik_chrome_task': {
        'task': 'crawlers.tasks.market_kahvaltilik_chrome_task',
        'schedule': crontab(minute=0, hour='15'),
    },

    'add-every-17-hours-market_temel_gida_chrome_task': {
        'task': 'crawlers.tasks.market_temel_gida_chrome_task',
        'schedule': crontab(minute=0, hour='17'),
    },

    'add-every-18-hours-market_donuk_hazir_gida_chrome_task': {
        'task': 'crawlers.tasks.market_donuk_hazir_gida_chrome_task',
        'schedule': crontab(minute=0, hour='18'),
    },

    'add-every-19-hours-market_pasta_ve_pasta_malzemeleri_chrome_task': {
        'task': 'crawlers.tasks.market_pasta_ve_pasta_malzemeleri_chrome_task',
        'schedule': crontab(minute=0, hour='19'),
    },

    'add-every-20-hours-market_firin_ve_pastahane_chrome_task': {
        'task': 'crawlers.tasks.market_firin_ve_pastahane_chrome_task',
        'schedule': crontab(minute=0, hour='20'),
    },

    'add-every-21-hours-market_dondurma_ve_tatli_chrome_task': {
        'task': 'crawlers.tasks.market_dondurma_ve_tatli_chrome_task',
        'schedule': crontab(minute=0, hour='21'),
    },

    'add-every-22-hours-market_atistirmalik_chrome_task': {
        'task': 'crawlers.tasks.market_atistirmalik_chrome_task',
        'schedule': crontab(minute=0, hour='22'),
    },

    'add-every-24-hours-market_su_ve_icecek_chrome_task': {
        'task': 'crawlers.tasks.market_su_ve_icecek_chrome_task',
        'schedule': crontab(minute=0, hour='0'),
    },

    'add-every-1-hours-market_cay_ve_kahve_chrome_task': {
        'task': 'crawlers.tasks.market_cay_ve_kahve_chrome_task',
        'schedule': crontab(minute=0, hour='1'),
    },

    'add-every-2-hours-market_temizlik_ve_deterjan_chrome_task': {
        'task': 'crawlers.tasks.market_temizlik_ve_deterjan_chrome_task',
        'schedule': crontab(minute=0, hour='2'),
    },

    'add-every-4-hours-market_kisisel_bakim_chrome_task': {
        'task': 'crawlers.tasks.market_kisisel_bakim_chrome_task',
        'schedule': crontab(minute=0, hour='4'),
    },

    'add-every-6-hours-market_vitamin_dermokozmetik_chrome_task': {
        'task': 'crawlers.tasks.market_vitamin_dermokozmetik_chrome_task',
        'schedule': crontab(minute=0, hour='6'),
    },

    'add-every-7-hours-market_evcil_hayvan_chrome_task': {
        'task': 'crawlers.tasks.market_evcil_hayvan_chrome_task',
        'schedule': crontab(minute=0, hour='7'),
    },


    # Firefox Browser

    'add-every-9-hours-market_meyve_ve_sebze_frifox_task': {
        'task': 'crawlers.tasks.market_meyve_ve_sebze_frifox_task',
        'schedule': crontab(minute=0, hour='9'),
    },

    'add-every-11-hours-market_et_tavuk_balik_firefox_task': {
        'task': 'crawlers.tasks.market_et_tavuk_balik_firefox_task',
        'schedule': crontab(minute=0, hour='11'),
    },

    'add-every-13-hours-market_sut_ve_sut_urunleri_firefox_task': {
        'task': 'crawlers.tasks.market_sut_ve_sut_urunleri_firefox_task',
        'schedule': crontab(minute=0, hour='13'),
    },

    'add-every-15-hours-market_kahvaltilik_firefox_task': {
        'task': 'crawlers.tasks.market_kahvaltilik_firefox_task',
        'schedule': crontab(minute=0, hour='15'),
    },

    'add-every-17-hours-market_temel_gida_firefox_task': {
        'task': 'crawlers.tasks.market_temel_gida_firefox_task',
        'schedule': crontab(minute=0, hour='17'),
    },

    'add-every-18-hours-market_donuk_hazir_gida_firefox_task': {
        'task': 'crawlers.tasks.market_donuk_hazir_gida_firefox_task',
        'schedule': crontab(minute=0, hour='18'),
    },

    'add-every-19-hours-market_pasta_ve_pasta_malzemeleri_firefox_task': {
        'task': 'crawlers.tasks.market_pasta_ve_pasta_malzemeleri_firefox_task',
        'schedule': crontab(minute=0, hour='19'),
    },

    'add-every-20-hours-market_firin_ve_pastahane_firefox_task': {
        'task': 'crawlers.tasks.market_firin_ve_pastahane_firefox_task',
        'schedule': crontab(minute=0, hour='20'),
    },

    'add-every-21-hours-market_dondurma_ve_tatli_firefox_task': {
        'task': 'crawlers.tasks.market_dondurma_ve_tatli_firefox_task',
        'schedule': crontab(minute=0, hour='21'),
    },

    'add-every-22-hours-market_atistirmalik_firefox_task': {
        'task': 'crawlers.tasks.market_atistirmalik_firefox_task',
        'schedule': crontab(minute=0, hour='22'),
    },

    'add-every-24-hours-market_su_ve_icecek_firefox_task': {
        'task': 'crawlers.tasks.market_su_ve_icecek_firefox_task',
        'schedule': crontab(minute=0, hour='0'),
    },

    'add-every-1-hours-market_cay_ve_kahve_firefox_task': {
        'task': 'crawlers.tasks.market_cay_ve_kahve_firefox_task',
        'schedule': crontab(minute=0, hour='1'),
    },

    'add-every-2-hours-market_temizlik_ve_deterjan_firefox_task': {
        'task': 'crawlers.tasks.market_temizlik_ve_deterjan_firefox_task',
        'schedule': crontab(minute=0, hour='2'),
    },

    'add-every-4-hours-market_kisisel_bakim_firefox_task': {
        'task': 'crawlers.tasks.market_kisisel_bakim_firefox_task',
        'schedule': crontab(minute=0, hour='4'),
    },

    'add-every-6-hours-market_vitamin_dermokozmetik_firefox_task': {
        'task': 'crawlers.tasks.market_vitamin_dermokozmetik_firefox_task',
        'schedule': crontab(minute=0, hour='6'),
    },

    'add-every-7-hours-market_evcil_hayvan_firefox_task': {
        'task': 'crawlers.tasks.market_evcil_hayvan_firefox_task',
        'schedule': crontab(minute=0, hour='7'),
    },

   


    #-------------------------------------------------------------#

    ## Activity: Furniture
    
    
    
    #-------------------------------------------------------------#


    ## Products

    'add-every-8-hours_insert_new_products_task': {
        'task': 'products.tasks.insert_new_products_task',
        'schedule': crontab(minute=0, hour='8'),
    },

    'add-every-8-30-hours_product_matches_task': {
        'task': 'products.tasks.product_matches_task',
        'schedule': crontab(minute=30, hour='8'),
    },

    'add-ayin_1_ve_3_haftasi_insert_new_sub_category': {
        'task': 'activities.tasks.insert_new_sub_category',
        'schedule': crontab(0, 0, day_of_month='1-7,15-21'),
        
    },


    #-------------------------------------------------------------#



}




