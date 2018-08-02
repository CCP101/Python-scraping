import csv

# from os import open

csvFile = open(r"D:\Work Station\PycharmProjects\Python-scraping\Python网络数据采集\version1\chapter5\files\test.csv",
               'w+', newline='')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow((i, i + 2, i * 2))
finally:
    csvFile.close()
