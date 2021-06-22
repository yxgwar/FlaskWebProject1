import sqlite3

DATABASE = 'database/test.db'

#sql = "create table accounts (id integer primary key autoincrement,user_name string not null,password string not null);"
#sql = "create table video (id integer primary key autoincrement,name string ,path string not null ,user_name string not null,time string not null);"
#sql = 'create table Comment (comment_id integer primary key autoincrement,comment string not null,video_id integer ,user_name string not null,time string not null);'
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

def video_insert(name,path,user_name,time):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'insert into video (name,path,user_name,time) values(?,?,?,?)'
    cur.execute(sql,[name,path,user_name,time])
    con.commit()
    con.close()

def video_id_query(id):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'select name, path ,user_name, time from video where id = ?'
    cur.execute(sql,[id])
    result = cur.fetchone()
    con.close()
    return result

def video_user_query(username):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'select name, path, time, id from video where user_name = ?' #增加了视频id便于查询评论
    cur.execute(sql,[username])
    result = cur.fetchall()
    con.close()
    return result

def video_comments_query(video_id):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'select user_name, comment, time from Comment where video_id = ?'
    cur.execute(sql,[video_id])
    result = cur.fetchall()
    con.close()
    return result

def video_comments_insert(video_id,user_name,comment,time):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'insert into Comment (video_id,user_name,comment,time) values(?,?,?,?)'
    cur.execute(sql,[video_id,user_name,comment,time])
    con.commit()
    con.close()

def user_name_query(input_user_name):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = "select user_name from accounts where user_name like ?"
    cur.execute(sql,['%' + input_user_name+ '%'])
    result = cur.fetchall()
    con.close()
    return result

def friends_list_query(user_name):#依据用户名查询好友
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'select servant_name from friends where owner_name = ?'
    cur.execute(sql,[user_name])
    result = cur.fetchall()
    con.close()
    return result

def message_query(user_name):#依据用户名查询收到的所有消息
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'select send_user,message,time from emails where receive_user = ?'
    cur.execute(sql,[user_name])
    result = cur.fetchall()
    con.close()
    return result
