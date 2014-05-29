# -*- coding: utf-8 -*-

import sqlite3
con = sqlite3.connect("addres.db") #ファイルが存在する場合がファイルを開く　ない場合は新しいデータベースが作成される


sql = u"""
   create table 電話帳 (
      ID  integer,
      名前 varchar(10),
      電話番号 integer
   );
   """

juge = 0
while juge < 1:
    print ("ID")
    ID = int(raw_input("---->"))
    print("名前")
    name = str(raw_input("---->"))
    print("電話番号")
    phone = int(raw_input("---->"))

    sql = u"insert into 電話帳 values('ID','name','phone')"
    con.execute(sql)
    juge = int(raw_input("続行....1 or終了....0"))
else:
    print("End")
    con.commit()
    con.close()
