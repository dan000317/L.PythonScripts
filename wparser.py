import requests
from bs4 import BeautifulSoup

req = requests.get('https://en.wikipedia.org/wiki/2022_Russian_invasion_of_Ukraine')
soup = BeautifulSoup(req.content, 'html.parser')

print(soup.prettify())