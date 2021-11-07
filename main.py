# coding=utf-8
from bs4 import BeautifulSoup
from requests import get
from replace_non_ascii import remove_accents

city = remove_accents(input('Podaj nazwę miejscowości: ').lower().replace(" ", ""))
default_url = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/'
URL = default_url + city
print(URL)

page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')

for offer in bs.findAll('article', class_='css-1uevyzq es62z2j29'):
    offer_name = offer.find('h3', class_='css-1873em4 es62z2j24').get_text()
    print(offer_name)
