from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
bsObj = BeautifulSoup(html, "html.parser")
print(bsObj.title)
print(bsObj.body.h1)
print(bsObj.h1)

