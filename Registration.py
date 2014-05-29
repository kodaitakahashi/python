# -*-coding: utf-8 -*-
import sqlite3
connection = sqlite3.connect('addres.db')
cursor = connection.cursor()
cursor.execute('''
              CREATE TABLE addres (id INTEGER PRIMARY KEY AUTOINCREMENT
              ,name TEXT(100) NOT NULL
              ,phone NOT NULL);
''')
cursor.close()
