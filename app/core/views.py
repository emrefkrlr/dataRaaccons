import imp
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

def core_index(request):

	
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
	
	context = {'configs': "configs"}
	
	return render(request, 'test.html', context)