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
from crawlers.metro_market.metro_market_tasks import MetroMarketTasks
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
def market_meyve_ve_sebze_chrome_task():
    
    _ACTIVITY_CATEGORY_ = "Meyve ve Sebze"
    
    # Chrome
    GetirTasks().getir_getir_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MetroMarketTasks().metro_market_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    IsteGelsinTasks().iste_gelsin_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MigrosTasks().migros_sanal_market_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_meyve_ve_sebze_frifox_task():

    _ACTIVITY_CATEGORY_ = "Meyve ve Sebze"

    # FireFox
    A101Tasks().a101_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    SokMarketTasks().sok_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    CarrefoursaTasks().carrefoursa_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_et_tavuk_balik_chrome_task():

    _ACTIVITY_CATEGORY_ = "Et Tavuk ve Balık"

    # Chrome
    GetirTasks().getir_getir_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MetroMarketTasks().metro_market_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    IsteGelsinTasks().iste_gelsin_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MigrosTasks().migros_sanal_market_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_et_tavuk_balik_firefox_task():

    _ACTIVITY_CATEGORY_ = "Et Tavuk ve Balık"

    # FireFox
    A101Tasks().a101_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    SokMarketTasks().sok_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    CarrefoursaTasks().carrefoursa_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_sut_ve_sut_urunleri_chrome_task():

    _ACTIVITY_CATEGORY_ = "Süt ve Süt Ürünleri"

    # Chrome
    GetirTasks().getir_getir_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MetroMarketTasks().metro_market_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    IsteGelsinTasks().iste_gelsin_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MigrosTasks().migros_sanal_market_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_sut_ve_sut_urunleri_firefox_task():

    _ACTIVITY_CATEGORY_ = "Süt ve Süt Ürünleri"
    
    # FireFox
    #A101Tasks().a101_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    SokMarketTasks().sok_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    CarrefoursaTasks().carrefoursa_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_kahvaltilik_chrome_task():

    _ACTIVITY_CATEGORY_ = "Kahvaltılık"

    # Chrome
    GetirTasks().getir_getir_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MetroMarketTasks().metro_market_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    IsteGelsinTasks().iste_gelsin_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MigrosTasks().migros_sanal_market_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_kahvaltilik_firefox_task():

    _ACTIVITY_CATEGORY_ = "Kahvaltılık"

    # FireFox
    A101Tasks().a101_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    SokMarketTasks().sok_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    CarrefoursaTasks().carrefoursa_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_temel_gida_chrome_task():

    _ACTIVITY_CATEGORY_ = "Temel Gıda"

    # Chrome
    GetirTasks().getir_getir_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MetroMarketTasks().metro_market_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    IsteGelsinTasks().iste_gelsin_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MigrosTasks().migros_sanal_market_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_temel_gida_firefox_task():

    _ACTIVITY_CATEGORY_ = "Temel Gıda"

    # FireFox
    A101Tasks().a101_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    SokMarketTasks().sok_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    CarrefoursaTasks().carrefoursa_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_donuk_hazir_gida_chrome_task():

    _ACTIVITY_CATEGORY_ = "Donuk Hazır Gıda"

    # Chrome
    GetirTasks().getir_getir_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MetroMarketTasks().metro_market_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    IsteGelsinTasks().iste_gelsin_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MigrosTasks().migros_sanal_market_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_donuk_hazir_gida_firefox_task():

    _ACTIVITY_CATEGORY_ = "Donuk Hazır Gıda"

    # FireFox
    A101Tasks().a101_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    SokMarketTasks().sok_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    CarrefoursaTasks().carrefoursa_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_pasta_ve_pasta_malzemeleri_chrome_task():

    _ACTIVITY_CATEGORY_ = "Pasta ve Malzemeleri"

    # Chrome
    GetirTasks().getir_getir_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MetroMarketTasks().metro_market_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    IsteGelsinTasks().iste_gelsin_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MigrosTasks().migros_sanal_market_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_pasta_ve_pasta_malzemeleri_firefox_task():

    _ACTIVITY_CATEGORY_ = "Pasta ve Malzemeleri"

    # FireFox
    A101Tasks().a101_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    SokMarketTasks().sok_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    CarrefoursaTasks().carrefoursa_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_firin_ve_pastahane_chrome_task():

    _ACTIVITY_CATEGORY_ = "Fırın ve Pastane"
    
    # Chrome
    GetirTasks().getir_getir_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MetroMarketTasks().metro_market_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    IsteGelsinTasks().iste_gelsin_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MigrosTasks().migros_sanal_market_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_firin_ve_pastahane_firefox_task():

    _ACTIVITY_CATEGORY_ = "Fırın ve Pastane"

    # FireFox
    A101Tasks().a101_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    SokMarketTasks().sok_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    CarrefoursaTasks().carrefoursa_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_dondurma_ve_tatli_chrome_task():

    _ACTIVITY_CATEGORY_ = "Dondurma ve Tatlı"

    # Chrome
    GetirTasks().getir_getir_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MetroMarketTasks().metro_market_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    IsteGelsinTasks().iste_gelsin_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MigrosTasks().migros_sanal_market_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_dondurma_ve_tatli_firefox_task():

    _ACTIVITY_CATEGORY_ = "Dondurma ve Tatlı"

    # FireFox
    A101Tasks().a101_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    SokMarketTasks().sok_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    CarrefoursaTasks().carrefoursa_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_atistirmalik_chrome_task():

    _ACTIVITY_CATEGORY_ = "Atıştırmalık"

    # Chrome
    GetirTasks().getir_getir_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MetroMarketTasks().metro_market_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    IsteGelsinTasks().iste_gelsin_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MigrosTasks().migros_sanal_market_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_atistirmalik_firefox_task():

    _ACTIVITY_CATEGORY_ = "Atıştırmalık"

    # FireFox
    A101Tasks().a101_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    SokMarketTasks().sok_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    CarrefoursaTasks().carrefoursa_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_su_ve_icecek_chrome_task():

    _ACTIVITY_CATEGORY_ = "Su ve İçeçek"

    # Chrome
    GetirTasks().getir_getir_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MetroMarketTasks().metro_market_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    IsteGelsinTasks().iste_gelsin_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MigrosTasks().migros_sanal_market_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_su_ve_icecek_firefox_task():

    _ACTIVITY_CATEGORY_ = "Su ve İçeçek"

    # FireFox
    A101Tasks().a101_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    SokMarketTasks().sok_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    CarrefoursaTasks().carrefoursa_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_cay_ve_kahve_chrome_task():

    _ACTIVITY_CATEGORY_ = "Çay ve Kahve"

    # Chrome
    GetirTasks().getir_getir_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MetroMarketTasks().metro_market_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    IsteGelsinTasks().iste_gelsin_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MigrosTasks().migros_sanal_market_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_cay_ve_kahve_firefox_task():

    _ACTIVITY_CATEGORY_ = "Çay ve Kahve"

    # FireFox
    A101Tasks().a101_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    SokMarketTasks().sok_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    CarrefoursaTasks().carrefoursa_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_temizlik_ve_deterjan_chrome_task():

    _ACTIVITY_CATEGORY_ = "Temizlik Deterjan"

    # Chrome
    GetirTasks().getir_getir_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MetroMarketTasks().metro_market_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    IsteGelsinTasks().iste_gelsin_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MigrosTasks().migros_sanal_market_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_temizlik_ve_deterjan_firefox_task():

    _ACTIVITY_CATEGORY_ = "Temizlik Deterjan"

    # FireFox
    A101Tasks().a101_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    SokMarketTasks().sok_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    CarrefoursaTasks().carrefoursa_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_kisisel_bakim_chrome_task():

    _ACTIVITY_CATEGORY_ = "Kişisel Bakım"

    # Chrome
    GetirTasks().getir_getir_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MetroMarketTasks().metro_market_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    IsteGelsinTasks().iste_gelsin_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MigrosTasks().migros_sanal_market_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_kisisel_bakim_firefox_task():

    _ACTIVITY_CATEGORY_ = "Kişisel Bakım"

    # FireFox
    A101Tasks().a101_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    SokMarketTasks().sok_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    CarrefoursaTasks().carrefoursa_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_vitamin_dermokozmetik_chrome_task():

    _ACTIVITY_CATEGORY_ = "Vitamin ve Dermokozmetik"

    # Chrome
    GetirTasks().getir_getir_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MetroMarketTasks().metro_market_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    IsteGelsinTasks().iste_gelsin_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MigrosTasks().migros_sanal_market_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_vitamin_dermokozmetik_firefox_task():

    _ACTIVITY_CATEGORY_ = "Vitamin ve Dermokozmetik"

    # FireFox
    A101Tasks().a101_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    SokMarketTasks().sok_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    CarrefoursaTasks().carrefoursa_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_evcil_hayvan_chrome_task():

    _ACTIVITY_CATEGORY_ = "Evcil Hayvan"

    # Chrome
    GetirTasks().getir_getir_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MetroMarketTasks().metro_market_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    IsteGelsinTasks().iste_gelsin_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    MigrosTasks().migros_sanal_market_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)


@shared_task
def market_evcil_hayvan_firefox_task():

    _ACTIVITY_CATEGORY_ = "Evcil Hayvan"

    # FireFox
    A101Tasks().a101_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    SokMarketTasks().sok_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)
    CarrefoursaTasks().carrefoursa_crawler_tasks(activity_name=_ACTIVITY_MARKET_, activity_category=_ACTIVITY_CATEGORY_)



# --------------------------- FURNITURE --------------------------- #

@shared_task
def furniture_vivense_task():
    VivenseTasks().vivense_crawler_tasks(activity_name=_ACTIVITY_FURNITURE_)












