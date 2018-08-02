import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='python_data')
cur = conn.cursor()

# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
# LAST_NAME, AGE, SEX, INCOME) \
#        VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
#        ('Mac', 'Mohan', 20, 'M', 2000)



cur.execute("USE scraping")
cur.execute("SELECT * FROM pages WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close()
