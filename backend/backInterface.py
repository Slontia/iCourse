'''
Created on 2017年10月28日

@author: 15061188
'''
# -*- coding: utf-8 -*-
from backend.models import Resource
import os
import time
'''
根据资源ID，返回资源链接
ID不存在则返回"no match"
无副作用
'''
def getLinkById(rid):
    try:
        ans = Resource.objects.get(resourceId=rid)
    except:
        print("no match")
        return "no match"
    print(ans.link)
    return ans.link

def addResource(resId, resName="name", resPath="", resIntroduction=""):
    if (os.path.exists(resPath) == False):
        return "找不到文件！"
    fsize = str(round(os.path.getsize(resPath)/float(1024*1024), 2))+'MB'   
    curTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    temp=Resource(resourceId=resId, name=resName, link=resPath, introduce=resIntroduction, size=fsize, uploadTime=curTime)
    temp.save()
    return "添加成功！"
