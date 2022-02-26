#续行符的三种方法： \  ()  """xxxxx"""
#attention sqlite3  not sqlite!
#使用sqlite显示数据库内容时，先用attach联系数据库文件至表单，再用SELECT * 打印内容,且
#开启.header on 和 .mode column

import sqlite3
conn = sqlite3.connect('todo.db') # Warning: This file is created in the currentdirectory
conn.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL,status bool NOT NULL)")
conn.execute("INSERT INTO todo (task,status) VALUES ('Read A-byte-of-python to get agood introduction into Python',0)")
conn.execute("INSERT INTO todo (task,status) VALUES ('Visit the Python website',1)")
conn.execute("INSERT INTO todo (task,status) VALUES ('Test various editors for andcheck the syntax highlighting',1)")
conn.execute("INSERT INTO todo (task,status) VALUES ('Choose your favorite WSGI-Framework',0)")
conn.commit()

