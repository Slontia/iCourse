'''
Created on 2017年10月28日

@author: 15061188
'''
# -*- coding: utf-8 -*-
from backend.models import Resource, User
import os
import time
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
