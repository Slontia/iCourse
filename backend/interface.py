# 该文件为一系列和数据库的接口

from backend.models import *
from django.contrib.auth.models import User

# 前后端衔接用
from django.http import HttpResponse
import json

# 获取某学院课程列表
# REQUIRES: type(col_id) == <class 'int'> && lower_value <= col_id <= upper_value
# MODIFIES: None
# EFFECTS: 返回学院编号为col_id的学院的课程列表,返回类型为list

def college_course_list(col_id):
    result = Course.objects.filter(college_id=col_id).values_list("id", flat=True)
    return list(result)

# 通过某课程类别获取课程列表
# REQUIRES: type(cla_id) == <class 'int'>
# MODIFIES: None
# EFFECTS: 返回某种课程类别的课程列表,返回类型为list

def classification_course_list(cla_id):
    result = Course.objects.filter(class_id=cla_id).values_list("id", flat=True)
    return list(result)

# 查询课程详细信息
# REQUIRES: type(cou_id) == <class 'int'>
# MODIFIES: None
# EFFECTS: 返回某个课程的所有信息,返回类型为dict,若课程不存在则返回空字典

def course_information(cou_id):
    result = Course.objects.filter(id=cou_id)
    if(len(result) == 0):
        return {}
    result = result.values()[0] 
    return result

def course_visit_count(cou_id):
    result = Course.objects.filter(id=cou_id)
    if(len(result) == 0):
        return -1
    result = result.values()[0].visit_count
    return result

# 查询课程贡献度列表
# REQUIRES: type(cou_id) == <class 'int'>
# MODIFIES: None
# EFFECTS: 返回某个课程的贡献度列表,表中元素为排好序的(user_id, score)元组,返回类型为list

def course_contribution_list(cou_id):
    temp = R_Course_User_Contribution.objects.filter(course_id=cou_id)
    if(len(temp) == 0):
        return []
    temp = temp.values_list("user_id", "score")
    keys = []
    for item in temp:
        if(item[0] not in keys):
            keys.append(item[0])
    values = []
    for key in keys:
        contrib = 0
        for item in temp:
            if(item[0] == key):
                contrib += item[1]
        values.append(contrib)
    
    result = list(zip(keys,values))
    result = sorted(result, key=lambda x:x[1], reverse=True)
    return result

# 查询资源信息
# REQUIRES: type(resource_id) == <class 'int'>
# MODIFIES: None
# EFFECTS: 返回某个资源的所有信息,返回类型为dict,若资源不存在则返回空字典

def resource_information(resource_id):
    result = Resource.objects.filter(id=resource_id)
    if(len(result) == 0):
        return {}
    result = result.values()[0]
    return result

# 查询个人信息
# REQUIRES: type(username) == <class 'string'>
# MODIFIES: None
# EFFECTS: 返回某个用户的一些信息,返回类型为dict,若用户不存在则返回空字典

def user_information(username):
    result = User.objects.filter(username=username)
    if(len(result) == 0):
        return {}
    profile = User.objects.get(username=username).userprofile
    result = result.values('username', 'email')[0]
    result['nickname'] = profile.nickname
    result['gender'] = profile.gender
    result['intro'] = profile.intro
    return result

# 根据课程id查询相应的资源信息
# REQUIRES: type(course_id) == <class 'int'>
# MODIFIES: None
# EFFECTS: 返回资源是属于course_id的所有资源的id,以list形式返回

def resource_courseid_list(course_id):
    print("****",course_id)
    c_c = Course.objects.filter(id=course_id)
    print("####", c_c)
    c_c = c_c.values()[0]
#    print(c_c)
#    print(c_c['course_code'])
    c_c=c_c['course_code']
    result = Resource.objects.filter(course_code=c_c)
#    print(result)
    ans = []
    for i in result:
#        print(i)
#        print(str(i))
        ans_id_i = str(i)
#        print(int(ans_id_i),'!!!',int(ans_id_i)+1)
        ans.append(int(ans_id_i))
    return ans

# 根据resource_id和number返回满足数量的课程资源的(resource_id, 上传用户名（若没有用户名则显示为匿名用户）, 下载次数，资源名称) 并且已经按上传时间排好了序
# 返回类型为list,list中元素的类型为tuple
def resource_information_list(course_id, number):
    course_id = list(Course.objects.filter(id=course_id).values_list('course_code', flat=True))[0]
    count = 0
    result = []
    temp = list(Resource.objects.filter(course_code=course_id).values_list('id', 'upload_user_id','download_count','name', 'upload_time'))
    temp = sorted(temp, key=lambda x:x[4], reverse=True)
    #print(temp)^M
    for item in temp:
        if(item[1] == None):
            resource = (item[0], '匿名用户', item[2], item[3])
        else:
            resource = (item[0], User.objects.get(id=int(item[1])), item[2], item[3])
        result.append(resource)
        count += 1
        if(count == number):
            break
    return result

