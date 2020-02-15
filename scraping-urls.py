# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv

x = 1
url_output = []

def list_urls():
    while x < 4:
        page = "/pg" + str(x)
        url = "URL" + page
        headers = {'User-Agent':'Mozilla/5.0'}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")
        for aa in soup.find_all("a", class_="SPECIFY CLASS HERE"):
            link = aa.get("href")
            name = aa.get_text()
            output = "URL" + link, name
            #print(output)
            url_output.append(output)
        x = x + 1

    with open("urls.csv", 'w', encoding='Shift_jis') as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(url_output)


if __name__ == '__main__':
    list_urls()
