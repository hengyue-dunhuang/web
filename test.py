# coding=UTF-8
# 续行符的三种方法： \  ()  """xxxxx"""
# attention sqlite3  not sqlite!
# 使用sqlite显示数据库内容时，先用attach联系数据库文件至表单，再用SELECT * 打印内容,且
# 开启.header on 和 .mode column
# import sqlite3
# conn = sqlite3.connect('todo.db') # Warning: This file is created in the currentdirectory
# conn.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL,status bool NOT NULL)")
# conn.execute("INSERT INTO todo (task,status) VALUES ('Read A-byte-of-python to get agood introduction into Python',0)")
# conn.execute("INSERT INTO todo (task,status) VALUES ('Visit the Python website',1)")
# conn.execute("INSERT INTO todo (task,status) VALUES ('Test various editors for andcheck the syntax highlighting',1)")
# conn.execute("INSERT INTO todo (task,status) VALUES ('Choose your favorite WSGI-Framework',0)")
# conn.commit()

import sqlite3
from bottle import route, run, template, debug,request,static_file,error,default_app
from paste import httpserver

@route("/todo")
def todo_list():
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    output = template('make_table',rows=result)
    return output
    

@route('/new', method='GET')
def new_item():
    if request.GET.save:
        new = request.GET.task.strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new, 1))
        new_id = c.lastrowid
        conn.commit()
        c.close()
        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
    else: return template('new_task.tpl')

@route('/help')
def help():
    return static_file('help', root='/home/zhy/web')

@route('/edit/<no:int>', method='GET')
def edit_item(no):
    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()
        if status == 'open':
            status = 1
        else:
            status = 0
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit,status, no))
        conn.commit()
        return '<p>The item number %s was successfully updated</p>' % no

    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no),))
        cur_data = c.fetchone()
        return template('edit_task', old=cur_data, no=no)

@route('/json<json:re:[0-9]+>')
def show_json(json):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (json,))
    result = c.fetchall()
    c.close()
    if not result:
        return {'task': 'This item number does not exist!'}
    else:
        return {'task': result[0]}

@error(403)
def mistake403(code):
    return 'The parameter you passed has the wrong format!'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'
#debug(True)
#run(port=1024, host='0.0.0.0',reloader=True)
run(port=8012, host='192.168.1.102',server = "tornado",reloader=True)
#run(port=8012, host='192.168.43.139',server = "tornado",reloader=True)