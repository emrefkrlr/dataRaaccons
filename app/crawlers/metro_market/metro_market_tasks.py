from crawlers.service import CrawlerServices
from crawlers.metro_market import metro_market_crawler
from mongo.services import MongoService
import datetime


class MetroMarketTasks(object):

    def metro_market_tasks(self, activity_name, activity_category):
        
        get_crawler_config = CrawlerServices().get_crawler_config(company="metro_market", activity=activity_name)

        get_crawlers = CrawlerServices().fetch_urls_to_crawl({"status": 1, 'company__name': 'metro_market', "activity__name": activity_name, "activity_category__name": activity_category})

        if get_crawlers:

            for crawler in get_crawlers:

                print("metro_market_tasks {} started...".format(crawler.page_url))
                    
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

                if crawler.page_numbers >= 1:

                    for page in range(1, crawler.page_numbers + 1):

                        innerHTML = metro_market_crawler.MetroMarketCrawler().get_innerHTML(crawler.page_url, page)
                        products_and_price = metro_market_crawler.MetroMarketCrawler().html_parser(innerHTML, get_crawler_config, crawler.page_category) if innerHTML else False
                            
                        if products_and_price:

                            data['products_and_price'] = data['products_and_price'] + products_and_price
                        
                        else:

                            print("metro_market_tasks products_and_price is False...")
                                                    
                else:
                        
                    innerHTML = metro_market_crawler.MetroMarketCrawler().get_innerHTML(crawler.page_url)
                    products_and_price = metro_market_crawler.MetroMarketCrawler().html_parser(innerHTML, get_crawler_config, crawler.page_category) if innerHTML else False
                        
                    if products_and_price:
                            
                        data['products_and_price'] = products_and_price
                    
                    else:

                        print("metro_market_tasks products_and_price is False...")
                    
                if data['products_and_price']:
                    
                    document_save = MongoService().insert_one(collection=activity_name, document=data)

                    if document_save:
                        
                        print("Document saved mongodb MetroMarket...", datetime.datetime.utcnow())
        else:

            print("MetroMarket Activity Category: {} bulunmuyor....".format(activity_category))

