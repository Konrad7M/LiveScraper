from selenium import webdriver
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd
import os,re,sys
import time,datetime
from selenium.webdriver.common.by import By
import itertools

def parseTwitch(url):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--executable_path="chromedriver.exe"') 
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-extensions')
        chrome_bin = os.getenv('GOOGLE_CHROME_SHIM', None)
        is_local = os.getenv('IS_LOCAL', None)
        chromedriver_path = r'chromedriver.exe'
        service_log_path = "{}/chromedriver.log".format('\.')
        service_args = ['"--verbose", "--log-path=scrape.log"']
        chromedriver_path = 'chromedriver.exe'
        chrome_options.binary_location = r'C:\Program Files (x86)\Chromium\Application\chrome.exe'
        browser = webdriver.Chrome(executable_path=chromedriver_path,chrome_options=chrome_options,service_args=service_args)
        browser.get(url)
        browser.implicitly_wait(1)
        chats = list()
        chats_prev = list()
        while True: 
                innerHTML = browser.execute_script("return document.body")
                chats = list(browser.find_elements_by_xpath("//li[@class='tw-full-width']"))
                chats_read = [chat for chat in chats if chat not in chats_prev]
                if bool(chats_read):
                        for chatingo in chats_read:
                                try:
                                        user    =       chatingo.find_element_by_xpath(".//span[@data-a-target='chat-message-username']").get_attribute("innerText")
                                except:
                                        user    =       "problem"
                                try:
                                        message =       chatingo.find_element_by_xpath(".//span[@class='text-fragment']").get_attribute("innerText")
                                except:
                                        message =       "problem"
                                try:
                                        time    =       chatingo.find_element_by_xpath(".//div[@class='tw-pd-x-05']/p[@class='tw-font-size-7']").get_attribute("innerText")
                                except:
                                        time    =       "problem" 
                                print("[ " + user + " | " + time + " ]: " + message)
                chats_prev = chats
        browser.quit()
        return chats