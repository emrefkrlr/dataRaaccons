from crawlers.scraper import *
from crawlers import functions
import uuid


class MetroMarketCrawler(object):

    def get_innerHTML(self, url, page=None):

        if page is not None:

            url = url.format(page)
    
        scraper = Scraper()
        
        try:
            response_get = scraper.GET(url=url)

            time.sleep(5)

            soup = BeautifulSoup(response_get.text, "lxml")
        
        except Exception as e:

            print("MetroMarketCrawler İnnerHtml Error: {}".format(e))

        return soup if soup else False

    
    def html_parser(self, html, crawler_config, page_category):

        css_selector = crawler_config.css_selector.split(",")
        p1 = crawler_config.p1.split(",")
        p2 = crawler_config.p2.split(",")
        p3 = crawler_config.p3.split(",")
        p4 = crawler_config.p4.split(",")
        p5 = crawler_config.p5
        p6 = crawler_config.p6.split(",")
        products_and_price = []

        # get product list
        try:

            content = html.find(eval(css_selector[0]), eval(css_selector[1]))
            products = content.find_all(eval(p1[0]), eval(p1[1]))

        except (TypeError, KeyError) as e:

            print("Product list not found : {}".format(e))

        for product in products:
            # get articles
            try:

                articleName = product.find(eval(p2[0]), eval(p2[1]))
                articleURL = product.find(eval(p3[0]), eval(p3[1]))
                articleMeas = product.find(eval(p4[0]), eval(p4[1]))
                articleImage = product.find(eval(p5))
                articlePrice = product.find(eval(p6[0]), eval(p6[1]))

            except AttributeError as e:

                print("Articles error: {}".format(e))

            try:
                # editing articles
                articleName = articleName.text.strip() if articleName else None
                articleMeas = articleMeas.text.strip() if articleMeas else None
                articleURL = articleURL["href"] if articleURL else "None"
                
                # Replace key character with value character in string
                articlePrice = float(functions.char_to_replace(functions.clear_price_text(articlePrice.text))) if articlePrice else None

                try:
        
                    articleImage = articleImage["src"]

                except (AttributeError, TypeError, KeyError) as e:
                    articleImage = None

            except Exception as e:

                print("Editing articles error: {}".format(e))

            # assignment articles
            product_detail = {
                'product_id': str(uuid.uuid4().hex),
                'sub_category': page_category,
                'product_name': articleName,
                'product_url': 'https://online.metro-tr.com' + articleURL,
                'measurement_value': articleMeas,
                'currenct_unit': 'tl',
                'price': articlePrice,
                'image': articleImage
            }

            products_and_price.append(product_detail)

            print(product_detail)
        
        return products_and_price if products_and_price else False
