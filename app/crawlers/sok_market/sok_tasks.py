from crawlers.service import CrawlerServices
from crawlers.sok_market import sok_crawler
from mongo.services import MongoService
import datetime
import time

class SokMarketTasks(object):

    def sok_crawler_tasks(self, activity_name):

        try:

            get_crawler_config = CrawlerServices().get_crawler_config(company="sok_market", activity=activity_name)

            get_crawlers = CrawlerServices().fetch_urls_to_crawl({"status": 1, 'company__name': 'sok_market', "activity__name": activity_name})

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

                data['products_and_price'] = []
                css_selector = get_crawler_config.css_selector.replace(" ", ".")

                innerHTML = sok_crawler.SokCrawler().get_innerHTML(crawler.page_url, css_selector)
                products_and_price = sok_crawler.SokCrawler().html_parser(innerHTML, get_crawler_config, crawler.page_category)
                data['products_and_price'] = products_and_price

                if data['products_and_price']:
                    document_save = MongoService().insert_one(collection=activity_name, document=data)

                    if document_save:
                        print("Document saved mongodb...", datetime.datetime.utcnow())

        except Exception as e:
            print("SokCrawlers sok_crawler_tasks EXCEPTION: {}".format(e))