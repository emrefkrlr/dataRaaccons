from crawlers.service import CrawlerServices
from crawlers.market.getir import getir_crawler
from mongo.services import MongoService
import datetime
import time

class GetirTasks(object):

    def getir_getir_crawler(self):
        
        print("Task getir_getir_crawler started.....", datetime.datetime.utcnow())
        
        try:
            #fetch urls to crawl
            filter = {'status': 1, 'activity': 1, 'company__name': 'getir_getir'}
            urls = CrawlerServices().fetch_urls_to_crawl(filter=filter)
            
            for url in urls:
                now = datetime.now()
                data = {
                    'info': {
                        'company_name': str(url.company),
                        'demand': str(url.demand),
                        'activity': str(url.activity),
                        'activity_category': str(url.activity_category),
                        'page_name': str(url.page_name),
                        'page_category': str(url.page_category),
                        'page_url': str(url.page_url),
                        'crawled_time': datetime.datetime.utcnow()
                    },
                }
                
                css_selector = url.css_selector.replace(" ", ".")
                innerHTML = getir_crawler.GetirCrawler().get_innerHTML(url.page_url, css_selector)
                products_and_price = getir_crawler.GetirCrawler().html_parser(innerHTML)
                data['products_and_price'] = products_and_price

                document_save = MongoService().insert_one(db_name='DataRaccoons', host='dataRaccoonsMongo', port='27017', 
                username='root', password='root', collection='market', document=data)

                if document_save:

                    print("Document saved mongodb...", datetime.datetime.utcnow())

                time.sleep(3)
                
        except Exception as e:
            print("\nGetirTasks getir_getir_crawler Exception: \n{}\nURL: {}".format(e, url.page_url))