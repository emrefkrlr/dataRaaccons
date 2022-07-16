from crawlers import web_driver_config, functions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import uuid


class IsteGelsinCrawler(object):

    def get_innerHTML(self, url, css_selector):
        
        driver = webdriver.Remote(web_driver_config.REMOTE_URL, desired_capabilities=DesiredCapabilities.CHROME)
        
        try:
            driver.get(url)
            time.sleep(5)
            previous_height = driver.execute_script(' return document.body.scrollHeight')
            
            while True:
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                time.sleep(3)
                new_height = driver.execute_script('return document.body.scrollHeight')
                
                if new_height == previous_height:
                    break

                previous_height = new_height

            get_content = driver.find_element_by_css_selector(css_selector)
            result = get_content.get_attribute('innerHTML')
            driver.quit()

            return result
        
        except Exception as e:
            print("IsteGelsinCrawler get_innerHTML EXCEPTION: \n{}\nURL: {}".format(e, url))
            

    
    def html_parser(self, html, crawler_config,page_category):

        try:
            
            soup = BeautifulSoup(html, 'html.parser')

            p1 = crawler_config.p1.split(",")
            p2 = crawler_config.p2.split(",")
            p3 = crawler_config.p3
            p4 = crawler_config.p4
            p5 = crawler_config.p5.split(",")
             
            product_list = soup.find_all(eval(p1[0]), eval(p1[1]))
            products_and_price = []
            
            for product in product_list:
                
                articleName = product.find(eval(p2[0]), eval(p2[1]))
                articleURL = product.find(eval(p3))
                articleMeas_get = articleName.text.strip().split(" ")
                articleMeas = articleMeas_get[-2] + " " + articleMeas_get[-1]
                articleImage = product.find(eval(p4))
                articlePrice = product.find(eval(p5[0]), eval(p5[1])).text.strip()
                # Replace key character with value character in string
                articlePrice = functions.char_to_replace(articlePrice)
                
                product_detail = {
                    'product_id': str(uuid.uuid4().hex),
                    'sub_category': page_category,
                    'product_name': articleName.text.strip() if articleName.text != "" else None,
                    'product_url': 'https://www.istegelsin.com/' + articleURL['href'] if articleURL else None,
                    'measurement_value': articleMeas if articleMeas != "" else None,
                    'currenct_unit': 'tl',
                    'price': float(articlePrice if articlePrice != "" else None),
                    'image': articleImage['src'] if articleImage else None
                    }
                
                products_and_price.append(product_detail)

            
            return products_and_price if products_and_price else None

        except Exception as e:
            print("IsteGelsinCrawler html_parser EXCEPTION: \n{}".format(e))