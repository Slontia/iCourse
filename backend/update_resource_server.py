'''
Created on 2017年11月26日

@author: ohazyi
'''
# -*- coding: utf-8 -*-
#from backend.models import Resource, User



import os
import sys
import time
import datetime

import pymysql

aa = "(""'hello lll world"")"
print(aa)
print(aa.replace("'","\'"))
a1 = aa.find("l")
a2 = aa.rfind("l")
print(a1,' ',a2)

str = "this is string example....wow!!! this is really stringis is sis";
print (str.replace("is", "was"));
print (str.replace("is", "was", 3));


#连接数据库
conn = pymysql.connect(host='10.2.28.124',port=3306,user = 'root',passwd='Hotcode@1506',db='icourse',charset="utf8") #db：库名
#创建游标
cur = conn.cursor()
#查询表中存在的数据
#cur.execute("select * from backend_resource;")
#fetchall:获取lcj表中所有的数据
#ret1 = cur.fetchall()
#print(ret1)
#print("----------------------")

#向数据库表中插入数据
#cur.execute("insert into backend_resource (name,intro,course_code,upload_time,only_url,url) values('C++.pptx','2015-2016','A123456B',now(),1,'https://www.baidu.com');")
#提交
#conn.commit()
#关闭指针对象
cur.close()
#关闭连接对象
#conn.close()

def get_classification(s):
    if (s[0]=='B'):
        return int(s[3:5])
    return int(s[1:3])

i = 0
#file = open("/Users/Mr.ZY/Desktop/爬虫结果.csv")
# Read the entire file as a single string

user = "{'name' : 'jim', 'sex' : 'male', 'age': 18}"
b = eval(user)
#print (b)


str1 = "this is string example....wow!!!";
str2 = "exam";
 
#print (str1.find(str2))
#print (str1.find(str2, 10))
#print (str1.find(str2, 40))
#print (str1.find('s'))
#print (str1.find('s',str1.find('s')+1))

pos = 0 # Global varible, this line can be deleted




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

    college_id = get_classfication(course_code)
    sql = "insert into backend_course (name,college_id,class_id,hours,credit,course_code) values('"+course_name+"',"+str(college_id)+",NULL,NULL,NULL,'"+course_code+"');";
    print(sql)
    print("#######")
    return
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
        #创建游标
        cur = conn.cursor()
        #同时向数据库lcj表中插入多条数据
        cur.execute(sql)
        #提交
        conn.commit()
        #关闭指针对象
        cur.close()
        
with open('爬虫结果.csv','rt',encoding='utf-8') as f:
    data = f.read()



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



'''
根据资源ID，返回资源链接
ID不存在则返回"no match"
无副作用
'''
def getLinkById(_id):
    try:
        ans = Resource.objects.get(id=_id)
    except:
        return "找不到链接"
    return ans.link

#相较于其他属性，id是最适合互异的，所以每个资源的id都要不一样
def addResource(_id, userId, courseId, resName="name", resPath="", resIntroduction=""):
    if (os.path.exists(resPath) == False):
        return "找不到文件！"
    fsize = round(os.path.getsize(resPath)/float(1024*1024), 2)  
    curTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    temp=Resource(id=_id, name=resName, link=resPath, introduce=resIntroduction, size=fsize, uploadTime=curTime, upload_user_id=userId, course_id=courseId)
    temp.save()
    return "添加成功！"

def checkUsernameAndPassword(_username, _password):
    try:
        ans = User.objects.get(username=_username)
    except:
        return "用户名不存在"
    if (ans.password == _password):
        return "登陆成功"
    else:
        return "账户名与密码不符"
