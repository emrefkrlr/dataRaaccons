from __future__ import absolute_import, unicode_literals
from asyncio.log import logger
from celery import shared_task
from crawlers.market.getir.getir_tasks import GetirTasks
from crawlers.market.iste_gelsin.iste_gelsin_tasks import IsteGelsinTasks
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

@shared_task
def getir_getir_crawler_task():

    now = datetime.now()
    print("Celery getir_getir_crawler_task started....", now)

    GetirTasks().getir_getir_crawler()

    print("Celery getir_getir_crawler_task done....", now)

@shared_task
def iste_gelsin_crawler_task():

    now = datetime.now()
    print("Celery iste_gelsin_crawler_task started....", now)

    IsteGelsinTasks().iste_gelsin_crawler()

    print("Celery iste_gelsin_crawler_task done....", now)