import requests
from bs4 import BeautifulSoup

url = "http://10.0.4.98:8080/web/index.jsp"
response = requests.get(url)  # 返回响应状态码
response.encoding = "UTF-8"  # 字符编码转换
contents = response.text  # 获得响应数据的文本
soup = BeautifulSoup(contents, "html.parser")  # 用于页面解析
list = soup.select("ul")  # 根据标签名称查找标签
print(type(list))
# print(list[0])
# print(type(list[0]))
print(len(list))  # 长度
for i in list:
    print(i)
    print("-------------------")

print(list[0].text)  # 文本内容
print(list[1].select("li"))  # 当前第二个位置的ul标签下的li标签
print("--------------------")
list2 = soup.select(".c")
print(len(list2))
print(list2[0].text)
