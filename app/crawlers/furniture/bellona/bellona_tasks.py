from crawlers.service import CrawlerServices
from crawlers.furniture.bellona import bellona_crawler
from mongo.services import MongoService
import datetime
import time



class BellonaTasks(object):

    def bellona_crawler(self):

        print("Task bellona_crawler starded.....", datetime.datetime.utcnow())
        
        try:
            #fetch urls to crawl
            filter = {'status': 1, 'activity': 2, 'company__name': 'bellona'}
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

                        innerHTML = bellona_crawler.BellonaCrawler().get_innerHTML(url.page_url, css_selector, page)
                        products_and_price = bellona_crawler.BellonaCrawler().html_parser(innerHTML, url.page_category)

                        data['products_and_price'] = data['products_and_price'] + products_and_price
                
                else:
                    innerHTML = bellona_crawler.BellonaCrawler().get_innerHTML(url.page_url, css_selector)
                    products_and_price = bellona_crawler.BellonaCrawler().html_parser(innerHTML, url.page_category)
                    data['products_and_price'] = products_and_price

                document_save = MongoService().insert_one(db_name='DataRaccoons', host='dataRaccoonsMongo', port='27017', 
                username='root', password='root', collection='furniture', document=data)

                if document_save:

                    print("Document saved mongodb...", datetime.datetime.utcnow())

                time.sleep(3)
                
        except Exception as e:
            print("\n BellonaTasks bellona_crawler Exception: \n{}\nURL: {} \nPAGE: {}".format(e, url.page_url, page))