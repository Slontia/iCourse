# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from backend import interface
import json
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.shortcuts import render

import requests
import urllib.request
import json
import datetime

import os

def page404(request):
    return
# return HttpResponse(u"page not found: 404")

def home(request):
    return render(request, 'index.html')

def course(request):
    return render(request, 'course.html')

def contact(request):
    return render(request, 'contact.html')

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

# Register Interface
# REQUIRES: the ajax datatype must be json and the data should be like {'name': value,...}
# MODIFIES: create a new user in database, update tables(mainly auth_user and backend_userprofile)
# EFFECTS: if register success, return a json data {'error': 0};
#          else return a json data {'error': error}, error is a list of error
# URL: /sign/register/
@csrf_exempt
def userRegister(request):
    try:
        if(request.method == 'POST'):
            data = json.dumps(request.POST)
            data = json.loads(data)
            username = str(data.get('username'))
            password1 = str(data.get('password1'))
            password2 = str(data.get('password2'))
            email = str(data.get('email'))
            gender = str(data.get('gender'))
            nickname = str(data.get('nickname'))
            intro = str(data.get('intro'))
            
            registerForm = RegisterForm({'username':username,'password1':password1,'password2':password2,'email':email,'gender':gender,'nickname':nickname,'intro':intro})
            
            if(not registerForm.is_valid()):
                return HttpResponse(json.dumps({'error': 201}, cls=ComplexEncoder))
        
            user=User()
            user.username = username
            user.set_password(password1)
            user.email = email
            user.save()
            
            #用户扩展信息 profile
            profile=UserProfile()
            profile.user_id = user.id # user_id
            profile.gender = gender
            profile.nickname = nickname
            profile.intro = intro
            profile.save()
            
            '''
                #注册成功以后自动进行登录，登录前需要先验证，去掉注释后需要修改your url，HttpResponseRedirect进行页面重定向
                newUser=auth.authenticate(username=username,password=password1)
                if(newUser is not None):
                auth.login(request, newUser)
                return HttpResponseRedirect("/your url/")
                '''

    except Exception as e:
        return HttpResponse(json.dumps({'error': 202}))
    
    return HttpResponse(json.dumps({'error': 0}))

# the Interface of search course list by college id
# REQUIRES: the ajax data should be json data {'college_id': class_id}
# MODIFIES: None
# EFFECTS: return json data {'course_id_list': course_id_list}, course_id_list is a list
# URL: /course/college_course/
@csrf_exempt
def course_by_college(request):
    if(request.method == "POST"):
        data = json.dumps(request.POST)
        data = json.loads(data)
        college_id = int(data.get('college_id'))
        course_id_list = interface.college_course_list(6)
        print(course_id_list)
        return HttpResponse(json.dumps({'course_id_list': course_id_list}, cls=ComplexEncoder))

# the Interface of search course list by class id
# REQUIRES: the ajax data should be json data {'class_id': class_id}
# MODIFIES: None
# EFFECTS: return json data {'course_id_list': course_id_list}, course_id_list is a list
# URL: /course/classification_course/
@csrf_exempt
def course_by_class(request):
    if(request.method == "POST"):
        data = json.dumps(request.POST)
        data = json.loads(data)
        class_id = int(data.get('class_id'))
        course_id_list = interface.classification_course_list(class_id)
        return HttpResponse(json.dumps({'course_id_list': course_id_list}, cls=ComplexEncoder))

# Course Information Interface
# REQUIRES: the ajax data should be json data {'course_id': class_id}
# MODIFIES: None
# EFFECTS: return json data {'course_info': course_info}, course_info is a dict
# URL: /course/course_info/
@csrf_exempt
def course_information(request):
    if(request.method == "POST"):
        data = json.dumps(request.POST)
        data = json.loads(data)
        course_id = int(data.get('course_id','0'))
        course_info = interface.course_information(course_id)
        return HttpResponse(json.dumps({'course_info': course_info}, cls=ComplexEncoder))
