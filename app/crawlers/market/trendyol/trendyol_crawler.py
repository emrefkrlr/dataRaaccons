from crawlers import web_driver_config, functions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import uuid


class TrendyolCrawler(object):

    def get_innerHTML(self, url, css_selector, page):
        
        driver = webdriver.Remote(web_driver_config.REMOTE_URL, desired_capabilities=DesiredCapabilities.CHROME)
        # Hızlı Teslimat
        # https://www.trendyol.com/sr?wc=103809&rd=true&pi=1
        url = url.format(page)
        try:
            driver.get(url)
            time.sleep(5)

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
            driver.quit()
            return result
        
        except Exception as e:
            print("\nget_innerHTML Exeption: \n{}".format(e))
            

    
    def html_parser(self, html):

        try:
            
            soup = BeautifulSoup(html, 'html.parser')
             
            product_list = soup.find_all("div", {"class": "p-card-wrppr"})
            products_and_price = []
            
            for product in product_list:
                
                articleBrand = product.find("span", {"class": "prdct-desc-cntnr-ttl"})
                articleName = product.find("div", {"class": "prdct-desc-cntnr-ttl-w"})
                
                
                name = ''
                if len(articleName)>1:
                    product_name = articleName.find_all("span")
                    
                    for i in range(0, len(product_name)):
                        
                        name = name + product_name[i].text + ' '
                    articleName = name
                else:
                    articleName = articleName.text

                articleMeas_get = name.strip().split(" ")
                articleMeas = articleMeas_get[-2] + " " + articleMeas_get[-1]
                
                articleImage = product.find("img")
                articlePrice = product.find("div", {"class": "prc-box-dscntd"}).text.strip()
               # Replace key character with value character in string
                articlePrice = functions.char_to_replace(articlePrice)
                
                product_detail = {
                    'product_id': str(uuid.uuid4().hex),
                    'category': 'None',
                    'brand': articleBrand.text.strip() if articleBrand.text != "" else None,
                    'product_name': articleName.strip() if articleName != "" else None,
                    'measurement_value': articleMeas if articleMeas != "" else None,
                    'currenct_unit': 'tl',
                    'price': float(articlePrice if articlePrice != "" else None),
                    'image': articleImage['src'] if articleImage else None
                    }
                
                products_and_price.append(product_detail)
                                            
                    
            
            return products_and_price

        except Exception as e:
            print("\nHTML PARSER Exeption: \n{}".format(e))