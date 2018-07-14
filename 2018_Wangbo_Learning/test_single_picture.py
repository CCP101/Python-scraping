import requests
from bs4 import BeautifulSoup
import re

url = "http://www.huitu.com/design/show/20171024/140320359021.html"
response = requests.get(url)
print(response)
response.encoding = "utf-8"
contents = response.text  # 获得响应数据的文本
soup = BeautifulSoup(contents, "html.parser")  # 用于页面解析
# print(soup)
imgList = soup.select("img")
print(imgList)
for i in imgList:
    # print(i)
    imgUrlList = re.findall("src=\"([^\"]*\")", str(i))
    print(imgUrlList)