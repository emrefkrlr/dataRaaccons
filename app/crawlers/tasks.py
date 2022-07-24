from __future__ import absolute_import, unicode_literals
from asyncio.log import logger
from celery import shared_task
from datetime import datetime

from crawlers.a101.a101_tasks import A101Tasks
from crawlers.getir.getir_tasks import GetirTasks
from crawlers.iste_gelsin.iste_gelsin_tasks import IsteGelsinTasks
from crawlers.sok_market.sok_tasks import SokMarketTasks
from crawlers.hepsiburada.hepsiburada_tasks import HepsiburadaTasks
from crawlers.trendyol.trendyol_tasks import TrendyolTasks
from crawlers.migros.migros_tasks import MigrosTasks
from crawlers.carrefoursa.carrefoursa_tasks import CarrefoursaTasks
from crawlers.istikbal.istikbal_tasks import IstikbalTasks
from crawlers.bellona.bellona_tasks import BellonaTasks
from crawlers.dogtas.dogtas_tasks import DogtasTasks
from crawlers.enzahome.enzahome_tasks import EnzahomeTasks
from crawlers.ider_mobilya.ider_mobilya_tasks import IderMobilyaTasks
from crawlers.ikea.ikea_tasks import IkeaTasks
from crawlers.kelebek_mobilya.kelebek_mobilya_tasks import KelebekMobilyaTasks
from crawlers.kilim_mobilya.kilim_mobilya_tasks import KilimMobilyaTasks
from crawlers.koctas.koctas_tasks import KoctasTasks
from crawlers.modalife.modalife_tasks import ModalifeTasks
from crawlers.mudo.mudo_tasks import MudoTasks
from crawlers.normod.normod_tasks import NormodTasks
from crawlers.ocasso.ocasso_taks import OcassoTasks
from crawlers.ruum_store.ruum_store_tasks import RuumStoreTasks
from crawlers.vivense.vivense_tasks import VivenseTasks

_ACTIVITY_MARKET_ = "market"
_ACTIVITY_FURNITURE_ = "furniture"


# --------------------------- MARKET --------------------------- #

@shared_task
def market_getir_getir_task():
    GetirTasks().getir_getir_crawler_tasks(activity_name=_ACTIVITY_MARKET_)


@shared_task
def market_iste_gelsin_task():
    IsteGelsinTasks().iste_gelsin_crawler_tasks(activity_name=_ACTIVITY_MARKET_)


@shared_task
def market_a101_task():
    A101Tasks().a101_crawler_tasks(activity_name=_ACTIVITY_MARKET_)


@shared_task
def market_sok_market_task():
    SokMarketTasks().sok_crawler_tasks(activity_name=_ACTIVITY_MARKET_)


@shared_task
def market_migros_sanal_market_task():
    MigrosTasks().migros_sanal_market_crawler_tasks(activity_name=_ACTIVITY_MARKET_)


@shared_task
def market_trendyol_task():
    TrendyolTasks().trendyol_crawler_tasks(activity_name=_ACTIVITY_MARKET_)


@shared_task
def market_hepsiburada_task():
    HepsiburadaTasks().hepsiburada_crawler_tasks(activity_name=_ACTIVITY_MARKET_)


@shared_task
def market_carrefoursa_task():
    CarrefoursaTasks().carrefoursa_crawler_tasks(activity_name=_ACTIVITY_MARKET_)


# --------------------------- FURNITURE --------------------------- #

@shared_task
def furniture_istikbal_task():
    IstikbalTasks().istikbal_crawler_tasks(activity_name=_ACTIVITY_FURNITURE_)


@shared_task
def furniture_bellona_task():
    BellonaTasks().bellona_crawler_tasks(activity_name=_ACTIVITY_FURNITURE_)


@shared_task
def furniture_hepsiburada_task():
    HepsiburadaTasks().hepsiburada_crawler_tasks(activity_name=_ACTIVITY_FURNITURE_)


@shared_task
def furniture_trendyol_task():
    TrendyolTasks().trendyol_crawler_tasks(activity_name=_ACTIVITY_FURNITURE_)
