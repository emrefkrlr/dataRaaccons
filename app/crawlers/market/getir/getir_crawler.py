from crawlers import web_driver_config, functions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import uuid


class GetirCrawler(object):

    def get_innerHTML(self, url, css_selector):
        
        driver = webdriver.Remote(web_driver_config.REMOTE_URL, desired_capabilities=DesiredCapabilities.CHROME)
        
        try:
            
            driver.get(url)
            time.sleep(7)
            get_content = driver.find_element_by_css_selector(css_selector)
            result = get_content.get_attribute('innerHTML')
            driver.quit()
            return result
        
        except Exception as e:
            print("\nGetirCrawler get_innerHTML Exeption: \n{}\nURL: {}".format(e, url))
            

    
    def html_parser(self, html):

        try:
            
            soup = BeautifulSoup(html, 'html.parser')
            first_category = soup.find_all("div", {"class": "style__Item-sc-__sc-v9v4ek-2 gNQDii"})    
            product_list = soup.find_all("div", {"class": "style__Wrapper-sc-__sc-sbxwka-15 fDGESZ sc-2e93b13-0 gTAifC"})
            products_and_price = []
            
            for product in product_list:

                articles = product.find_all("article")                
                category = product.find("h5", {"class": "style__Title5-sc-__sc-1nwjacj-6"})
                
                for article in articles:
                    
                    articleName = article.find("span", {"class": "sc-bb7ebefc-3"})
                    articleMeas = article.find("p", {"class": "style__ParagraphText-sc-__sc-1nwjacj-9"})
                    articlePrice = article.find("span", {"class": "sc-bb7ebefc-5"}).text
                    articleImage = article.find('img')
                    # Replace key character with value character in string
                    articlePrice = functions.char_to_replace(articlePrice)

                    product_detail = {
                        'product_id': str(uuid.uuid4().hex),
                        'sub_category': category.text if category else first_category[1].text,
                        'product_name': articleName.text if articleName.text != "" else None,
                        'product_url': None,
                        'measurement_value': articleMeas.text if articleMeas.text != "" else None,
                        'currency_unit': 'tl',
                        'price': float(articlePrice if articlePrice != "" else None),
                        'image': articleImage['src'] if articleImage else None
                    }
                    products_and_price.append(product_detail)
            
            return products_and_price

        except Exception as e:
            print("\nHTML PARSER Exeption: \n{}".format(e))