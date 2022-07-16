from crawlers import web_driver_config, functions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import uuid


class HepsiburadaCrawler(object):

    def get_innerHTML(self, url, css_selector, page=None):

        try:

            driver = webdriver.Remote(web_driver_config.REMOTE_URL, desired_capabilities=DesiredCapabilities.FIREFOX)

            if page is not None:
                url = url.format(page)
            
            driver.get(url)
            time.sleep(2)

            
            get_content = driver.find_element_by_css_selector(css_selector)
            result = get_content.get_attribute('innerHTML')
            print(url)
            driver.quit()
            
            return result
        
        except Exception as e:
            print("\n HepsiburadaCrawler get_innerHTML EXCEPTION: {}".format(e))
            

    
    def html_parser(self, html, crawler_config, page_category):

        try:
            
            soup = BeautifulSoup(html, 'html.parser')

            p1 = crawler_config.p1.split(",")
            p2 = crawler_config.p2
            p3 = crawler_config.p3
            p4 = crawler_config.p4
            p5 = crawler_config.p5.split(",")
             
            product_list = soup.find_all(eval(p1[0]), eval(p1[1]))
            products_and_price = []
            
            if product_list is not None and len(product_list) > 0:

                for product in product_list:
                    
                    articleBrand = None
                    articleName = product.find(eval(p2)).text
                    articleURL = product.find(eval(p3))
                    articleMeas = None
                    articleImage = product.find(eval(p4))
                    articlePrice = product.find(eval(p5[0]), eval(p5[1])).text

                # Replace key character with value character in string
                    articlePrice = functions.char_to_replace(articlePrice)
                    
                    product_detail = {
                        'product_id': str(uuid.uuid4().hex),
                        'sub_category': page_category,
                        'brand': articleBrand if articleBrand != "" else None,
                        'product_name': articleName.strip() if articleName != "" else None,
                        'product_url': 'https://www.hepsiburada.com' + articleURL['href'] if articleURL else None,
                        'measurement_value': articleMeas if articleMeas != "" else None,
                        'currenct_unit': 'tl',
                        'price': float(articlePrice.strip() if articlePrice != "" else None),
                        'image': articleImage['src'] if articleImage else None
                        }
                    
                    products_and_price.append(product_detail)

            else:

                print("Product List Null")                          
                    
            return products_and_price

        except Exception as e:
            print("HepsiburadaCrawler html_parser EXCEPTION: {}".format(e))