'''
Created on 2017年11月6日

@author: ohazyi
'''
# -*- coding: utf-8 -*-
#from backend.models import Resource, User

import os
import sys
import time
import datetime

import pymysql

#连接数据库
conn = pymysql.connect(host='10.2.28.124',port=3306,user = 'root',passwd='Hotcode@1506',db='icourse',charset="utf8") #db：库名

i = 0

pos = 0 # Global varible, this line can be deleted

def get_classification(s):
    if (s[0]=='B'):
        return (s[3:5])
    return (s[1:3])

def itera(s, s_f):
    global pos
    j = s.find(s_f,pos)
    #print(j)
    str = s[pos:j]
    #print(str)
    pos = j+1
    return str
def check(str):
    j = str.rfind('.')
    if (j == -1):
        return 0
    if (str[j:len(str)].lower() == ".exe"):
        return 0
    print (str[j:len(str)])
    return 1
def work(s):
    global pos
    pos = 0
    semi = itera(s, ",")

    course_code = itera(s, ",")

    code_web = itera(s, ",")

    course_name = itera(s, ",")

    if (s[pos]=='"'):
        j = s.find('"', pos+1)
        teacher = s[pos+1:j]
        print('teacher: ', teacher, ' ',j,' ',len(s))
        pos = j+1
        if (s[pos]==','):
            pos=pos+1
    else:
        teacher = itera(s, ",")

    college_id = get_classification(course_code)

    ###########################
    #insert into backend_course
    ###########################
    
#    sql = "insert into backend_course (name,college_id,class_id,hours,credit,course_code) values('"+course_name+"',"+college_id+",NULL,NULL,NULL,'"+course_code+"');";
#    print(sql)
#    try:
#        #创建游标
#        cur = conn.cursor()
#        #同时向数据库lcj表中插入多条数据
#        cur.execute(sql)
#        #提交
#        conn.commit()
#        #关闭指针对象
#        cur.close()
#    except Exception as e:
#        print(e)
#        print("$$$$$$$$$$$$$$$$$$$$$$$$$")
#    print("#######")
#    return

    #############################
    #insert into backend_resource
    #############################
    while pos != 0:
        url =  itera(s,", \'")
        url = url[3: len(url)-1]
        url = url.replace("'","\\'")
        print(url)
        if (pos==0):
            break
        name = itera(s, "\')\"")
        name = name[2: len(name)]
        name = name.replace("'","\\'")
        pos=pos+3
        print(name)
        print("---")
        if (not check(name)):
            continue
        
        date = datetime.datetime.now()
        date = date.strftime("%Y-%m-%d %H:%M:%S")
        #sql = "insert into backend_resource (name,intro,course_code,upload_time,only_url,url) values('C++.pptx','2015-2016','A123456B',now(),1,'https://www.baidu.com');""
        sql = "insert into backend_resource"+"(name,intro,course_code,upload_time,only_url,url) values('"+name+"','"+semi+"','"+course_code+"','"+date+"',1,'"+url+"');"
        print(sql)
        try:
            #创建游标
            cur = conn.cursor()
            #同时向数据库lcj表中插入多条数据
            cur.execute(sql)
            #提交
            conn.commit()
            #关闭指针对象
            cur.close()
        except Exception as e:
            print(e)
            print("&&&&&&&&&&&&&&&&")
            
# Iterate over the lines of the file
with open('爬虫结果.csv','rt',encoding='utf-8') as f:
    for line in f:
        if (++i < 2):
            print(line)
            line=line.replace("\"\"","\'")
            if (line[0:16]=="academic_session"):
                continue
            work(line)
            print("**********")