'''
def course_visit_count(request):
    if(request.method == "POST"):
        data = json.dumps(request.POST)
        data = json.loads(data)
        course_id = int(data.get('course_id','0'))
'''
@csrf_exempt
def refresh_visit_course_time(request):
    if(request.method == "POST"):
        
        data = json.dumps(request.POST)
        data = json.loads(data)
        course_id = int(data.get('course_id'))
        print (course_id)
        last_view_dict = request.session.get('last_view')
        now_time = datetime.datetime.now()
        course = Course.objects.get(id=course_id)
        if (last_view_dict == None): # have not visited any courses
            request.session['last_view'] = {course_id: str(now_time)}
        else:
            print(last_view_dict)
            last_view = last_view_dict[str(course_id)]
            if (last_view != None): # has visited the course
                last_visit_time = datetime.datetime.strptime(last_view[:-7], "%Y-%m-%d %H:%M:%S")
                if (now_time >= last_visit_time + datetime.timedelta(hours=24)):
                    course.visit_count += 1
                    course.save()
                    request.session['last_view'][course_id] = str(now_time)
            else: # have not visited the course
                course.visit_count += 1
                course.save()
                request.session['last_view'][course_id] = str(now_time)
        print(course.visit_count)
        
        return HttpResponse(json.dumps({'visit_count': course.visit_count}))

# User Information Interface
# REQUIRES: the ajax data should be json data {'username': username}
# MODIFIES: NONE
# EFFECTS: return json data {'user_info': user_info}, user_info is a dict
@csrf_exempt
def user_information(request):
    if(request.method == "POST"):
        #data = json.dumps(request.POST)
        #data = json.loads(request.POST)
        #data = json.loads(request.body.decode())
        #data = request.POST
        username = str(request.POST.get('username'))
        
        user_info = interface.user_information(username)
        return HttpResponse(json.dumps({'user_info': user_info}, cls=ComplexEncoder))

# Resource Information Interface
# REQUIRES: the ajax data should be json data {'resource_id': resource_id}
# MODIFIES: None
# EFFECTS: return json data {'resource_info': resource_info}, resource_info is a dict
# URL:
@csrf_exempt
def resource_information(request):
    if(request.method == "POST"):
        # data = json.loads(request.POST)
        #data = json.loads(request.body.decode())
        resource_id = int(request.POST.get('resource_id'))
        resource_info = interface.resource_information(resource_id)
        print("******************")
        print(resource_info)
        print("******************")
        return HttpResponse(json.dumps({'resource_info': resource_info}, cls=ComplexEncoder))


# Course Contribution List Interface
# REQUIRES: the ajax data should be json data {'course_id', course_id}
# MODIFIES: None
# EFFECTS: return data {'contrib_list': contrib_list}
#          contrib_list is a list whose element is tuples like (user_id, total scores),
#          the list is ordered by total scores
# URL:
@csrf_exempt
def course_contrib_list(request):
    if(request.method == "POST"):
        data = json.loads(request.POST)
        #data = json.loads(request.body.decode())
        course_id = int(data.get('course_id'))
        contrib_list = interface.resource_contribution_list(course_id)
        return HttpResponse(json.dumps({'contrib_list': contrib_list}, cls=ComplexEncoder))

# Check User Status Interface
# REQUIRES: POST method
# MODIFIES: None
# EFFECTS: return json data {'is_login': is_login}
#          is_login is True if request.user.is_authenticated(), else False
# URL: /sign/get_user/
@csrf_exempt
def get_user(request):
    if(request.method == "POST"):
        is_login = request.user.is_authenticated()
        return HttpResponse(json.dumps({'is_login': is_login}, cls=ComplexEncoder))

# rewrite the authenticate method
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # try authenticate the username or the emial
            user = User.objects.get(Q(username=username) | Q(email=username))    # Q offers a '&' operation between two objects
            if(user.check_password(password)):
                return user    # if success, return the user object
        except Exception as e:
            return None    # return None if failed

