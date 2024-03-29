# coding=utf-8
from bs4 import BeautifulSoup
from requests import get
from parse_price import parse_price_for_apartment,parse_price_per_meter
from replace_non_ascii import remove_accents


city = remove_accents(input('Podaj nazwę miejscowości: ').lower().replace(" ", ""))
default_url = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/'
URL = default_url + city
print(URL)

page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')



for offer in bs.findAll('article', class_='css-1uevyzq es62z2j29'):
    offer_name = offer.find('h3', class_='css-1873em4 es62z2j24').get_text()
    offer_rooms = offer.find_all("span", class_='css-348r18 es62z2j20')[0].get_text()
    offer_area = offer.find_all("span", class_='css-348r18 es62z2j20')[1].get_text()
    offer_price_per_meter = offer.find_all('span', class_='css-348r18 es62z2j20')[-1].get_text()
    offer_price_for_apartment = offer.find('p', class_='css-lk61n3 es62z2j19').get_text()
    # print(parse_price_for_apartment(offer_price_for_apartment))
    # print(parse_price_per_meter(offer_price_per_meter))


