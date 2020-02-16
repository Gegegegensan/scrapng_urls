# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv

x = 1
url_output = []
info_output = []

def list_urls():
    while x < 4: # Change this number accordingly depending on how many pages you want to scrape
        page = "<>" + str(x) # Add a directory name that represents next pages
        url = "URL" + page # Paste the URL you want to scrape
        headers = {'User-Agent':'Mozilla/5.0'}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")
        for atag in soup.find_all("a", class_="SPECIFY CLASS HERE"): # Paste the class names here
            link = atag.get("href")
            #if "<SPECIFIC STRING>" in link:
            #    link.replace("<SPECIFIC STRING>", "")
            name = atag.get_text()
            output = "URL" + link, name # Paste the URL you want to scrape since link only shows directory names
            #print(output)
            url_output.append(output)
        x = x + 1

    with open("urls.csv", 'w', encoding='Shift_jis') as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(url_output)

def list_info():
    with open('urls.csv') as f:
    lines = f.readlines()
    
    for line in lines:
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(line, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        for date in soup.find_all('<SPECIFY>', class_='<SPECIFY>'): # Replace <SPECIFY> with necessary HTML tag and class name
            date_info = date.get_text()
            company = soup.title
            url = line
            info = soup.find_all('<SPECIFY>',type='<SPECIFY>') # Replace <SPECIFY> with necessary HTML tag and class name
            output = company, date_info, line, info
            info_output.append(output)

    with open("urls-detailed-info.csv", 'w', encoding='Shift_jis') as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(info_output)
        
        
if __name__ == '__main__':
    list_urls()
    list_info()
