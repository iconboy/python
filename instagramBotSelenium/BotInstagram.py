
# author: Niki Moretti
# date: 2023-04-09
# version: 1.0
# description: Bot Instagram - Selenium
# email: developer.nick2018@gmail.com
# github: https://github.com/iconboy/
# linkedin: https://www.linkedin.com/in/niki-moretti-82446a181/
# telegram: https://t.me/developerfullstac
# Whatsapp: +55 46 9 9612-6914



import random
from selenium import webdriver
from selenium.webdriver.common.keys  import Keys
import time 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'/Users/nikimoretti/dev/Py Projects/Testes/geckodriver')

    def login(self):
        driver = self.driver
        driver.get('http://instagram.com')
        time.sleep(3)
        driver.find_element("xpath","//input[@name='username']").send_keys(self.username)
        time.sleep(2)
        driver.find_element("xpath","//input[@name='password']").send_keys(self.password)
        time.sleep( 3 + 4 * random.random() )
        driver.find_element("xpath","//button[contains(.,'Log in')]").click()
        time.sleep( 3 + 14 * random.random() )
   
    def search_hashtag(self, hashtag):
        driver = self.driver
        driver.get('http://instagram.com/explore/tags/' + hashtag)
        time.sleep( 3 + 10 * random.random() )
        # down the page
        for i in range(1, 3):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep( 3 + 10 * random.random() )
            time.sleep( 3 + 10 * random.random() )
            hrefs = driver.find_elements(By.TAG_NAME, 'a')

            hrefs = hrefs[10:]
            for href in hrefs:
                hreflink = href.get_attribute('href')
                print(hreflink)

InstagramBot = InstagramBot('yourUsername', 'yourPassword')
InstagramBot.login()
InstagramBot.search_hashtag('searchHashtag')
