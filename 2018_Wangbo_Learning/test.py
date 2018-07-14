import requests
from bs4 import BeautifulSoup
import re
# 导入所需的库
url = "http://10.0.4.98:8080/web/index.jsp"
#  输入目标页面
response = requests.get(url)  # 返回响应代码 Response [200]
print(response)
#  确定网页正常及允许爬虫
response.encoding = "utf-8"
#  中文网页强制转换编码
contents = response.text  # 获得响应数据的文本
soup = BeautifulSoup(contents, "html.parser")  # 用于页面解析
#  BeautifulSoup进行数据分析与解析
print(soup)
#  查看整理好后的web数据 查看目标标签
imgList = soup.select("img")
print(imgList)
#  选择关键词初步选择所有满足项目
count = 1
#  循环计数
for i in imgList:
    # print(i)
    imgUrlList = re.findall("src=\"([^\"]*)\"", str(i))
    print(imgUrlList)
    # 正则表达式解析
    urlValue = imgUrlList[0]
    responseGet = requests.get(urlValue)
    # 讲目标加入到列表中（多个文件）
    print("*" * count)
    wf = open(r"C:\Users\Administrator\Desktop\image\copy_%d.jpg" % count, "wb")
    wf.write(responseGet.content)
    # 文件输出
    count = count + 1
