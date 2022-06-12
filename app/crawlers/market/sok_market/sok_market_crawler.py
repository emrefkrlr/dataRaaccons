from crawlers import web_driver_config, functions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import uuid


class SokMarketCrawler(object):

    def get_innerHTML(self, url, css_selector):
        
        driver = webdriver.Remote(web_driver_config.REMOTE_URL, desired_capabilities=DesiredCapabilities.FIREFOX)
        
        try:
            
            driver.get(url)
            time.sleep(5)
            get_content = driver.find_element_by_css_selector(css_selector)
            result = get_content.get_attribute('innerHTML')
            driver.quit()
            return result
        
        except Exception as e:
            print("\nSokMarketCrawler get_innerHTML Exeption: \n{}\nURL: {}".format(e, url))
            

    
    def html_parser(self, html, page_category):

        try:
            
            soup = BeautifulSoup(html, 'html.parser')
            product_list = soup.find_all("li")
            products_and_price = []
            
            for product in product_list:
                
                articleName = product.find("strong", {"class": "content-title"})
                articleURL = product.find("a")
                articleMeas_get = articleName.text.strip().split(" ")
                articleMeas = articleMeas_get[-2] + " " + articleMeas_get[-1]

                articleImage = product.find("div", {"class": "imagewrap-image"})
                
                if articleImage.get('style'):
                    articleImage = product.find("div", {"class": "imagewrap-image"}).get('style').split('"')
                    articleImage = articleImage[1]
                
                articlePrice = product.find("div", {"class": "content-prices"})
                
                if len(articlePrice)> 1:
                    articlePrice = articlePrice.find_all("span")
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
                                            
                    
            
            return products_and_price

        except Exception as e:
            print("\nSokMarketCrawler html_parser Exeption: \n{}".format(e))