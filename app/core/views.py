from django.shortcuts import render
from crawlers.getir.getir_tasks import GetirTasks
from crawlers.a101.a101_tasks import A101Tasks
from crawlers.trendyol.trendyol_tasks import TrendyolTasks
from crawlers.hepsiburada.hepsiburada_tasks import HepsiburadaTasks
from crawlers.sok_market.sok_tasks import SokMarketTasks
from crawlers.iste_gelsin.iste_gelsin_tasks import IsteGelsinTasks
from crawlers.istikbal.istikbal_tasks import IstikbalTasks
from crawlers.bellona.bellona_tasks import BellonaTasks
from crawlers.migros.migros_tasks import MigrosTasks
from crawlers.carrefoursa.carrefoursa_tasks import CarrefoursaTasks

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
from products import tasks


#def core_index(request):

	
	#print(GetirTasks().getir_getir_crawler_tasks(activity_name="market"))
	#print(A101Tasks().a101_crawler_tasks(activity_name="market"))
	#print(TrendyolTasks().trendyol_crawler_tasks(activity_name="market"))
	#print(TrendyolTasks().trendyol_crawler_tasks(activity_name="furniture"))
	#print(HepsiburadaTasks().hepsiburada_crawler_tasks(activity_name="market"))
	#print(HepsiburadaTasks().hepsiburada_crawler_tasks(activity_name="furniture"))
	#print(SokMarketTasks().sok_crawler_tasks(activity_name="market"))
	#print(IsteGelsinTasks().iste_gelsin_crawler_tasks(activity_name="market"))
	#print(IstikbalTasks().istikbal_crawler_tasks(activity_name="furniture"))
	#print(BellonaTasks().bellona_crawler_tasks(activity_name="furniture"))
	#print(MigrosTasks().migros_sanal_market_crawler_tasks(activity_name="market"))
	#print(CarrefoursaTasks().carrefoursa_crawler_tasks(activity_name="market"))
	
	#print(DogtasTasks().dogtas_crawler_tasks(activity_name="furniture"))
	#print(EnzahomeTasks().enzahome_crawler_tasks(activity_name="furniture")) YENİ
	#print(IderMobilyaTasks().ider_mobilya_crawler_tasks(activity_name="furniture"))
	#print(IkeaTasks().ikea_crawler_tasks(activity_name="furniture"))
	#print(KelebekMobilyaTasks().kelebek_mobilya_crawler_tasks(activity_name="furniture"))
	#print(KilimMobilyaTasks().kilim_mobilya_crawler_tasks(activity_name="furniture"))
	#print(KoctasTasks().koctas_crawler_tasks(activity_name="furniture"))
	#print(ModalifeTasks().modalife_crawler_tasks(activity_name="furniture"))
	#print(MudoTasks().mudo_crawler_tasks(activity_name="furniture"))
	#print(NormodTasks().normod_crawler_tasks(activity_name="furniture"))
	#print(OcassoTasks().ocasso_crawler_tasks(activity_name="furniture"))
	#print(RuumStoreTasks().ruum_store_crawler_tasks(activity_name="furniture"))
	#print(VivenseTasks().vivense_crawler_tasks(activity_name="furniture"))
	#print(tasks.insert_new_products_task())
	
	#context = {'configs': "configs"}
	
	#return render(request, 'test.html', context)