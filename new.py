from urllib.request import Request, urlopen 
from bs4 import BeautifulSoup as soup
import pandas as pdp

url = "https://www.imdb.com/chart/top/"

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
page_html = urlopen(req).read()

print(page_html)