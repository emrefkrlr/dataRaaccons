from crawlers.service import CrawlerServices
from crawlers.market.a101 import a101_crawler
from mongo.services import MongoService
import datetime
import time


class A101Tasks(object):

    def a101_crawler(self):

        print("Task a101_crawler starded.....", datetime.datetime.utcnow())
        
        try:
            #fetch urls to crawl
            filter = {'status': 1, 'activity': 1, 'company__name': 'A101'}
            urls = CrawlerServices().fetch_urls_to_crawl(filter=filter)
            
            for url in urls:
                
                data = {
                    'info': {
                        'company_name': str(url.company),
                        'demand': str(url.demand),
                        'activity': str(url.activity),
                        'activity_category': str(url.activity_category),
                        'page_name': str(url.page_name),
                        'page_category': str(url.page_category),
                        'page_url': str(url.page_url),
                        'crawled_time': str(datetime.datetime.utcnow())
                    },
                }
                
                data['products_and_price'] = []
                css_selector = url.css_selector.replace(" ", ".")

                if url.page_numbers >= 1:
                    for page in range(1, url.page_numbers + 1):

                        innerHTML = a101_crawler.A101Crawler().get_innerHTML(url.page_url, css_selector, page)
                        products_and_price = a101_crawler.A101Crawler().html_parser(innerHTML, url.page_category)

                        data['products_and_price'].append(products_and_price[0])
                
                else:
                    innerHTML = a101_crawler.A101Crawler().get_innerHTML(url.page_url, css_selector)
                    products_and_price = a101_crawler.A101Crawler().html_parser(innerHTML, url.page_category)
                    data['products_and_price'] = products_and_price

                document_save = MongoService().insert_one(db_name='DataRaccoons', host='dataRaccoonsMongo', port='27017', 
                username='root', password='root', collection='market', document=data)

                if document_save:

                    print("Document saved mongodb...", datetime.datetime.utcnow())

                time.sleep(3)
                
        except Exception as e:
            print("\nA101Tasks a101_crawler Exception: \n{}\nURL: {} \nPAGE: {}".format(e, url.page_url, page))