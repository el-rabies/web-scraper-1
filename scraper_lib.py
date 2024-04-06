from selenium import webdriver
from bs4 import BeautifulSoup

def ffhome_page_scraper(soup:BeautifulSoup):
    #Get Table Body
    table_body = soup.find('tbody')
    #Get Collections of rows
    row_list = table_body.find_all('tr')
    #Manage Indevidual Rows
    title_list = []
    counter = 0
    for row in row_list:
        title = row.find('td')
        print(title, counter)
        title_list.append(title)
        counter += 1
    return title_list