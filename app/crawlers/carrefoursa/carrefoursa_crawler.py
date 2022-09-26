from crawlers.scraper import *
from crawlers import functions
import uuid


class CarrefoursaCrawler(object):

    def get_innerHTML(self, url, page=None):

        if page is not None:

            url = url.format(page)

        scraper = Scraper()

        try:

            response_get = scraper.GET(url=url)

            time.sleep(5)

            soup = BeautifulSoup(response_get.text, "lxml")

        except Exception as e:
            
            print("CarrefoursaCrawler İnnerHtml Error: {}".format(e))

        return soup if soup else False
    

    def html_parser(self, html, crawler_config, page_category):

        css_selector = crawler_config.css_selector.split(",")
        p1 = crawler_config.p1.split(",")
        p2 = crawler_config.p2.split(",")
        p3 = crawler_config.p3
        p4 = crawler_config.p4.split(",")
        p5 = crawler_config.p5
        products_and_price = []

        # get product list
        try:

            content = html.find(eval(css_selector[0]), eval(css_selector[1]))            
            products = content.find_all(eval(p1[0]), eval(p1[1]))

        except (TypeError, KeyError) as e:

            print("CarrefoursaCrawler Product list not found : {}".format(e))

        for product in products:
            # get articles
            try:

                articleName = product.find(eval(p2[0]), eval(p2[1]))
                articleImage = product.find(eval(p3))
                articlePrice = product.find(eval(p4[0]), eval(p4[1]))
                articleURL = product.find(eval(p5))
                
            except AttributeError as e:

                print("CarrefoursaCrawler Articles error: {}".format(e))

            try:
                # editing articles
                articleName = articleName.text.strip() if articleName else None
                articleImage = articleImage["src"] if articleImage else None
                articleURL = articleURL["href"] if articleURL else "None"

                if articleName:
                    
                    articleMeas_get = articleName.strip().split(" ")

                    if len(articleMeas_get)>1:

                        articleMeas = str(articleMeas_get[-2]) + " " + str(articleMeas_get[-1])

                    else:

                        articleMeas = None

                # Replace key character with value character in string
                articlePrice = float(functions.char_to_replace(articlePrice.text)) if articlePrice else None
            
            except Exception as e:

                print("CarrefoursaCrawler Editing articles error: {}".format(e))

            # assignment articles
            product_detail = {
                'product_id': str(uuid.uuid4().hex),
                'category': page_category,
                'product_name': articleName,
                'product_url': 'https://www.carrefoursa.com' + articleURL,
                'measurement_value': articleMeas,
                'currenct_unit': 'tl',
                'price': articlePrice,
                'image': articleImage
            }

            products_and_price.append(product_detail)
    
        return products_and_price if products_and_price else False