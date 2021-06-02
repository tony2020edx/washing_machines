import pymysql

import time

date = time.strftime('%Y-%m-%d 0:0:0')


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='passme123@#$',
                             db='hpsize')


my_cursor = connection.cursor()


sql = "INSERT INTO hptable (product, saleprice, date) VALUES (%s, %s, %s)"
val = ("Acer", "11",date)



my_cursor.execute(sql,val)

my_cursor.execute("SELECT * from hptable")

connection.commit()


result = my_cursor.fetchall()

for i in result:
    print(i)

connection.close()









