from selenium import webdriver
from bs4 import BeautifulSoup
from scraper_lib import ffhome_page_scraper

#Get response from page
URL = 'https://www.fanfiction.net/'
dr = webdriver.Firefox()
dr.get(URL)
dr.execute_script("return document.cookie")  
dr.execute_script("return navigator.userAgent")
#Get html
soup = BeautifulSoup(dr.page_source, 'html.parser')
ffhome_page_scraper(soup)
dr.quit
exit