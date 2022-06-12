from __future__ import absolute_import, unicode_literals
from asyncio.log import logger
from celery import shared_task
from crawlers.market.getir.getir_tasks import GetirTasks
from crawlers.market.iste_gelsin.iste_gelsin_tasks import IsteGelsinTasks
from crawlers.market.sok_market.sok_market_tasks import SokMarketTasks
from crawlers.market.a101.a101_tasks import A101Tasks
from crawlers.market.migros.migros_tasks import MigrosTasks
from crawlers.market.trendyol.trendyol_tasks import TrendyolTasks
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

@shared_task
def getir_getir_crawler_task():

    GetirTasks().getir_getir_crawler()


@shared_task
def iste_gelsin_crawler_task():

    IsteGelsinTasks().iste_gelsin_crawler()


@shared_task
def sok_market_crawler_task():

    SokMarketTasks().sok_market_crawler()


@shared_task
def a101_crawler_task():

    A101Tasks().a101_crawler()


@shared_task
def migros_sanal_market_crawler_task():

    MigrosTasks().migros_sanal_market_crawler()


@shared_task
def trendyol_crawler_task():

    TrendyolTasks().trendyol_crawler()



