from crawlers.service import CrawlerServices
from crawlers.market.iste_gelsin import iste_gelsin_crawler
from mongo.services import MongoService
import datetime
import time


class IsteGelsinTasks(object):

    def iste_gelsin_crawler(self):

        print("Task iste_gelsin_crawler starded.....", datetime.datetime.utcnow())
        
        try:
            #fetch urls to crawl
            filter = {'status': 1, 'activity': 1, 'company__name': 'iste_gelsin'}
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
                innerHTML = iste_gelsin_crawler.IsteGelsinCrawler().get_innerHTML(url.page_url, css_selector)
                products_and_price = iste_gelsin_crawler.IsteGelsinCrawler().html_parser(innerHTML, url.page_category)
                data['products_and_price'] = products_and_price

                document_save = MongoService().insert_one(db_name='DataRaccoons', host='dataRaccoonsMongo', port='27017', 
                username='root', password='root', collection='market', document=data)

                if document_save:

                    print("Document saved mongodb...", datetime.datetime.utcnow())

                time.sleep(3)
                
        except Exception as e:
            print("\nIsteGelsinTasks iste_gelsin_crawler Exception: \n{}\nURL: {}".format(e, url.page_url))