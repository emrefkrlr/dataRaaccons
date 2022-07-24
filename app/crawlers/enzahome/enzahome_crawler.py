from crawlers import web_driver_config, functions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import uuid

class EnzaHomeCrawler(object):

    
    def get_innerHTML(self, url, css_selector, page=None):

        try:
        
            driver = webdriver.Remote(web_driver_config.REMOTE_URL, desired_capabilities=DesiredCapabilities.CHROME)
            
            if page is not None:
                url = url.format(page)
                

            driver.get(url)
            time.sleep(7)
            driver.save_screenshot("screenshot.png")
            get_content = driver.find_element(By.CSS_SELECTOR, css_selector)
            result = get_content.get_attribute('innerHTML')
            driver.quit()

            return result if result else None
            
        except Exception as e:
            print("EnzaHomeCrawler get_innerHTML EXCEPTION: {}".format(e))


    def html_parser(self, html, crawler_config, page_category):

        try:

            soup = BeautifulSoup(html, 'html.parser')
            
            p1 = crawler_config.p1.split(",")
            p2 = crawler_config.p2.split(",")
            p3 = crawler_config.p3.split(",")
            p4 = crawler_config.p4.split(",")
            p5 = crawler_config.p5.split(",")
            
            product_list = soup.find_all(eval(p1[0], eval(p1[1])))
            products_and_price = []

            for product in product_list:

                articleName = product.find(eval(p2[0], eval(p2[1])))
                articleNameD = product.find(eval(p3[0], eval(p3[1])))
                articleImage = product.find(eval(p4[0], eval(p4[1])))
                articlePrice = product.find(eval(p5[0], eval(p5[1]))).text.strip()
                articleURL = articleName.findChildren("a" , recursive=False)

                # Replace key character with value character in string
                articlePrice = functions.char_to_replace(functions.clear_price(articlePrice))
                articleName = articleName.text.strip() + ' ' + articleNameD.text.strip()
                
                product_detail = {
                    'product_id': str(uuid.uuid4().hex),
                    'category': page_category,
                    'product_name': articleName if articleName != "" else None,
                    'product_url': 'https://www.enzahome.com.tr' + articleURL[0]['href'] if articleURL else None,
                    'measurement_value': None,
                    'currenct_unit': 'tl',
                    'price': float(articlePrice if articlePrice != "" else None),
                    'image': articleImage['src'] if articleImage else None
                    }
                
                products_and_price.append(product_detail)

            return products_and_price if products_and_price else None

        except Exception as e:
            print("EnzaHomeCrawler html_parser EXCEPTION: {}".format(e))