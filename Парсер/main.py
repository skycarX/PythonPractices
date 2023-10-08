import requests
from bs4 import BeautifulSoup as bs

url = "https://quotes.toscrape.com/"
reqs = requests.get(url)
soup = bs(reqs.text, 'lxml')
quotes = soup.find_all('span', class_='text')

authors = soup.find_all('small', class_='author')

tags = soup.find_all('div', class_='tags')

for i in range(0, len(quotes)):
    print(quotes[i].text)
    print('--by ' + authors[i].text + ' --')
    tagsforquote = tags[i].find_all('a', class_='tag')
    for tagsforquote in tagsforquote:
        print('-' + tagsforquote.text)
    print('\n')