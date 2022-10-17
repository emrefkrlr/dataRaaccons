from crawlers.service import CrawlerServices
from mongo.services import MongoService
from crawlers.a101 import a101_crawler
import datetime


class A101Tasks(object):

    def a101_crawler_tasks(self, activity_name, activity_category):

        try:

            get_crawler_config = CrawlerServices().get_crawler_config(company="A101", activity=activity_name)

            get_crawlers = CrawlerServices().fetch_urls_to_crawl({"status": 1, 'company__name': 'A101', "activity__name": activity_name, "activity_category__name": activity_category})

            if get_crawlers:

                for crawler in get_crawlers:

                    print("a101_crawler_tasks {} started...".format(crawler.page_url))
                    
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

                    if crawler.page_numbers >= 1:
                        
                        for page in range(1, crawler.page_numbers + 1):

                            innerHTML = a101_crawler.A101Crawler().get_innerHTML(crawler.page_url, page)
                            products_and_price = a101_crawler.A101Crawler().html_parser(innerHTML, get_crawler_config, crawler.page_category)
                            
                            if products_and_price:
                        
                                data['products_and_price'] = data['products_and_price'] + products_and_price
                            
                            else:

                                print("a101_crawler_tasks products_and_price is False...")        
                    
                    else:

                        innerHTML = a101_crawler.A101Crawler().get_innerHTML(crawler.page_url)
                        products_and_price = a101_crawler.A101Crawler().html_parser(innerHTML, get_crawler_config, crawler.page_category)
                        
                        if products_and_price:

                            data['products_and_price'] = products_and_price
                        
                        else:

                            print("a101_crawler_tasks products_and_price is False...")
                    
                    if data['products_and_price']:

                        document_save = MongoService().insert_one(collection=activity_name, document=data)

                        if document_save:
                            print("Document saved mongodb A101...", datetime.datetime.utcnow())
            else:

                print("A101 Activity Category: {} bulunmuyor....".format(activity_category))


        except Exception as e:
            print("A101Tasks a101_crawler_tasks EXCEPTION: {} \n ACTIVITY: {}".format(e, activity_name))