from crawlers import web_driver_config, functions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import uuid


class BellonaCrawler(object):

    def get_innerHTML(self, url, css_selector, page=None):

        try:

            driver = webdriver.Remote(web_driver_config.REMOTE_URL, desired_capabilities=DesiredCapabilities.FIREFOX)
            if page is not None:
                url = url.format(page)

            driver.get(url)
            time.sleep(3)
            get_content = driver.find_element(By.CSS_SELECTOR, css_selector)
            result = get_content.get_attribute('innerHTML')
            driver.quit()
            
            return result if result else None

        except Exception as e:
            print("BellonaCrawler get_innerHTML EXCEPTION: {}".format(e))


    def html_parser(self, html, crawler_config, page_category):

        try:

            soup = BeautifulSoup(html, 'html.parser')

            p1 = crawler_config.p1.split(",")
            p2 = crawler_config.p2.split(",")
            p3 = crawler_config.p3.split(",")
            p4 = crawler_config.p4
            p5 = crawler_config.p5.split(",")

            product_list = soup.find_all(eval(p1[0]), eval(p1[1]))
            products_and_price = []

            for product in product_list:
                    
                articleName = product.find(eval(p2[0]), eval(p2[1]))
                articleURL = product.find(eval(p3[0]), eval(p3[1]))
                articleMeas = None
                articleImage = product.find(eval(p4))
                articlePrice = product.find(eval(p5[0]), eval(p5[1])).text.strip()
                
                # Replace key character with value character in string
                articlePrice = functions.char_to_replace(articlePrice)
                    
                product_detail = {
                    'product_id': str(uuid.uuid4().hex),
                    'sub_category': page_category,
                    'product_name': articleName.text.strip() if articleName.text != "" else None,
                    'product_url': 'https://www.bellona.com.tr' + articleURL['href'] if articleURL else None,
                    'measurement_value': articleMeas if articleMeas != "" else None,
                    'currenct_unit': 'tl',
                    'price': float(articlePrice if articlePrice != "" else None),
                    'image': articleImage['src'] if articleImage else None
                }
                    
                products_and_price.append(product_detail)

            return products_and_price if products_and_price else None

        except Exception as e:
            print("BellonaCrawler html_parser EXCEPTION: {}".format(e))

