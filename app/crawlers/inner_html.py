from crawlers import web_driver_config, functions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from crawlers.service import CrawlerServices
import time
from bs4 import BeautifulSoup
import uuid


class GetInnerHtml(object):

    def get_driver(self, browser_name):

        try:

            ua = UserAgent()
            userAgent = ua.random

            web_driver = CrawlerServices().get_web_driver_address()

            if browser_name == "chrome":

                opts = Options()
                opts.add_argument("user-agent={}".format(userAgent))
                driver = webdriver.Remote(web_driver, desired_capabilities=DesiredCapabilities.CHROME, options=opts)

            else:

                profile = webdriver.FirefoxProfile()
                profile.set_preference("general.useragent.override", userAgent)
                driver = webdriver.Remote(web_driver, desired_capabilities=DesiredCapabilities.FIREFOX, browser_profile=profile)

            agent = driver.execute_script("return navigator.userAgent")

            print("User Agent: {}".format(agent))
            
            return driver

        except Exception as e:
            print("GetInnerHtml get_driver Exception: {}".format(e))


    def get_inner_html_for_one_page(self, browser, css_selector, url):

        driver = self.get_driver(browser_name=browser)
        driver.get(url)
        try_to = 0

        while try_to < 3:

            try:

                get_content = driver.find_element(By.CSS_SELECTOR, css_selector)
                html_content = get_content.get_attribute('innerHTML')
                try_to = 3
                driver.quit()

                return html_content

            except Exception as e:

                driver.refresh()
                try_to += 1
                print("get_inner_html_for_one_page Exception: {}\nUrl: {}\nCSS_SELECTOR: {}\nTry: {}".format(e, url, css_selector, try_to))
                
            
        driver.quit()
        return False


    def get_inner_html_for_button_paginations(self, browser, css_selector, url, next_page_element, page):

        driver = self.get_driver(browser_name=browser)
        driver.get(url)
        driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
        
        try_to = 0
        html_content = []
        
        for p in range(1, page + 1):

            
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, css_selector)))

            while try_to < 3:

                try:

                    get_content = driver.find_element(By.CSS_SELECTOR, css_selector)
                    html = get_content.get_attribute('innerHTML')
                    html_content.append(html)
                    try_to = 3
                    
                except NoSuchElementException:

                    driver.refresh()
                    try_to += 1
                    print("get_inner_html_for_button_paginations Exception: {}\nUrl: {}\nCSS_SELECTOR: {}\nTry: {}".format(e, url, css_selector, try_to))

            try:
                    
                WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, next_page_element)))
                next_page_element = driver.find_element(By.CSS_SELECTOR, next_page_element)
                print("Burası Ne...............", next_page_element)
                next_page_element.click()
                

            except Exception as e:
                print("Nex Page Error", e)
        
        driver.quit()
        return html_content
