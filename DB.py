import sqlite3

DATABASE = 'database/test.db'

#sql = "create table accounts (id integer primary key autoincrement,user_name string not null,password string not null);"
#sql = "create table video (id integer primary key autoincrement,name string ,path string not null ,user_name string not null);"

def ac_insert(user_name,password):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'insert into accounts (user_name,password) values(?,?)'
    cur.execute(sql,[user_name,password])
    con.commit()
    con.close()

def ac_id(user_name):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'select id from accounts where user_name = ?'
    cur.execute(sql,[user_name])
    result = cur.fetchone()
    con.close()
    try:
        return result[0]
    except:
        return None

def ac_name(id):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'select user_name from accounts where id = ?'
    cur.execute(sql,[id])
    result = cur.fetchone()
    con.close()
    try:
        return result[0]
    except:
        return None

def ac_query(user_name):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'select password from accounts where user_name = ?'
    cur.execute(sql,[user_name])
    result = cur.fetchone()
    con.close()
    try:
        return result[0]
    except:
        return None

def video_insert(name,path,user_name):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'insert into video (name,path,user_name) values(?,?,?)'
    cur.execute(sql,[name,path,user_name])
    con.commit()
    con.close()

def video_name_query(name):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'select path from video where name = ?'
    cur.execute(sql,[name])
    result = cur.fetchone()
    con.close()
    try:
        return result[0]
    except:
        return None