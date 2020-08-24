from selenium import webdriver
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd
import os,re,sys
import time,datetime

def parseYouTube(url):
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
        #url = sys.argv[1]
       # url = r'https://www.youtube.com/watch?v=NMre6IAAAiU'
        url = url.replace(r'watch?',r'live_chat?')
        browser.get(url)
        browser.implicitly_wait(1)
        chats = list()
        chats_prev = list()
        timeout = time.time() + 5
        while True: #timeout > time.time():
                innerHTML = browser.execute_script("return document.body")
                chats = list(browser.find_elements_by_css_selector('yt-live-chat-text-message-renderer'))
                chats_read = [chat for chat in chats if chat not in chats_prev]
                if bool(chats_read):
                        for chat in chats_read:
                                timestap = chat.find_element_by_css_selector('#timestamp').get_attribute('innerText')
                                author_name = chat.find_element_by_css_selector("#author-name").get_attribute('innerText')
                                message = chat.find_element_by_css_selector("#message").get_attribute('innerText')
                                print("[" + author_name + "|"+ time.strftime(' %H:%M:%S ') + "|"+ timestap + "]:" + message + "\n")
                chats_prev = chats
        browser.quit()
        return chats

      