# Login Interface
# REQUIRES: the ajax data should be json data {'username':username, 'passward':passward
# MODIFIES: request.user.is_authenticated() == True
# EFFECTS: return json data {'error': error}, if login success, error=0,
#          else error is the error list
# URL: /sign/login/
@csrf_exempt
def userLogin(request):
    if(request.method == "POST"):
        data = json.dumps(request.POST)
        data = json.loads(data)
        #data = json.loads(requset.body.decode())
        username = str(data.get('username'))
        print ('username: ' + username)
        password = str(data.get('password'))
        print ('password:' + password)
        
        loginForm = LoginForm({'username': username, 'password': password})
        
        if(loginForm.is_valid()):
            cb = CustomBackend()
            user = cb.authenticate(username=username, password=password)
            if(user is not None and user.is_active):
                auth.login(request, user)
                request.session['username'] = username # store in session
                print ('success')
                return HttpResponse(json.dumps({'error': 0}))
            else:
                return HttpResponse(json.dumps({'error': 101})) # username not exists
        else:
            return HttpResponse(json.dumps({'error': 102}, cls=ComplexEncoder)) # password error

# Logout Interface
# REQUIRES: POST method
# MODIFIES: request.user.is_authenticated() == False
# EFFECTS: return json data {'error': error}, if logout success, error=0,
#          else error is the error list
# URL: /sign/login/
@csrf_exempt
def userLogout(request):
    if(request.method == "POST"):
        #error = []
        try:
            #print(request.user)
            #print(request.user.is_authenticated())
            auth.logout(request)
            #del request.session['username']
            #print(request.user)
            #print(request.user.is_authenticated())
            return HttpResponse(json.dumps({'error': 0}))
        except Exception as e:
            #error.append(str(e))
            #print(error)
            return HttpResponse(json.dumps({'error': 301}))


# use session
@csrf_exempt
def isLoggedIn(request):
    if(request.method == "POST"):
        return HttpResponse(json.dumps({
                                       'username': request.session.get('username',default=None),
                                       }))

def http_get(url):
    response = urllib.request.urlopen(url)
    return response.read()

# Course Search Interface(by ohazyi)
# REQUIRES: the ajax data should be json data {'query': query}
# MODIFIES: NONE
# EFFECTS: return data {'query_list': query_list}
#          query_list is a list whose element is dicts like (user_id, total scores),
#          such as {'college_id': 10, 'class_id': 55, 'name': '安卓', 'credit': 5, 'id': 9, 'hours': 10}
#          the list is ordered by id temporaily (can be modified to revelance)
@csrf_exempt
def course_query(request):
    if(request.method == "POST"):
        data = json.dumps(request.POST) # new
        data = json.loads(data)
        #data = json.loads(request.body.decode())
        query = str(data.get('keyword'))
        print ('query: ' + query)
        cs_url = 'http://10.2.28.124:8080/solr/mynode/select?'#q=Bill&wt=json&indent=true'
        param  = {'q':query, 'fl':'id,name,college_id,class_id,credit,hours', 'rows':'10000', 'wt':'json', 'indent':'true'}
        
        r = requests.get(cs_url, params = param)
        
        query_res = http_get(r.url)
        #json_r = bytes.decode(query_res)
        json_r = json.loads(bytes.decode(query_res))
        query_list = json_r['response']['docs']
        print (query_list)
        print(len(query_list))
        return HttpResponse(json.dumps({'query_list': query_list}, cls=ComplexEncoder))

# Course id list(by ohazyi)
# REQUIRES: the ajax data should be json data {'query': query}
# MODIFIES: NONE
# EFFECTS: return data {'resource_id_list': query_list}
#          query_list is a list whose course_id = request.get('id') is dicts like (1, 2, 3, 4, 6)...
# retrun like: {"resource_id_list": [1, 2, 3, 4, 6]}
@csrf_exempt
def resource_id_list(request):
    if(request.method == "POST"):
        data = json.dumps(request.POST) # new
        data = json.loads(data)
        #data = json.loads(request.body.decode())
        course_id = str(data.get('course_id'))
        print ('course_id: ' + course_id)
        res = interface.resource_courseid_list(course_id)
        return HttpResponse(json.dumps({'resource_id_list': res}, cls=ComplexEncoder))

# Handle the uploaded resource
def handle_upload_resource(f, path):
    t = path.split("/")
    file_name = t[-1]
    t.remove(t[-1]) 
    t.remove(t[0])
    path = "/".join(t)
    try:
        if(not os.path.exists(path)):
            os.makedirs(path)
        file_name = path + "/" + file_name
        print(file_name)
        destination = open(file_name, 'wb+')
        for chunk in f.chunks():
            destination.write(chunk)
            destination.close()
    except Exception as e: 
        print(e)
    return file_name

