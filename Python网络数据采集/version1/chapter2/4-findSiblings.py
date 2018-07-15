from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:  # 收集表格数据
    print(sibling)  # 格式规范使爬虫更稳定
