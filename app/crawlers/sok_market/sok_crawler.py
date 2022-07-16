from crawlers import web_driver_config, functions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import uuid


class SokCrawler(object):

    def get_innerHTML(self, url, css_selector):

        try:

            driver = webdriver.Remote(web_driver_config.REMOTE_URL, desired_capabilities=DesiredCapabilities.FIREFOX)
            driver.get(url)
            time.sleep(5)
            get_content = driver.find_element_by_css_selector(css_selector)
            result = get_content.get_attribute('innerHTML')
            driver.quit()
            
            return result

        except Exception as e:
            print("SokCrawler get_innerHTML EXCEPTION: {}".format(e))

    
    def html_parser(self, html, crawler_config, page_category):

        try:

            soup = BeautifulSoup(html, 'html.parser')
            p1 = crawler_config.p1
            p2 = crawler_config.p2.split(",")
            p3 = crawler_config.p3
            p4 = crawler_config.p4.split(",")
            p5 = crawler_config.p5
            p6 = crawler_config.p6.split(",")
            p7 = crawler_config.p7
            p8 = crawler_config.p8.split(",")
            p9 = crawler_config.p9

            product_list = soup.find_all(eval(p1))
            products_and_price = []
            
            for product in product_list:
                
                articleName = product.find(eval(p2[0]), eval(p2[1]))
                articleURL = product.find(eval(p3))
                articleMeas_get = articleName.text.strip().split(" ")
                articleMeas = articleMeas_get[-2] + " " + articleMeas_get[-1]

                articleImage = product.find(eval(p4[0]), eval(p4[1]))
                
                if articleImage.get(eval(p5)):
                    articleImage = product.find(eval(p6[0]), eval(p6[1])).get(eval(p7)).split('"')
                    articleImage = articleImage[1]
                
                articlePrice = product.find(eval(p8[0]), eval(p8[1]))
                
                if len(articlePrice)> 1:
                    articlePrice = articlePrice.find_all(eval(p9))
                    articlePrice = articlePrice[1].text    
                else:
                    articlePrice = articlePrice.text

                # Replace key character with value character in string
                articlePrice = functions.char_to_replace(articlePrice)
                
                product_detail = {
                    'product_id': str(uuid.uuid4().hex),
                    'sub_category': page_category,
                    'product_name': articleName.text.strip() if articleName.text != "" else None,
                    'product_url': 'https://www.sokmarket.com.tr' + articleURL['href'] if articleURL else None,
                    'measurement_value': articleMeas if articleMeas != "" else None,
                    'currenct_unit': 'tl',
                    'price': float(articlePrice if articlePrice != "" else None),
                    'image': articleImage if articleImage else None
                    }
                
                products_and_price.append(product_detail)

           
            return products_and_price if products_and_price else None

        except Exception as e:
            print("SokCrawler html_parser EXCEPTION: {}".format(e))