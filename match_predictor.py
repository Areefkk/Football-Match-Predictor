import pandas as pd
from bs4 import BeautifulSoup
import requests

## Creates a soup to extract the HTML code for the website
url = 'https://en.wikipedia.org/wiki/2022_FIFA_World_Cup'
res = requests.get(url)
content = res.text
soup = BeautifulSoup(content, 'lxml')

match_data = soup.find_all('div', class_='footballbox')

