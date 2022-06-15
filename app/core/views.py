from distutils.command.config import config
from email import message
from itertools import count
from multiprocessing import context
from pickletools import markobject
from pprint import pprint
from unicodedata import name
from django.shortcuts import render
from mongo.services import MongoService
from crawlers.service import CrawlerServices
from activities.service import ActivitiesService
import logging
from crawlers.market.migros.migros_tasks import MigrosTasks
from crawlers.market.trendyol.trendyol_tasks import TrendyolTasks
from crawlers.market.a101.a101_tasks import A101Tasks

from crawlers.furniture.istikbal.istikbal_tasks import IstikbalTasks
from crawlers.furniture.bellona.bellona_tasks import BellonaTasks
from crawlers.furniture.trendyol.trendyol_tasks import TrendyolTasks as FurnitureTrendyol
from crawlers.furniture.hepsiburada.hepsiburada_tasks import HepsiburadaTasks

from crawlers.functions import char_to_replace
import datetime
import json
from dashboard.service import DashboardService
from products.models import Products
from companies.models import Companies, CompanyActivities
from activities.models import Activities, ActivityCategory
from products.service import ProductsService
from products.product_matches import jaro_winkler_distance
from products.tasks import insert_new_products_task, product_matches_task
from django.db.models import Count
from account.models import AccountCompany
from statistics import mean

logger = logging.getLogger(__name__)


def index(request):
	
	#fetch urls to crawl

	#filter = {'status': 1, 'activity': 1, 'company__name':'sok', 'category': 'meyve_ve_sebze'}
	

	

	activities = ActivitiesService().get_activities(filter={'status': 1})
	
	#print(len(activities))
	for a in activities:
		#print(a.name)
		filter = {'status': 1, 'activity': a.id}
		
		urls = CrawlerServices().fetch_urls_to_crawl(filter=filter)

		#print(urls)

	categories = CrawlerServices().get_unique_page_category(filter=filter)


	query = {}
	

	market_data = MongoService().find(db_name='DataRaccoons', 
	host='dataRaccoonsMongo', port='27017', username='root', 
	password='root', collection='market', query=query, distinct="info.company_name")





	#### DASHBOARD #####


	results = []
	main_company_id = 1
	activity_id = 1
	
	#for i in DashboardService().activity_category_based_product_statistics_of_companies(main_company_id==main_company_id, activity_id=activity_id):
		#print(i)


	#print("-----------------------------------")

	#print(DashboardService().main_company_activity_category_based_statistics(activity_id=activity_id, company_id=main_company_id))

	#print("-----------------------------------")

	#print(DashboardService().main_company_activity_category_based_products_ratio(activity_id=activity_id, company_id=main_company_id))
	
	#print("-----------------------------------")


	#print(DashboardService().activity_category_based_products_ratio_of_companies(activity_id=activity_id))
	#print(datetime.datetime.utcnow())

	#print(datetime.datetime.now())
	#print(datetime.datetime(2009, 11, 12, 12))


	#print(MigrosTasks().migros_sanal_market_crawler())
	#print(A101Tasks().a101_crawler())
	#print(TrendyolTasks().trendyol_crawler())

	#print(IstikbalTasks().istikbal_crawler())
	#print(BellonaTasks().bellona_crawler())
	#print(FurnitureTrendyol().trendyol_crawler())
	print(HepsiburadaTasks().hepsiburada_crawler())


	z = "2.495,25"

	#print(insert_new_products_task())
	#print(product_matches_task())
	#get() returned more than one Products -- it returned 2!

	#print(float(char_to_replace(z)))

	#print(int(z))

	#activity_categories = ActivityCategory.objects.filter(**{"activity": 1})



	#for activity_category in activity_categories:


	#	print("\n-----------------------------\n{}".format(activity_category))
	#	a = Products.objects.filter(**{'activity_category': activity_category.id, 'status': 1}).values('company',"activity_category",).annotate(product_count=Count("sub_category"))
	#	print(a)
	#	print("\n-----------------------------\n")
		


	#main_category = Products.objects.filter(**{'company': 6}).values('activity_category').annotate(dcount=Count("sub_category"))
	
	#companies_to_compare = Products.objects.values("company","activity_category").filter(**{'status':1}).annotate(dcount=Count("sub_category"))
	

	#for company_to_compare in companies_to_compare:
		#print(company_to_compare)
	#	pass
	
	
	
	context = {'urls': urls}
	
	return render(request, 'index.html', context)