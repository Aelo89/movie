import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# scraping

url = 'https://www.imdb.com/chart/top/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


# extract
movies = []
for row in soup.select('tbody.lister-list tr'):
    title = row.find('td', class_='titleColumn').find('a').get_text()
    rating = row.find('td', class_='ratingColumn imdbRating').find('strong').get_text()
    movies.append([title, rating])

df = pd.DataFrame(movies, columns=['Title','Rating'])

time.sleep(1)

# data to csv
df.to_csv('top-rated-movies.csv', index=False)

