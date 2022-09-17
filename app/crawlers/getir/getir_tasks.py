from crawlers.service import CrawlerServices
from mongo.services import MongoService
from crawlers.getir import getir_crawler
import datetime
import time

class GetirTasks(object):

    def getir_getir_crawler_tasks(self, activity_name, activity_category):

        try:

            print("Task getir_getir_crawler_tasks started.....", datetime.datetime.utcnow())

            get_crawler_config = CrawlerServices().get_crawler_config(company="getir_getir", activity=activity_name)

            get_crawlers = CrawlerServices().fetch_urls_to_crawl({"status": 1, 'company__name': 'getir_getir', "activity__name": activity_name, "activity_category__name": activity_category })

            if get_crawlers:

                for crawler in get_crawlers:
                    
                    data = {
                        'info': {
                            'company_name': str(crawler.company),
                            'demand': str(crawler.demand),
                            'activity': str(crawler.activity),
                            'activity_category': str(crawler.activity_category),
                            'page_name': str(crawler.page_name),
                            'page_category': str(crawler.page_category),
                            'page_url': str(crawler.page_url),
                            'crawled_time': str(datetime.datetime.utcnow())
                        },
                    }

                    css_selector = get_crawler_config.css_selector.replace(" ", ".")
                    innerHTML = getir_crawler.GetirCrawler().get_innerHTML(crawler.page_url, css_selector)
                    products_and_price = getir_crawler.GetirCrawler().html_parser(innerHTML, get_crawler_config)
                    
                    if len(products_and_price) > 0:
                        data['products_and_price'] = products_and_price

                    if data['products_and_price']:
                        document_save = MongoService().insert_one(collection=activity_name, document=data)

                        if document_save:
                            print("Document saved mongodb Getir...", datetime.datetime.utcnow())
            
            else:

                print("GETIR Activity Category: {} bulunmuyor....".format(activity_category))
                  

        except Exception as e:
            print("GetirTasks getir_getir_crawler_tasks EXCEPTION: {} \n ACTIVITY: {}".format(e, activity_name))
            