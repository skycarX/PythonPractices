import requests
from bs4 import BeautifulSoup as bs

url = "https://citaty.info/random"
reqs = requests.get(url)
soup = bs(reqs.text, 'lxml')
quotes = soup.find_all('div', class_='field-item even last')
authors = soup.find_all('div', class_='field-item even')

for i in range(0, len(quotes)):
    print(quotes[i].text)
    print('('+authors[i].text+')')