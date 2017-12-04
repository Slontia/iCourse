# 该文件为一系列和数据库的接口

from backend.models import *
from django.contrib.auth.models import User

# 前后端衔接用
from django.http import HttpResponse
import json
import datetime

# 获取某学院课程列表(modefied by xdt 2017.11.8)
# REQUIRES: type(col_id) == <class 'int'> && lower_value <= col_id <= upper_value
# MODIFIES: None
# EFFECTS: 返回学院编号为col_id的学院的课程信息列表，列表中的每个元素是字典

def college_course_list(col_id):
    result = Course.objects.filter(college_id=col_id)
    if(len(result) == 0):
        return []
    result = result.values()
    for course in result:
        course['credit'] = float(course['credit'])
    return list(result)

# 通过某课程类别获取课程列表(modefied by xdt 2017.11.8)
# REQUIRES: type(cla_id) == <class 'int'>
# MODIFIES: None
# EFFECTS: 返回某种课程类别的课程信息列表,列表中的每个元素是字典

def classification_course_list(cla_id):
    result = Course.objects.filter(class_id=cla_id)
    if(len(result) == 0):
        return []
    result = result.values()
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
    result['credit'] = float(result['credit'])
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
    if(not result['only_url']):
        result['url'] = '/download/' + str(result['id']) + '/'
    return result

# 查询个人信息
# REQUIRES: type(username) == <class 'string'>
# MODIFIES: None
# EFFECTS: 返回某个用户的一些信息,返回类型为dict,若用户不存在则返回空字典

def user_information_by_username(username):
    is_email = False
    result = User.objects.filter(username=username)
    if(len(result) == 0):
        result = User.objects.filter(email=username)
        if(len(result) == 0):
            return {}
        else:
            is_email = True
    if(is_email):
        profile = User.objects.get(email=username).userprofile
    else:
        profile = User.objects.get(username=username).userprofile
    result = result.values('username', 'email')[0]
    result['nickname'] = profile.nickname
    result['gender'] = profile.gender
    result['intro'] = profile.intro
    return result

def user_information_by_id(user_id):
    result = User.objects.filter(id=user_id)
    if(len(result) == 0):
        return {}
    result = result.values('username', 'email')[0]
    return result


# 根据课程id查询相应的资源信息
# REQUIRES: type(course_id) == <class 'int'>
# MODIFIES: None
# EFFECTS: 返回资源是属于course_id的所有资源的id,以list形式返回

def resource_courseid_list(course_id):
    ans = []
    c_c = Course.objects.filter(id=course_id)
    if (len(c_c) == 0):
        return ans
    c_c = c_c.values()[0]
    c_c=c_c['course_code']
    result = Resource.objects.filter(course_code=c_c)
    for i in result:
        ans_id_i = str(i)
        ans.append(int(ans_id_i))
    return ans

# 根据resource_id和number返回满足数量的课程资源的(resource_id, 上传用户名（若没有用户名则显示为匿名用户）, 下载次数，资源名称) 并且已经按上传时间排好了序
# 返回类型为list,list中元素的类型为tuple
def resource_information_list(course_id, number):
    course_id = list(Course.objects.filter(id=course_id).values_list('course_code', flat=True))
    if(len(course_id) == 0):
        return []
    course_id = course_id[0]
    count = 0
    result = []
    temp = list(Resource.objects.filter(course_code=course_id).values_list('id', 'upload_user_id','download_count','name', 'upload_time'))
    temp = sorted(temp, key=lambda x:x[4], reverse=True)
    #print(temp)^M
    for item in temp:
        if(item[1] == None):
            resource = {'resource_id':item[0], 'username':'匿名用户', 'download_count':item[2], 'name':item[3]}
        else:
            #resource = {'resource_id':item[0], 'username':User.objects.get(id=int(item[1])), 'download_count':item[2], 'name':item[3]}
            resource = {'resource_id':item[0], 'username':User.objects.get(id=int(item[1])).username, 'download_count':item[2], 'name':item[3]}
        result.append(resource)
        count += 1
        if(count == number):
            break
    return result

# 根据前端传来的username(可能为用户名或邮箱)，返回正确的用户名username
def get_username(username_or_email):
    result = User.objects.filter(username=username_or_email)
    if(len(result) == 0):
        result = User.objects.filter(email=username_or_email)
        if(len(result) == 0):
            return {}
    return result.values('username')[0]

def refresh_ip_visit_info(ip):
    ip_obj = IpVisitInfo.objects.filter(ip=ip)
    nowdate = str(datetime.datetime.now().strftime("%Y-%m-%d"))
    if (len(ip_obj) == 0):
        IpVisitInfo.objects.create(
            ip = str(ip), 
            visit_count = 1,
            early_date = nowdate,
            latest_date = nowdate
        )
        return
    ip_obj = ip_obj[0]
    if(ip_obj.latest_date != nowdate):
        ip_obj.latest_date = nowdate
        ip_obj.visit_count += 1
        ip_obj.save()

