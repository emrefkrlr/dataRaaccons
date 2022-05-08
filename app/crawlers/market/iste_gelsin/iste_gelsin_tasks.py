from crawlers.service import CrawlerServices
from crawlers.market.iste_gelsin import iste_gelsin_crawler
from mongo.services import MongoService
from datetime import datetime
import time


class IsteGelsinTasks(object):

    def iste_gelsin_crawler(self):

        print("Task iste_gelsin_crawler starded.....", datetime.now())
        
        try:
            #fetch urls to crawl
            filter = {'status': 1, 'activity': 1, 'company__name': 'iste_gelsin'}
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
                innerHTML = iste_gelsin_crawler.IsteGelsinCrawler().get_innerHTML(url.page_url, css_selector)
                products_and_price = iste_gelsin_crawler.IsteGelsinCrawler().html_parser(innerHTML, url.category)
                data['products_and_price'] = products_and_price

                document_save = MongoService().insert_one(db_name='DataRaccoons', host='dataRaccoonsMongo', port='27017', 
                username='root', password='root', collection='Market', document=data)

                if document_save:

                    print("Document saved mongodb...", now)

                time.sleep(3)
                
        except Exception as e:
            print("\nException: {}".format(e))