import requests
from bs4 import BeautifulSoup
import re

url = "http://soso.nipic.com/?q=IT"
response = requests.get(url)
print(response)
response.encoding = "utf-8"
contents = response.text  # 获得响应数据的文本
soup = BeautifulSoup(contents, "html.parser")  # 用于页面解析
print(soup)
imgList = soup.select("img")
print(imgList)
count = 1
for i in imgList:
    print(i)
    imgUrlList = re.findall("data-original=\"([^\"]*\")", str(i))
    print(imgUrlList)
    urlValue = imgUrlList[0]
    responseGet = requests.get(urlValue)
    print("*" * count)
    wf = open(r"C:\Users\liwen\Desktop\image\copy_%d.jpg" % count, "wb")
    wf.write(responseGet.content)
    count = count + 1
print("copy file success! Finish the project")
