from crawlers import web_driver_config, functions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import uuid


class MigrosCrawler(object):

    def get_innerHTML(self, url, css_selector, page=None):

        driver = webdriver.Remote(web_driver_config.REMOTE_URL, desired_capabilities=DesiredCapabilities.CHROME)
        if page is not None:
            url = url.format(page)
        

        print(url)
        try:
            
            driver.get(url)
            time.sleep(5)
            get_content = driver.find_element_by_css_selector(css_selector)
            result = get_content.get_attribute('innerHTML')
            driver.quit()
            return result
        
        except Exception as e:
            print("\nMigrosCrawler get_innerHTML Exeption: \n{}\nURL: {}".format(e, url))
            

    
    def html_parser(self, html, page_category):

        try:
            
            soup = BeautifulSoup(html, 'html.parser') 
            product_list = soup.find_all("mat-card")
            products_and_price = []
            
            for product in product_list:
                
                articleName = product.find("a", {"class": "product-name"})
                articleURL = product.find("a")
                articleMeas_get = articleName.text.strip().split(" ")
                articleMeas = articleMeas_get[-2] + " " + articleMeas_get[-1]
                articleImage = product.find("img", {"class": "ng-star-inserted"})
                articlePrice = product.find("span", {"class": "amount"}).text.strip()
                # Replace key character with value character in string
                articlePrice = functions.char_to_replace(articlePrice)
                
                product_detail = {
                    'product_id': str(uuid.uuid4().hex),
                    'sub_category': page_category,
                    'product_name': articleName.text.strip() if articleName.text != "" else None,
                    'product_url': 'https://www.migros.com.tr' + articleURL['href'] if articleURL else None,
                    'measurement_value': articleMeas if articleMeas != "" else None,
                    'currenct_unit': 'tl',
                    'price': float(articlePrice if articlePrice != "" else None),
                    'image': articleImage['src'] if articleImage else None
                    }
                
                products_and_price.append(product_detail)
                                            
            return products_and_price

        except Exception as e:
            print("\nMigrosCrawler html_parser Exeption: \n{}".format(e))