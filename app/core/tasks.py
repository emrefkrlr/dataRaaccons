from __future__ import absolute_import, unicode_literals
from asyncio.log import logger

from celery import shared_task
import logging


logger = logging.getLogger(__name__)

@shared_task
def helloTask():
    print('Hello Celery Crontab')
    logger.info("Task executable...")