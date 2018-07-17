from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)

'''
/wiki/Brian_Dennehy
/wiki/Dead_Man%27s_Walk_(miniseries)
/wiki/Keith_Carradine
/wiki/Man_or_Muppet
/wiki/Alan_Jay_Lerner
/wiki/Tom_Kitt_(musician)
/wiki/Jeff_Whitty
/wiki/Harvey_Fierstein
/wiki/Brian_Stokes_Mitchell
/wiki/Jelly%27s_Last_Jam
/wiki/Drama_Desk_Award_for_Outstanding_Lyrics
/wiki/Stew_(musician)
/wiki/Hugh_Wheeler
/wiki/Memphis_(musical)
/wiki/Paul_Tazewell
/wiki/Ruined
/wiki/Henry_VIII_of_England
/wiki/Mary_Boleyn
/wiki/Norfolk
'''
