from crawlers import web_driver_config, functions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import uuid


class IsteGelsinCrawler(object):

    def get_innerHTML(self, url, css_selector):
        
        driver = webdriver.Remote(web_driver_config.REMOTE_URL, desired_capabilities=DesiredCapabilities.FIREFOX)
        
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
            print("\nget_innerHTML Exeption: \n{}".format(e))
            

    
    def html_parser(self, html):

        try:
            
            soup = BeautifulSoup(html, 'html.parser')
             
            product_list = soup.find_all("div", {"class": "product-card"})
            products_and_price = []
            
            for product in product_list:
                
                articleName = product.find("span", {"class": "product-name"})
                articleURL = product.find("a")
                articleMeas_get = articleName.text.strip().split(" ")
                articleMeas = articleMeas_get[-2] + " " + articleMeas_get[-1]
                articleImage = product.find("img")
                articlePrice = product.find("span", {"class": "discountless-price"}).text.strip()
                # Replace key character with value character in string
                articlePrice = functions.char_to_replace(articlePrice)
                
                product_detail = {
                    'product_id': str(uuid.uuid4().hex),
                    'category': 'None',
                    'product_name': articleName.text.strip() if articleName.text != "" else None,
                    'product_url': articleURL['href'] if articleURL else None,
                    'measurement_value': articleMeas if articleMeas != "" else None,
                    'currenct_unit': 'tl',
                    'price': float(articlePrice if articlePrice != "" else None),
                    'image': articleImage['src'] if articleImage else None
                    }
                
                products_and_price.append(product_detail)
                                            
                    
            
            return products_and_price

        except Exception as e:
            print("\nHTML PARSER Exeption: \n{}".format(e))