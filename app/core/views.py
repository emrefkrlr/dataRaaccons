from distutils.command.config import config
from multiprocessing import context
from django.shortcuts import render
from mongo.services import MongoService
from crawlers.service import CrawlerServices
import logging
from datetime import datetime
import json
logger = logging.getLogger(__name__)




def index(request):
	
	#fetch urls to crawl

	filter = {'status': 1, 'activity': 1, 'company__name':'iste_gelsin'}
	
	urls = CrawlerServices().fetch_urls_to_crawl(filter=filter)
	
	for url in urls:
		now = datetime.now()

		class_name = url.css_selector.replace(" ", ".")

		data = {
			'info': {
				'company_name': str(url.company),
            	'activity': str(url.activity),
            	'demand': str(url.demand),
            	'page_name': str(url.page_name),
            	'page_url': str(url.page_url),
				'css_selector': str(class_name),
            	'crawled_time': str(now)
			},
		}
		
		
		print(data)
	context = {'urls': urls}
	
	return render(request, 'index.html', context)