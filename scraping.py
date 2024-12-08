import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd
import time
from lxml import html


# URL of the website to scrape
url = "https://m.imdb.com/chart/top/"

# Send an HTTP GET request to the website
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(r.content, "html.parser")

movie_name = []
year = []
rating = []

movie_data = soup.find_all('li', class_= "ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent")

for i in movie_data:
    title = i.h3.text


movies = []
for row in movie_data:
    title = row.find('h3', class_='ipc-title__text').get_text()
    year = int(row.find('span', class_='sc-b0691f29-8 ilsLEX cli-title-metadata-item').get_text())
    movies.append([title,year])

print(movies)


df = pd.DataFrame(movies, columns=['Title','Year'])


# Add a delay between requests to avoid overwhelming the website with requests
time.sleep(1)


# Export the data to a CSV file
df.to_csv('top-rated-movies.csv', index=False)
