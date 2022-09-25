from crawlers.scraper import *
from crawlers import functions
import uuid
import json

class GetirCrawler(object):

    def get_innerHTML(self, url, page=None):

        if page is not None:

            url = url.format(page)
        
        scraper = Scraper()
        cookies={
            "language": "tr"
        }
        
        try:

            response_get = scraper.GET(url=url, cookies=cookies)

            #time.sleep(5)

            #soup = BeautifulSoup(response_get.text, "lxml")
        
        except Exception as e:

            print("MetroMarketCrawler İnnerHtml Error: {}".format(e))

        return response_get if response_get else False

    
    def html_parser(self, html, crawler_config):

        p1 = crawler_config.p1
        p2 = crawler_config.p2
        p3 = crawler_config.p3
        p4 = crawler_config.p4
        p5 = crawler_config.p5
        p6 = crawler_config.p6
        p7 = crawler_config.p7
        p8 = crawler_config.p8
        p9 = crawler_config.p9
        p10 = crawler_config.p10
        products_and_price = []

        body = json.loads(html.content)

        try:

            sub_categories = body["data"]["category"]["subCategories"]

            for sub_category in sub_categories:

                sub_category_name = sub_category["name"]

                products = sub_category["products"]

                for product in products:
                    # get articles
                    articleName = product["name"]
                    articleURL = "https://getir.com/urun/" + product["slug"]
                    articleMeas = product["shortDescription"]
                    articleImage = product["squareThumbnailURL"]
                    articlePrice = product["price"]

                    # assignment articles
                    product_detail = {
                        'product_id': str(uuid.uuid4().hex),
                        'category': sub_category_name,
                        'product_name': articleName,
                        'product_url': articleURL,
                        'measurement_value': articleMeas,
                        'currenct_unit': 'tl',
                        'price': articlePrice,
                        'image': articleImage
                    }

                    products_and_price.append(product_detail)
        
        except Exception as e:
            print("Articles error: {}".format(e))
    
        return products_and_price if products_and_price else False