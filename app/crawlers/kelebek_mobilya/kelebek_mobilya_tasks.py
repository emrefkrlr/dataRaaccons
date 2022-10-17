from crawlers.service import CrawlerServices
from mongo.services import MongoService
from crawlers.kelebek_mobilya import kelebek_mobilya_crawler
import datetime
import time


class KelebekMobilyaTasks(object):

    def kelebek_mobilya_crawler_tasks(self, activity_name):

        try:

            get_crawler_config = CrawlerServices().get_crawler_config(company="kelebek_mobilya", activity=activity_name)

            get_crawlers = CrawlerServices().fetch_urls_to_crawl({"status": 1, 'company__name': 'kelebek_mobilya', "activity__name": activity_name})

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
                        'crawled_time': str(datetime.datetime.now()),
                    },
                }

                data['products_and_price'] = []
                css_selector = get_crawler_config.css_selector.replace(" ", ".")

                if crawler.page_numbers >= 1:
                    for page in range(1, crawler.page_numbers + 1):

                        innerHTML = kelebek_mobilya_crawler.KelebekMobilyaCrawler().get_innerHTML(crawler.page_url, css_selector, page)
                        products_and_price = kelebek_mobilya_crawler.KelebekMobilyaCrawler().html_parser(innerHTML, get_crawler_config, crawler.page_category)
                        
                        if products_and_price:
                            data['products_and_price'] = data['products_and_price'] + products_and_price
                            
                
                else:
                    innerHTML = kelebek_mobilya_crawler.KelebekMobilyaCrawler().get_innerHTML(crawler.page_url, css_selector)
                    products_and_price = kelebek_mobilya_crawler.KelebekMobilyaCrawler().html_parser(innerHTML, get_crawler_config, crawler.page_category)
                    
                    if products_and_price:
                        data['products_and_price'] = products_and_price
                
                if data['products_and_price']:
                    document_save = MongoService().insert_one(collection=activity_name, document=data)

                    if document_save:
                        print("Document saved mongodb Kelebek Mob...", datetime.datetime.utcnow())

        except Exception as e:
            print("KelebekMobilyaTasks kelebek_mobilya_crawler_tasks EXCEPTION: {}".format(e))