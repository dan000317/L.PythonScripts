import urllib.request, urllib.parse, urllib.error
from bs4 import  BeautifulSoup

handle = urllib.request.urlopen('https://en.wikipedia.org/wiki/2022_Russian_invasion_of_Ukraine')
for line in handle:
    print(line.decode())