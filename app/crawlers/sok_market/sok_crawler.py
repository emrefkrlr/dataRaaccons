from crawlers.scraper import *
from crawlers import functions
import uuid
import json



class SokCrawler(object):

    def get_innerHTML(self, url, page=None):

        if page is not None:

            url = url.format(page)
        
        scraper = Scraper()
        scraper.headers = {
            "store-id": "2359"
        }
        
        try:
 
            response_get = scraper.GET(url=url)

            #time.sleep(5)

            #soup = BeautifulSoup(response_get.text, "lxml")
        
        except Exception as e:

            print("SokCrawler İnnerHtml Error: {}".format(e))

        return response_get if response_get else False

    
    def html_parser(self, html, crawler_config, page_category):

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
        p11 = crawler_config.p11
        p12 = crawler_config.p12
        p13 = crawler_config.p13
        p14 = crawler_config.p14
        products_and_price = []

        body = json.loads(html.content)
        
        try:

            for i in body[eval(p1)][eval(p2)]:
                # get articles
                articleName = i[eval(p3)]
                articleURL = "https://www.sokmarket.com.tr/" + i[eval(p4)] + "-p-" + str(i[eval(p5)])
                articleMeas = i[eval(p6)][eval(p7)]
                articleImage = i[eval(p8)][eval(p9)] + i[eval(p10)][0][eval(p11)]
                articlePrice = float(i[eval(p12)][eval(p13)])
                page_category = i[eval(p14)]
                
                # editing articles
                articleName = articleName.strip()
                page_category = page_category.split("/")
                page_category = page_category[1]

                # assignment articles
                product_detail = {
                    'product_id': str(uuid.uuid4().hex),
                    'category': page_category,
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