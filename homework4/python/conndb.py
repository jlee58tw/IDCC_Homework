#!/usr/bin/python
     
import MySQLdb
     
db = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="bike")
cursor = db.cursor()
     
cursor.execute("SELECT * FROM test")
result = cursor.fetchall()
     
for record in result:
    print record[0]
