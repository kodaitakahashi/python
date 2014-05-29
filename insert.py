#-*- coding:utf-8 -*-
import sqlite3
connection = sqlite3.connect('addres.db')
cursor = connection.cursor()
sql = "INSERT INTO addres(name,phone) VALUES(?,?);"
print("NAME")
name=raw_input("------->")
print("PHONE")
phone=raw_input("------->")
fact =[name,phone]
cursor.execute(sql,fact)
connection.commit()

cursor.close()
