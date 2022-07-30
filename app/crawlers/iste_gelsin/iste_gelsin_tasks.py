from crawlers.service import CrawlerServices
from crawlers.iste_gelsin import iste_gelsin_crawler
from mongo.services import MongoService
import datetime


class IsteGelsinTasks(object):

    def iste_gelsin_crawler_tasks(self, activity_name):

        try:

            get_crawler_config = CrawlerServices().get_crawler_config(company="iste_gelsin", activity=activity_name)

            get_crawlers = CrawlerServices().fetch_urls_to_crawl({"status": 1, 'company__name': 'iste_gelsin', "activity__name": activity_name})

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

                innerHTML = iste_gelsin_crawler.IsteGelsinCrawler().get_innerHTML(crawler.page_url, css_selector)
                products_and_price = iste_gelsin_crawler.IsteGelsinCrawler().html_parser(innerHTML, get_crawler_config, crawler.page_category)
                data['products_and_price'] = products_and_price

                if data['products_and_price']:
                    document_save = MongoService().insert_one(collection=activity_name, document=data)

                    if document_save:
                        print("Document saved mongodb...", datetime.datetime.utcnow())

        except Exception as e:
            print("HepsiburadaTasks hepsiburada_crawler_tasks EXCEPTION: {} \n ACTIVITY: {}".format(e, activity_name))