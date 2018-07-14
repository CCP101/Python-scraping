import requests
from bs4 import BeautifulSoup
import re  # 正则表达式类库

url = "http://10.0.4.98:8080/web/index.jsp"
response = requests.get(url)
# print(response)#<Response [200]>
response.encoding = "UTF-8"
# print(response.text)
contents = response.text  # 返回当前页面的所有内容
soup = BeautifulSoup(contents, "html.parser")
# print(soup)
# print(soup.select("a img"))
imgList = soup.select("a img")
count = 1
for i in imgList:
    # print(type(i))
    imgUrlList = re.findall("data-original=\"([^\"]*)!", str(i))
    # print(imgUrlList)
    if len(imgUrlList) != 0:
        # print(imgUrlList[0])
        urlValue = imgUrlList[0]
        responseGet = requests.get(urlValue)
        # print(responseGet.content)
        print("*" * count)
        wf = open(r"C:\Users\Administrator\Desktop\image\copy_%d.jpg" % count, "wb")
        wf.write(responseGet.content)
        count = count + 1

print("ok")
