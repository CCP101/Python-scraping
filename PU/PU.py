import requests
from bs4 import BeautifulSoup
import re

count = 1
school_student = []
cookie_str = "XXXXXXXXXXXXXXXX"
for i in range(742):
    url = ("http://jcnuaa.pocketuni.net/index.php?app=event&mod=School&act=rank&k=3&&p=%d" % count)
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value
    headers = {'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/68.0.3440.106 Safari/537.36"}
    response = requests.get(url, headers=headers, cookies=cookies)
    # print(response)
    response.encoding = "utf-8"
    contents = response.text
    soup = BeautifulSoup(contents, "html.parser")
    # print(soup)
    List = soup.select("div")
    # print(List) # test if log in successfully
    chart = re.findall(""
                       "<tr>\s*"
                       "<td>([0-9]+)</td>\s*"
                       "<td>([\u4e00-\u9fa5]{2,})</td>\s*"
                       "<td>([0-9]{8,})</td>\s*"
                       "<td class=\"rank4\">([1-9]\d*.\d*|0.\d*[1-9]\d*)</td>"
                       , str(List))
    for a in range(10):
        school_student.append(chart[a])
    print("*" * count)
    count = count+1
print(school_student)
# wf = open(r"C:\Users\liwen\Desktop\nanhang.txt", "wb")
# wf.write(school_student)
