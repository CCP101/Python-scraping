import requests
from bs4 import BeautifulSoup
import re
count = 1
school_student = []
cookie_str = r"PHPSESSID=36fa74305b7fdeb81395a; Hm_lvt_dd3" \
             r"ea352543392a029ccf9da1be54a50=1535029961,15351067" \
             r"43; TS_think_language=zh-CN; TS_LOGGED_USER=ZUdBLN" \
             r"H%3D8LWr37Zuotakxs5tv; Hm_lpvt_dd3ea352543392a02" \
             r"9ccf9da1be54a50=1535120447"
url = ("http://jcnuaa.pocketuni.net/index.php?app=event&mod=School&act=rank&k=3&&p=%d" % count)
response = requests.get(url)
for i in range(700):
    url = ("http://jcnuaa.pocketuni.net/index.php?app=event&mod=School&act=rank&k=3&&p=%d" % count)
    response = requests.get(url)
    # print(response)
    response.encoding = "utf-8"
    contents = response.text
    soup = BeautifulSoup(contents, "html.parser")
    # print(soup)
    List = soup.select("div")
    # print(List)
    chart = re.findall(""
                       "<tr>\s*"
                       "<td>([0-9]+)</td>\s*"
                       "<td>([\u4e00-\u9fa5]{2,})</td>\s*"
                       "<td></td>\s*"
                       "<td class=\"rank4\">([1-9]\d*.\d*|0.\d*[1-9]\d*)</td>"
                       , str(List))
    for a in range(10):
        school_student.append(chart[a])
    print("*" * count)
    count = count+1
print(school_student)
# wf = open(r"C:\Users\liwen\Desktop\nanhang.txt", "wb")
# wf.write(school_student)






