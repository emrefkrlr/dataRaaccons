from math import prod
from crawlers.scraper import *
from crawlers import functions
import uuid
import json

class MigrosCrawler(object):

    def get_innerHTML(self, url, page=None):

        if page is not None:

            url = url.format(page)

        scraper = Scraper()
        
        try:

            response_get = scraper.GET(url=url)

            #time.sleep(5)

            #soup = BeautifulSoup(response_get.text, "lxml")
        
        except Exception as e:

            print("MigrosCrawler İnnerHtml Error: {}".format(e))

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
        p15 = crawler_config.p15
        products_and_price = []

        body = json.loads(html.content)

        products = body[eval(p1)][eval(p2)]

        try:

            for product in products:
                
                # get articles
                articleName = product[eval(p3)]
                articleURL = "https://www.migros.com.tr/" + product[eval(p4)]
                articleImage = product[eval(p5)][0][eval(p6)][eval(p7)]
                sub_category = product[eval(p14)][eval(p15)]
                
                if len(product[eval(p8)])>0:
                    
                    articlePrice = float(functions.char_to_replace(functions.clear_price_text(product[eval(p8)][0][eval(p9)])))

                else:

                    articlePrice = float(product[eval(p10)]/100)

                if articleName:
                        
                    articleMeas_get = articleName.strip().split(" ")

                    if len(articleMeas_get)>1:

                        articleMeas = str(articleMeas_get[-2]) + " " + str(articleMeas_get[-1])

                    else:

                        articleMeas = product[eval(p11)][eval(p12)][eval(p13)]
                        
                # assignment articles
                product_detail = {
                    'product_id': str(uuid.uuid4().hex),
                    'sub_category': sub_category,
                    'product_name': articleName,
                    'product_url': articleURL,
                    'measurement_value': articleMeas,
                    'currenct_unit': 'tl',
                    'price': articlePrice,
                    'image': articleImage
                }

                products_and_price.append(product_detail)

        except Exception as e:
            print("MigrosCrawler Articles error: {}".format(e))
        
        return products_and_price if products_and_price else False
