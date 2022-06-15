from crawlers import web_driver_config, functions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import uuid


class HepsiburadaCrawler(object):

    def get_innerHTML(self, url, css_selector, page=None):
        
        driver = webdriver.Remote(web_driver_config.REMOTE_URL, desired_capabilities=DesiredCapabilities.FIREFOX)
        # Hızlı Teslimat
        if page is not None:
            url = url.format(page)
        
        try:
            
            driver.get(url)
            time.sleep(2)

            """
            previous_height = driver.execute_script(' return document.body.scrollHeight')
            
            while True:
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                time.sleep(3)
                new_height = driver.execute_script('return document.body.scrollHeight')
                
                if new_height == previous_height:
                    break

                previous_height = new_height
                
            """
            get_content = driver.find_element_by_css_selector(css_selector)
            result = get_content.get_attribute('innerHTML')
            print(url)
            driver.quit()
            return result
        
        except Exception as e:
            print("\n HepsiburadaCrawler get_innerHTML Exeption: \n{}\nURL: {}".format(e, url))
            

    
    def html_parser(self, html, page_category):

        try:
            
            soup = BeautifulSoup(html, 'html.parser')
             
            product_list = soup.find_all("li", {"class": "productListContent-item"})
            products_and_price = []
            
            if product_list is not None and len(product_list) > 0:

                for product in product_list:
                    
                    articleBrand = None
                    articleName = product.find("h3").text
                    articleURL = product.find("a")
                    articleMeas = None
                    articleImage = product.find("img")
                    articlePrice = product.find("div", {"data-test-id": "price-current-price"}).text

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
            print("\n HepsiburadaCrawler html_parser Exeption: \n{}".format(e))