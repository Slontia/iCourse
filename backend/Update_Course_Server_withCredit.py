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

jj = str(1)
print(jj)
dict = {'工程基础类': 1, '数学与自然科学类': 2, '语言类':3, '博雅类':4,
        '核心通识类': 5, '体育类': 6, '一般通识类': 7, '核心专业类': 8, '一般专业类':9}

print(dict['工程基础类'])

#连接数据库
conn = pymysql.connect(host='10.2.28.124',port=3306,user = 'root',passwd='Hotcode@1506',db='icourse',charset="utf8") #db：库名

d = {} # dict that stores values of course_code

i = 0

pos = 0 # Global varible, this line can be deleted

def get_classification(s):
    if (s[0]=='B'):
        return (s[3:5])
    return (s[1:3])

def work(s):
    a = s.split(',') #['B3I050511', '一般专业类', '选修', '航空科学与工程学院', '3', '']

    #print(len(a))

    if (len(a)<7):
        return

    course_code = a[0]

    type = a[1]

    credit = a[4]

    e = a[1]

    d = a[2]

    name = a[5]
    course_name = name.replace('$', ',')

    teacher_t = a[6]
    teacher_all = teacher_t.split('◇')
    teacher = teacher_all[0]

    #print(teacher_t,'^^^^^',teacher)
    
    if (a[2]=="选修"):
        elective = "2"
    else:
        elective = "1"

    print(course_code,' ',type,'  ',credit,'  dict=',dict[e],' d= ',d,' elective=',elective)

    #return
    
    ###########################
    #insert into backend_course
    ###########################

    #update backend_course set elective = 1 where course_code='B3J103940';
    #update backend_course set credit=2.5 where course_code='B3J103940';
    #update backend_course set class_id = 1 where course_code='B3J103940';

    class_id = str(dict[e])
    
    sql1 = "update backend_course set elective = " + elective + " where course_code='"+course_code+"';"
    print(sql1)

    sql2 = "update backend_course set credit=" + str(credit) +" where course_code='"+course_code+"';"
    print(sql2)

    sql3 = "update backend_course set class_id = "+class_id+" where course_code='"+course_code+"';"
    print(sql3)


    
    try:
        #创建游标
        cur = conn.cursor()


        sql0 = "select * from backend_course where course_code = '"+course_code+"';"

        print(sql0)
        # 使用 execute()  方法执行 SQL 查询 
        cur.execute(sql0)
 
        #使用 fetchone() 方法获取单条数据.
        data = cur.fetchone()

        print("###",data)

        #return
    
        if (data==None): #
              college_id = get_classification(course_code)
              sql4 = "insert into backend_course (name,college_id,class_id,hours,course_code,"+"elective,teacher,credit) values('"+course_name+"',"+college_id+","+class_id+",NULL,'"+ course_code+"',"+elective+",'"+teacher+"',"+str(credit)+");";
              print("!!!",sql4)

              cur.execute(sql4)
              conn.commit()
            
        else:
            #同时向数据库表中插入多条数据
            cur.execute(sql1)
            #提交
            conn.commit()

            cur.execute(sql2)
            conn.commit()

            cur.execute(sql3)
            conn.commit()

            sql_t = "select teacher from backend_course where course_code = '"+course_code+"';"

            #print(sql0)
            # 使用 execute()  方法执行 SQL 查询 
            cur.execute(sql_t)
 
            #使用 fetchone() 方法获取单条数据.
            data = cur.fetchone()
            data_str = str(data)
            print("TEACHER::: ",data_str, " ::: ",teacher)
            t_pos = data_str.find("'",2)
            print(t_pos)
            if (t_pos!=-1):
                teacher_old = data_str[2:t_pos]
            else:
                teacher_old = ""
            print(teacher_old)
            if (teacher!=None and data_str.find(teacher)==-1):
                if (t_pos!=-1):
                    teacher = teacher_old+"|"+teacher
                
                print("TEACHER_new::: ",teacher)
                sql4 = sql3 = "update backend_course set teacher = '"+teacher+"' where course_code='"+course_code+"';"
                print(sql4)
            
                cur.execute(sql4)
                conn.commit()
            else:
                print("@@@Teahcer same")
        
        #关闭指针对象
        cur.close()
    except Exception as e:
        print(e)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("******NEXT********")
    return



pp = '123#446#5555#44'
#print("find",pp.find("55555"))
pp = pp.replace('#',',')
print(pp)

s = "B3I050511,一般专业类,选修,航空科学与工程学院,3,弹性力学（英文）(全英语),张彤|孙玉鑫|郭早阳|董雷霆◇[2-13周]星期二第5|6节|[2-13周]星期四第7|8节◇(一)317◇"

ans = s.split(',')
print(ans)
print(len(ans))
for i in range(0,len(ans)):
    print(i)
    print(ans[i],' !!! ')


# Iterate over the lines of the file
i = 0
with open('all_new.csv','rt',encoding='utf-8') as f:
    for line in f:
        
        i = i+1
        #if (i > 25):
            #break
        print(line)
        
        work(line)
        print("---")
        #break
