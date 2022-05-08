from crawlers.service import CrawlerServices
from crawlers.market.getir import getir_crawler
from mongo.services import MongoService
from datetime import datetime
import time

class GetirTasks(object):

    def getir_getir_crawler(self):
        
        print("Task getir_getir_crawler started.....", datetime.now())
        
        try:
            #fetch urls to crawl
            filter = {'status': 1, 'activity': 1, 'company__name': 'getir_getir'}
            urls = CrawlerServices().fetch_urls_to_crawl(filter=filter)
            
            for url in urls:
                now = datetime.now()
                print(url)
                data = {
                    'info': {
                        'company_name': str(url.company),
                        'activity': str(url.activity),
                        'demand': str(url.demand),
                        'page_name': str(url.page_name),
                        'page_url': str(url.page_url),
                        'category': str(url.category),
                        'crawled_time': str(now)
                    },
                }
                
                css_selector = url.css_selector.replace(" ", ".")
                innerHTML = getir_crawler.GetirCrawler().get_innerHTML(url.page_url, css_selector)
                products_and_price = getir_crawler.GetirCrawler().html_parser(innerHTML)
                data['products_and_price'] = products_and_price

                document_save = MongoService().insert_one(db_name='DataRaccoons', host='dataRaccoonsMongo', port='27017', 
                username='root', password='root', collection='Market', document=data)

                if document_save:

                    print("Document saved mongodb...", now)

                time.sleep(3)
                
        except Exception as e:
            print("\nException: {}".format(e))