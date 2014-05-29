#-*-coding:utf-8-*-
import sqlite3
connect = sqlite3.connect('addres.db')
cursor = connect.cursor()
cursor.execute("""SELECT * FROM addres""")
for row in cursor.fetchall():
    print row[0],row[1],row[2]

cursor.close()
