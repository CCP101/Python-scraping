import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, "html.parser")
# The main comparison table is currently the first table on the page

count = 0
table = bsObj.findAll("table", {"class": "wikitable"})
for i in table:
    rows = table[count].findAll("tr")
    csvFile = open(
        r"D:\Work Station\PycharmProjects\Python-scraping\Python网络数据采集\version1\chapter5\files\editors%d.csv" % count,
        'wt', newline='', encoding='utf-8')
    writer = csv.writer(csvFile)
    try:
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td', 'th']):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)
    finally:
        count = count+1
        csvFile.close()


