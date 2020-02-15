# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv

x = 1
url_output = []

def list_urls():
    while x < 4: # Change this number accordingly
        page = "<>" + str(x) # Add a directory name that represents next pages
        url = "URL" + page # Paste the URL you want to scrape
        headers = {'User-Agent':'Mozilla/5.0'}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")
        for atag in soup.find_all("a", class_="SPECIFY CLASS HERE"): # Paste the class names here
            link = atag.get("href")
            if "<SPECIFIC STRING>" in link:
                link.replace("<SPECIFIC STRING>", "")
            name = atag.get_text()
            output = "URL" + link, name # Paste the URL you want to scrape since link only shows directory names
            #print(output)
            url_output.append(output)
        x = x + 1

    with open("urls.csv", 'w', encoding='Shift_jis') as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(url_output)


if __name__ == '__main__':
    list_urls()
