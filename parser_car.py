# -*- coding: utf8 -*-
import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re

from config_parser import data_list


def get_html(url):
    response = requests.get(url)
    response.encoding = 'cp1251'
    return response.text


def start():
    res = ''
    f = open('res.txt', 'a')
    for data in data_list:
        html = get_html(data[0])
        soup = BeautifulSoup(html, 'lxml')
        res = ''
        pages = soup.find_all('div', class_='car-info__car-name')
        for models in pages:
            model = str(models)
            start = model.find('href="')
            end = model.find('</a>')
            model = model[start+2: end]
            start = model.find('">')
            g = model[start+2:]
            g = g.replace(' РєР°Р±СЂРёРѕ', '').replace(' РєСѓРїРµ', '').replace(' СѓРЅРёРІРµСЂСЃР°Р»', '').replace(' СЃРµРґР°РЅ', '').replace(' РІРµР·РґРµС…РѕРґ Р·Р°РєСЂС‹С‚С‹Р№', '').replace(' С…СЌС‚С‡Р±РµРє', '').replace(' С…СЌС‚С‡Р±РµРє', '')
            res += "('" + data[1] + ", " + g + "'), "
            f.write(res)
    print(res)
    f.close()

start()

# def get_total_pages(html):
#     soup = BeautifulSoup(html, 'lxml')
#     divs = soup.find('div', class_='pagination-pages clearfix')
#     pages = divs.find_all('a', class_='pagination-page')[-1].get('href')
#     total_pages = pages.split('=')[1].split('&')[0]
#     return int(total_pages)