# Resource Upload Interface
# REQUIRES: request.POST['course_code'] != None && request.POST['only_url'] == True/False && request.FILES['file'] != None ,the uploaded should less than 10MB
# MODIFIES: store the uploaded file to iCourse/media/uploads/%Y/%m && insert a record to backend_resource table in database
# EFFECTS: return json data {'error':error}, if upload success, error = 0, else error = 1
@csrf_exempt
def resourceUpload(request):
    if(request.method == 'POST'):
        errors = []
        if(not request.user.is_authenticated()):    # if the user is not authenticated
            return HttpResponse(json.dumps({'error':1}))
        upload_user_id = request.user.id
        data = json.loads(request.POST)
        intro = str(data.get('intro'))
        #course_id = int(data.get('course_id'))
        course_code = str(data.get('course_code'))
        only_url = bool(data.get('only_url'))     # only_url = True 表示只上传了一个链接,该链接应当保存在resource的url字段,link字段应该为None
        if(only_url):
            url = str(data.get('url'))
            name = str(data.get('name'))
            size = 0
            RUForm = ResourceUploadForm({'name':name, 'size':size, 'upload_user_id':upload_user_id, 'course_code':course_code})
            if(RUForm.is_valid()):
                resource_up = Resource()
                resource_ip.only_url = True
                resource_up.name = name
                resource_up.size = size     # bytes
                resource_up.intro = intro
                resource_up.url = url
                resource_up.course_code = course_code
                resource_up.upload_user_id = upload_user_id
                resource_up.save()
                return HttpResponse(json.dumps({'error':0}))
            else:
                errors.extend(RUForm.errors.values())
                return HttpResponse(json.dumps({'error':1}))
        else:
            name = str(request.FILES['file'].name)
            size = int(request.FILES['file'].size)
            RUForm = ResourceUploadForm({'name':name, 'size':size, 'upload_user_id':upload_user_id, 'course_id':course_code})
            if(RUForm.is_valid()):
                resource_up = Resource()
                resource_up.only_url = False
                resource_up.name = name
                resource_up.link = request.FILES['file']
                resource_up.size = size
                resource_up.intro = intro
                resource_up.course_code = course_code
                resource_up.upload_user_id = upload_user_id
                resource_up.save()
                handle_upload_resource(request.FILES['file'], resource_up.link.url)
                return HttpResponse(json.dumps({'error':0}))
            else:
                errors.extend(RUForm.errors.values())
                return HttpResponse(json.dumps({'error':1}))

# Download Interface
# REQUIRES: GET method
# MODIFIES: None
# EFFECTS: return a StreamingHttpResponse if success
# URL: /download/(\d+)/, (\d+) is resource_id
def download(request, resource_id): # 2 parameters
    if(request.method == "GET"):
        # alpha阶段暂时不实现下载表的写入
        '''
        user_id = request.user.id
        resource_id = int(data.get('resource_id'))
        download_record = R_Resource_User_Download.objects.create(user_id=user_id, resource_id=resource_id)
        download_record.save()
        '''
        resource = Resource.objects.get(id=resource_id)
        resource.download_count +=1 # 下载量+1
        resource.save()
        if(resource.only_url):    # 若仅保存了一个链接
            return HttpResponse(resource.url)
        link = resource.link.url
        real_name = resource.name
        t = link.split("/")
        file_name = t[-1]
        t.remove(t[-1])
        t.remove(t[0])
        file_path = "/".join(t)
        def file_iterator(file_name, file_path, chunk_size=512):
            path = file_path + "/" + file_name
            with open(path, 'rb') as f:       # must use 'rb'
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break
        try:
            response = StreamingHttpResponse(file_iterator(file_name, file_path))
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="{0}"'.format(real_name) # display the real_name of the file when user download it
            #print(response)
        except Exception as e:
            #print(e)
            return HttpResponse("未找到该文件")
        return response


# Latest Resource Information list
@csrf_exempt
def latest_resource_info(request):
    if(request.method == 'POST'):
        # data = json.loads(request.POST)
        course_id = int(request.POST.get('course_id'))
        number = int(request.POST.get('number'))
        result = interface.resource_information_list(course_id, number)
        return HttpResponse(json.dumps({'result': result}))
