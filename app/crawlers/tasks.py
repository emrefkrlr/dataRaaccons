from __future__ import absolute_import, unicode_literals
from asyncio.log import logger
from celery import shared_task
from crawlers.market.getir.getir_tasks import GetirTasks
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

@shared_task
def getir_getir_crawler_task():
    now = datetime.now()
    print("Celery getir_getir_crawler_task started....", now)

    GetirTasks().getir_getir_crawler()

    print("Celery getir_getir_crawler_task done....", now)