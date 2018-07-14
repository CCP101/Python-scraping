import requests
from bs4 import BeautifulSoup

url = "https://www.bilibili.com/"
respones = requests.get(url)  # 返回响应代码 Response [200]
print(respones)
respones.encoding = "utf-8"  # 字符编码转换
# respones.encoding = "GBK"
contents = respones.text  # 获得响应数据的文本
print(contents)
print(type(contents))
print("-" * 20)
soup = BeautifulSoup(contents, "html.parser")  # 页面解析
print(soup)
list = soup.contents
print("-" * 20)
print(type(list))
for text in list:
    print(text)
