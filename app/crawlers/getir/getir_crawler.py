from crawlers import web_driver_config, functions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import uuid

class GetirCrawler(object):

    def get_innerHTML(self, url, css_selector):

        driver = webdriver.Remote(web_driver_config.REMOTE_URL, desired_capabilities=DesiredCapabilities.CHROME)
        
        try:
            
            driver.get(url)
            time.sleep(5)
            get_content = driver.find_element_by_css_selector(css_selector)
            result = get_content.get_attribute('innerHTML')
            driver.quit()

            return result
        
        except Exception as e:
            print("GetirCrawler get_innerHTML EXCEPTION: {}".format(e))

    
    def html_parser(self, html, crawler_config):

        try:
            
            soup = BeautifulSoup(html, 'html.parser')

            p1 = crawler_config.p1.split(",")
            p2 = crawler_config.p2.split(",")
            p3 = crawler_config.p3
            p4 = crawler_config.p4.split(",")
            p5 = crawler_config.p5.split(",")
            p6 = crawler_config.p6.split(",")
            p7 = crawler_config.p7.split(",")
            p8 = crawler_config.p8
            
            first_category = soup.find_all(eval(p1[0]), eval(p1[1])) 
            product_list = soup.find_all(eval(p2[0]), eval(p2[1]))
            products_and_price = []
            
            for product in product_list:

                articles = product.find_all(eval(p3))
                category = product.find(eval(p4[0]), eval(p4[1]))
                
                for article in articles:
                    
                    articleName = article.find(eval(p5[0]), eval(p5[1]))
                    articleMeas = article.find(eval(p6[0]), eval(p6[1]))
                    articlePrice = article.find(eval(p7[0]), eval(p7[1])).text
                    articleImage = article.find(eval(p8))
                    # Replace key character with value character in string
                    articlePrice = functions.char_to_replace(articlePrice)


                    product_detail = {
                        'product_id': str(uuid.uuid4().hex),
                        'sub_category': category.text if category else first_category[1].text,
                        'product_name': articleName.text if articleName.text != "" else None,
                        'product_url': None,
                        'measurement_value': articleMeas.text if articleMeas.text != "" else None,
                        'currency_unit': 'tl',
                        'price': float(articlePrice if articlePrice != "" else None),
                        'image': articleImage['src'] if articleImage else None
                    }
                    products_and_price.append(product_detail)
                
          
            if products_and_price:
                return products_and_price

        except Exception as e:
            print("GetirCrawler html_parser EXCEPTION: {}".format(e))