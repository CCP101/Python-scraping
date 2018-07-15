from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
nameList = bsObj.findAll("span", {"class": "green"})  # find all<span class="green"></span>
for name in nameList:
    print(name.get_text())  # only use when you come to the final step
