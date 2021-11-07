from bs4 import BeautifulSoup
from requests import get

URL = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/wroclaw'

page = get(URL)
bs = BeautifulSoup(page.content)