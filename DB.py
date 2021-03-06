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
    sql = 'select name, path, time, id from video where user_name = ?' #???????????????id??????????????????
    cur.execute(sql,[username])
    result = cur.fetchall()
    con.close()
    return result

def video_comments_query(video_id):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'select user_name, comment, time, comment_id from Comment where video_id = ?'
    cur.execute(sql,[video_id])
    result = cur.fetchall()
    con.close()
    return result

def comment_video_query(comment_id):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'select video_id from Comment where comment_id = ?'
    cur.execute(sql,[comment_id])
    result = cur.fetchall()
    con.close()
    return result[0]

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

def friends_list_query(user_name):#???????????????????????????
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'select servant_name from friends where owner_name = ?'
    cur.execute(sql,[user_name])
    result = cur.fetchall()
    con.close()
    return result

def message_query(user_name):#??????????????????????????????????????????
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'select send_user,message,time from emails where receive_user = ?'
    cur.execute(sql,[user_name])
    result = cur.fetchall()
    con.close()
    return result

def friendship_query(owner_name,servant):#????????????????????????????????????owner_name??????????????????servant???????????????
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'select * from friends where owner_name = ? and servant_name = ?'
    cur.execute(sql,[owner_name,servant])
    result = cur.fetchone()
    con.close()
    if result is None:
        return None
    else:
        return True

def friendship_insert(owner_name,servant):#????????????
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'insert into friends (owner_name,servant_name) values(?,?)'
    cur.execute(sql,[owner_name,servant])
    con.commit()
    con.close()

def friendship_delete(owner_name,servant):#????????????
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'delete from friends where owner_name = ? and servant_name = ?'
    cur.execute(sql,[owner_name,servant])
    con.commit()
    con.close()

def send_eamil(send_user,receive_user,message,time):#????????????
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'insert into emails (send_user,receive_user,message,time) values(?,?,?,?)'
    cur.execute(sql,[send_user,receive_user,message,time])
    con.commit()
    con.close()

def admin_id_query(id):#????????????????????????
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'select * from admin where user_id = ?'
    cur.execute(sql,[id])
    result = cur.fetchone()
    con.close()
    if result is None:
        return None
    else:
        return True

def admin_name_query(name):#????????????????????????
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'select * from admin where user_name = ?'
    cur.execute(sql,[name])
    result = cur.fetchone()
    con.close()
    if result is None:
        return None
    else:
        return True

def video_delete(id):#????????????
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'delete from video where id = ?'
    cur.execute(sql,[id])
    con.commit()
    con.close()

def comment_delete(id):#????????????
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'delete from Comment where comment_id = ?'
    cur.execute(sql,[id])
    con.commit()
    con.close()

def video_query():
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = 'select name, path, time, id from video'
    cur.execute(sql)
    result = cur.fetchall()
    con.close()
    return result

def video_name_query(input_video_name):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    sql = "select name, path, time, id from video where name like ?"
    cur.execute(sql,['%' + input_video_name+ '%'])
    result = cur.fetchall()
    con.close()
    return result