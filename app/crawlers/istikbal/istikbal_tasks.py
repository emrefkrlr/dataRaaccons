from crawlers.service import CrawlerServices
from mongo.services import MongoService
from crawlers.istikbal import istikbal_crawler
import datetime
import time


class IstikbalTasks(object):

    def istikbal_crawler_tasks(self, activity_name):

        try:

            get_crawler_config = CrawlerServices().get_crawler_config(company="bellona", activity=activity_name)

            get_crawlers = CrawlerServices().fetch_urls_to_crawl({"status": 1, 'company__name': 'bellona', "activity__name": activity_name})

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
                        
                        innerHTML = istikbal_crawler.IstikbalCrawler().get_innerHTML(crawler.page_url, css_selector, page)
                        
                        products_and_price = istikbal_crawler.IstikbalCrawler().html_parser(innerHTML, get_crawler_config, crawler.page_category)

                        if products_and_price:
                            data['products_and_price'] = data['products_and_price'] + products_and_price


                else:
                    
                    innerHTML = istikbal_crawler.IstikbalCrawler().get_innerHTML(crawler.page_url, css_selector, page)
                    products_and_price = istikbal_crawler.IstikbalCrawler().html_parser(innerHTML, get_crawler_config, crawler.page_category)
                    
                    if products_and_price:

                        data['products_and_price'] = products_and_price
                
                if data['products_and_price']:
                    document_save = MongoService().insert_one(collection=activity_name, document=data)

                    if document_save:
                        print("Document saved mongodb İstikbal...", datetime.datetime.utcnow())

        except Exception as e:
            print("IstikbalTasks istikbal_crawler_tasks EXCEPTION: {} \n ACTIVITY: {}".format(e, activity_name))