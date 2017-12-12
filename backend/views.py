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
from django.db.models import Q, Sum
from django.views.generic.base import View
from django.shortcuts import render
from .email_send import *

import requests
import urllib.request
import json
import datetime
from datetime import date

import os

from django.utils.http import urlquote

from backend import notification

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
            user.is_active = False
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
    #发送验证邮件
    send_register_email(email, "register")
    print('finish send email')
    return HttpResponse(json.dumps({'error': 0}))

# modified by xdt 2017.11.8
# the Interface of search course list by college id
# REQUIRES: the ajax data should be json data {'college_id': class_id}
# MODIFIES: None
# EFFECTS: return json data {'course_info_list': course_info_list}, course_info_list is a list
# URL: /course/college_course/
@csrf_exempt
def course_by_college(request):
    if(request.method == "POST"):
        data = json.dumps(request.POST)
        data = json.loads(data)
        college_id = int(data.get('college_id'))
        course_info_list = interface.college_course_list(college_id)
        return HttpResponse(json.dumps({'course_info_list': course_info_list}, cls=ComplexEncoder))

# modified by xdt 2017.11.8
# the Interface of search course list by class id
# REQUIRES: the ajax data should be json data {'class_id': class_id}
# MODIFIES: None
# EFFECTS: return json data {'course_info_list': course_info_list}, course_info_list is a list
# URL: /course/classification_course/
@csrf_exempt
def course_by_class(request):
    if(request.method == "POST"):
        data = json.dumps(request.POST)
        data = json.loads(data)
        class_id = int(data.get('class_id'))
        course_info_list = interface.classification_course_list(class_id)
        return HttpResponse(json.dumps({'course_info_list': course_info_list}, cls=ComplexEncoder))

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
        a = request.user.id
        course_id = int(data.get('course_id'))
        course_info = interface.course_information(course_id)
        return HttpResponse(json.dumps({'course_info': course_info}, cls=ComplexEncoder))

# Visit Course Interface
# REQUIRES: the ajax data should be json data {'post_id': post_id}
# MODIFIES: Post.click_count
# EFFECTS: return json data {'click_count': click_count}, click_count is a integer
# URL: /course/click_count/
@csrf_exempt
def refresh_click_post_count(request):
    def refresh(now_time, post_id):
        post = Post.objects.get(id=post_id)
        post.click_count += 1
        post.save()
        request.session.modified = True
        request.session['last_post_click'][post_id] = str(now_time)
        return HttpResponse(json.dumps({'click_count': post.click_count}))

    if(request.method == "POST"):
        data = json.dumps(request.POST)
        data = json.loads(data)
        post_id = int(data.get('post_id'))

        last_post_click_dict = request.session.get('last_post_click')
        now_time = datetime.datetime.now()
        if (last_post_click_dict == None): # have not clicked any posts
            request.session['last_post_click'] = {}
            return refresh(now_time, post_id)
        else:
            print('last_post: ', last_post_click_dict)
            last_post_click = last_post_click_dict.get(str(post_id))
            if (last_post_click != None): # has clicked the post
                last_click_time = datetime.datetime.strptime(last_post_click[:-7], "%Y-%m-%d %H:%M:%S")
                if (now_time >= last_click_time + datetime.timedelta(hours=24)):
                    return refresh(now_time, post_id)
            else: # have not clicked the post
                return refresh(now_time, post_id)
        return HttpResponse(json.dumps({'click_count': post.objects.get(id=post_id).click_count}))

'''
def course_visit_count(request):
    if(request.method == "POST"):
        data = json.dumps(request.POST)
        data = json.loads(data)
        course_id = int(data.get('course_id','0'))
'''
# Visit Course Interface
# REQUIRES: the ajax data should be json data {'course_id': course_id}
# MODIFIES: Course.visit_count
# EFFECTS: return json data {'visit_count': visit_count}, visit_count is a integer
# URL: /course/visit_count/
@csrf_exempt
def refresh_visit_course_count(request):
    def refresh(now_time, course_id):
        course = Course.objects.get(id=course_id)
        course.visit_count += 1
        course.save()
        request.session.modified = True
        request.session['last_view'][course_id] = str(now_time)
        return HttpResponse(json.dumps({'visit_count': course.visit_count}))

    if(request.method == "POST"):
        data = json.dumps(request.POST)
        data = json.loads(data)
        course_id = int(data.get('course_id'))

        last_view_dict = request.session.get('last_view')
        now_time = datetime.datetime.now()
        if (last_view_dict == None): # have not visited any courses
            request.session['last_view'] = {}
            return refresh(now_time, course_id)
        else:
            print(last_view_dict)
            last_view = last_view_dict.get(str(course_id))
            if (last_view != None): # has visited the course
                last_visit_time = datetime.datetime.strptime(last_view[:-7], "%Y-%m-%d %H:%M:%S")
                if (now_time >= last_visit_time + datetime.timedelta(hours=24)):
                    return refresh(now_time, course_id)
            else: # have not visited the course
                return refresh(now_time, course_id)
        return HttpResponse(json.dumps({'visit_count': Course.objects.get(id=course_id).visit_count}))
        
# Resource Download Count Interface
# REQUIRES: the ajax data should be json data {'resource_id': resource_id}
# MODIFIES: Resource.download_id
# EFFECTS: return json data {'download_count': download_count}, download_count is a integer
# URL: /course/course_info/
@csrf_exempt
def refresh_download_resource_count(request):
    def refresh(now_time, resource_id):
        resource = Resource.objects.get(id=resource_id)
        resource.download_count += 1
        resource.save()
        request.session.modified = True
        request.session['last_download'][resource_id] = str(now_time)
        return HttpResponse(json.dumps({'download_count': resource.download_count}))

    if(request.method == "POST"):
        data = json.dumps(request.POST)
        data = json.loads(data)
        resource_id = int(data.get('download_count'))

        last_download_dict = request.session.get('last_download')
        now_time = datetime.datetime.now()
        if (last_download_dict == None): # have not visited any courses
            request.session['last_download'] = {}
            return refresh(now_time, resource_id)
        else:
            print(last_download_dict)
            last_download = last_download_dict.get(str(resource_id))
            if (last_download != None): # has visited the course
                last_download_time = datetime.datetime.strptime(last_download[:-7], "%Y-%m-%d %H:%M:%S")
                if (now_time >= last_download_time + datetime.timedelta(hours=24)):
                    return refresh(now_time, resource_id)
            else: # have not visited the course
                return refresh(now_time, resource_id)
        return HttpResponse(json.dumps({'download_count': Resource.objects.get(id=resource_id).download_count}))

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
        if ('username' in request.POST.keys()):
            username = str(request.POST.get('username'))
            user_info = interface.user_information_by_username(username)
        elif ('id' in request.POST.keys()):
            user_id = str(request.POST.get('id'))
            user_info = interface.user_information_by_id(user_id)
        else:
            return HttpResponse(json.dumps({}))
        print("******************")
        print(user_info)
        print("******************")
        return HttpResponse(json.dumps({'user_info': user_info}, cls=ComplexEncoder))

@csrf_exempt
def get_username(request):
    if(request.method == "POST"):
        user_id = str(request.POST.get('id'))


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
                return HttpResponse(json.dumps({'error': 0, 'username':user.username}))
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
        username = interface.get_username(request.session.get('username',default=None))
        return HttpResponse(json.dumps(username))

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
        param  = {'q':query, 'fl':'id,name,college_id,class_id,credit,hours,score', 'rows':1500, 'wt':'json', 'indent':'true'}

        r = requests.get(cs_url, params = param)

        query_res = http_get(r.url)
        #json_r = bytes.decode(query_res)
        json_r = json.loads(bytes.decode(query_res))
        query_list = json_r['response']['docs']
        print (query_list)
        ans = []
        for i in query_list:
            #print("*****   ", i)
            #print("$$$$$   ", i['score'])
            if (i['score']>=5):
                ans.append(i)
        print("---------------------------------------")
        print("All: ",len(query_list), "score > 5:",len(ans))
        print(ans)
        return HttpResponse(json.dumps({'query_list': ans}, cls=ComplexEncoder))
        #print(json.dumps({'query_list': query_list}))
        #print(json.dumps({'query_list': ans}))


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
        # print ('course_id: ' + course_id)
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
        print(request.user.id)
        data = request.POST
        intro = str(data.get('intro'))
        #course_id = int(data.get('course_id'))
        course_code = str(data.get('course_code'))
        only_url = str(data.get('only_url'))     # only_url = True 表示只上传了一个链接,该链接应当保存在resource的url字段,link字段应该为None
        if(only_url == 'True' or only_url == 'true'):
            only_url = True
        elif(only_url == 'False' or only_url == 'false'):
            only_url = False
        else:
            return HttpResponse(json.dumps({'error':1}))
        if(only_url):
            url = str(data.get('url'))
            name = str(data.get('name'))
            size = 0
            RUForm = ResourceUploadForm({'name':name, 'size':size, 'upload_user_id':upload_user_id, 'course_code':course_code})
            if(RUForm.is_valid()):
                resource_up = Resource()
                resource_up.only_url = True
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
            flag = False
            for ch in real_name:
                if(ord(ch) > 127):
                    flag = True
            if(flag):
                response['Content-Disposition'] = 'attachment;filename="{0}"'.format(urlquote(real_name))
            else:
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

# Repost Interface
# REQUIRES: POST method, only anthenticated user can report, need {'be_reported_resource_id': be_reported_resource_id}
# MODIFIES: insert a record in backend_report table in database
# EFFECTS: if success, return {'error': 0}, else return {'error': 1}
# URL: 暂时未定
@csrf_exempt
def user_report(request):
    if(request.method == 'POST'):
        if(not request.user.is_authenticated()):
            return HttpResponse(json.dumps({'error': 1}))
        be_reported_resource_id = request.POST.get('be_reported_resource_id')
        report_user_id = request.user.id
        report_content = request.POST.get('report_content', "用户未填写举报理由")
        report = Report.objects.create(report_user_id=report_user_id, be_reported_resource_id=be_reported_resource_id, report_content = report_content)
        report.save()
        return HttpResponse(json.dumps({'error':0}))

# User Information Modify Interface
# REQUIRES: need {'nickname':nickname, 'gender':gender, 'intro':intro, 'college_id':college_id}
# MODIFIES: modify user information in backend_userprofile
# EFFECTS: if success, return {'error': 0}, else return {'error': 1}
# URL:/user/modify/info/
@csrf_exempt
def user_modify_info(request):
    errors = []
    if(request.method == 'POST'):
        if(not request.user.is_authenticated()):
            return HttpResponse(json.dumps({'error':1}))
        print(request.POST)
        nickname = str(request.POST.get('nickname'))
        gender = str(request.POST.get('gender'))
        intro = str(request.POST.get('intro'))
        college_id = int(request.POST.get('college_id'))
        UIMForm = UserInfoModifyForm({'nickname':nickname, 'gender':gender, 'intro':intro, 'college_id':college_id})

        if(UIMForm.is_valid()):
            userprofile = UserProfile.objects.get(user_id=request.user.id)
            userprofile.nickname = nickname
            userprofile.gender = gender
            userprofile.intro = intro
            userprofile.college_id = college_id
            userprofile.save()
            print('Modify Success')
            return HttpResponse(json.dumps({'error':0}))
        else:
            errors.extend(UIMForm.errors.values())
            print(errors)     
            return HttpResponse(json.dumps({'error':1}))

@csrf_exempt
def ip_record(request):
    if (request.method == 'POST'):
        if ('HTTP_X_FORWARDED_FOR' in request.META.keys()):  
            ip = request.META['HTTP_X_FORWARDED_FOR']  
        else:  
            ip = request.META['REMOTE_ADDR']  
        print('ip:', ip)
        interface.refresh_ip_visit_info(str(ip))
        return HttpResponse(json.dumps({'result':0}))

# Publish Post Interface
# URL: /post/posting/publish/
@csrf_exempt
def posting_publish(request):
    errors = []
    if(request.method == 'POST'):
        data = request.POST
        course_id = int(data.get('course_id'))
        category = int(data.get('category'))
        title = str(data.get('title'))
        content = str(data.get('content'))
        user_id = request.user.id
        editor = int(data.get('editor'))
        intro = str(data.get('intro'))
        post_form = PostForm({'title':title, 'course_id':course_id, 'category':category})
        if(post_form.is_valid()):
            post = Post()
            post.title = title
            post.course_id = course_id
            post.category = category
            post.main_follow_id = -1;
            post.intro = intro;
            post.save()
        else:
            errors.extend(post_form.errors.values())
            print(errors)
            return HttpResponse(json.dumps({'error': 1}))
        follow_form = FollowForm({'post_id':post.id, 'user_id':user_id, 'content':content, 'editor':editor})
        print(post.id,user_id,content,editor)
        if(follow_form.is_valid()):
            follow = Follow()
            follow.post_id = post.id
            follow.user_id = user_id
            follow.content = content
            follow.editor = editor
            follow.is_main = True
            follow.save()
            post.main_follow_id = follow.id # renew post.main_follow_id
            post.save()
        else:
            errors.extend(follow_form.errors.values())
            print(errors)
            post.delete()
            return HttpResponse(json.dumps({'error': 1}))
        return HttpResponse(json.dumps({'error': 0}))

# Publish Follow Interface
# URL: /post/follow/publish/
@csrf_exempt
def follow_publish(request):
    if(request.method == 'POST'):
        data = request.POST
        post_id = int(data.get('post_id'))
        content = str(data.get('content'))
        user_id = request.user.id
        editor = int(data.get('editor'))
        # published?
        follow_form = FollowForm({'post_id':post_id, 'user_id':user_id, 'content':content, 'editor':editor})
        if(follow_form.is_valid()):
            result = Follow.objects.filter(post_id=post_id,user_id=user_id)
            if(len(result) > 0):
                return HttpResponse(json.dumps({'error': 1}))
            follow = Follow()
            follow.post_id = post_id
            follow.user_id = user_id
            follow.content = content
            follow.editor = editor
            follow.is_main = False
            follow.save()
            post = Post.objects.get(id=post_id) # renew post.follow_count
            post.follow_count += 1
            post.save()
        else:
            return HttpResponse(json.dumps({'error': 1}))
        return HttpResponse(json.dumps({'error': 0}))

# Publish Comment Interface
# URL: /post/comment/publish/
@csrf_exempt
def comment_publish(request):
    if(request.method == 'POST'):
        data = request.POST
        user_id = request.user.id
        follow_id = int(data.get('follow_id'))
        to_comment_id = int(data.get('to_comment_id'))
        content = str(data.get('content'))
        follow_comment_form = FollowCommentForm({'user_id':user_id, 'follow_id':follow_id, 'content':content})
        if(follow_comment_form.is_valid()):
            follow_comment = Follow_Comment()
            follow_comment.user_id = user_id
            follow_comment.follow_id = follow_id
            follow_comment.to_comment_id = to_comment_id
            follow_comment.content = content
            follow_comment.save()
            follow = Follow.objects.get(id=follow_id) # renew follow.comment_count
            follow.comment_count += 1
            follow.save()
        else:
            return HttpResponse(json.dumps({'error': 1}))
        return HttpResponse(json.dumps({'error': 0}))

# Follow Evaluate Interface
# URL: /post/follow/evaluate
@csrf_exempt
def follow_evaluate(request):
    if(request.method == 'POST'):
        data = request.POST
        user_id = request.user.id
        follow_id = int(data.get('follow_id'))
        grade = int(data.get('grade'))
        follow_evaluation_form = FollowEvaluationForm({'user_id':user_id, 'follow_id':follow_id, 'grade':grade})
        if(follow_evaluation_form.is_valid()):
            result = Follow_Evaluation.objects.filter(user_id=user_id, follow_id=follow_id)
            if(len(result) > 0): # if the user has evaluated the follow
                return HttpResponse(json.dumps({'error': 1}))
            else:
                follow_evaluation = Follow_Evaluation()
                follow_evaluation.user_id = user_id
                follow_evaluation.follow_id = follow_id
                follow_evaluation.grade = grade
                follow_evaluation.save()
                follow = Follow.objects.get(id=follow_id) # renew follow pos_eva_count or neg_eav_count
                if(grade == 1):
                    follow.pos_eva_count += 1
                else: # grade == -1
                    follow.neg_eva_count += 1
                follow.save()
        else:
            return HttpResponse(json.dumps({'error': 1}))
        return HttpResponse(json.dumps({'error': 0}))

# Get Post Id List Interface
# URL: /post/id/list/
@csrf_exempt
def post_id_list(request):
    if(request.method == 'POST'):
        course_id = int(request.POST.get('course_id'))
        id_list = list(Post.objects.filter(course_id=course_id).order_by('-update_time').values_list('id', flat=True))
        return HttpResponse(json.dumps({'id_list': id_list}))

# Post Information List Interface
# URL: /post/information/list/
@csrf_exempt
def post_infor_list(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        id_list = data.get('id_list')
        print(id_list)
        if(',' in id_list):
            id_list = id_list[1:-1].split(',')
        else:
            id_list = [id_list[1:-1]]
        print(id_list)
        get_content = str(data.get('get_content'))
        get_grade = str(data.get('get_grade'))
        get_follow_count = str(data.get('get_follow_count'))
        if(get_content == 'True' or get_content == 'true'):
            get_content = True
        elif(get_content == 'False' or get_content == 'false'):
            get_content = False
        else:
            return HttpResponse(json.dumps({'error':1}))
        if(get_grade == 'True' or get_grade == 'true'):
            get_grade = True
        elif(get_grade == 'False' or get_grade == 'false'):
            get_grade = False
        else:
            return HttpResponse(json.dumps({'error':1}))
        if(get_follow_count == 'True' or get_follow_count == 'true'):
            get_follow_count = True
        elif(get_follow_count == 'False' or get_follow_count == 'false'):
            get_follow_count = False
        else:
            return HttpResponse(json.dumps({'error':1}))
        info_list = []
        for item in id_list:
            item = int(item)
            result = Post.objects.filter(id=item)
            if(len(result) != 1):
                # error
                continue
            post = result.values('title', 'category', 'click_count', 'update_time','follow_count', 'main_follow_id', 'intro')[0]
            post['grade_sum'] = Follow.objects.filter(post_id=item).aggregate(grade_sum=Sum('pos_eva_count'))['grade_sum']
            main_follow = Follow.objects.get(id=post['main_follow_id'])
            post['user_id'] = main_follow.user_id
            post['content'] = main_follow.content
            post['user_name'] = User.objects.get(id=post['user_id']).username
            #post['update_time'] = '2017-11-18'
            info_list.append(post)
        return HttpResponse(json.dumps({'info_list':info_list},cls=ComplexEncoder))


# Get Follow Id List Interface
# URL: /follow/id/list/
@csrf_exempt
def follow_id_list(request):
    if(request.method == 'POST'):
        post_id = int(request.POST.get('post_id'))
        print(post_id)
        result = Post.objects.filter(id=post_id)
        if(len(result) != 1):
            return HttpResponse(json.dumps({'main_id':-1, 'id_list':[]}))
        main_id = result[0].main_follow_id
        print(main_id)
        id_list = list(Follow.objects.filter(post_id=post_id).order_by('-pos_eva_count','neg_eva_count').values_list('id', flat=True))
        id_list.remove(main_id)
        return HttpResponse(json.dumps({'main_id':main_id, 'id_list':id_list}))

# Follow Information List Interface
# URL: /follow/info/list/
@csrf_exempt
def follow_info_list(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        id_list = data.get('id_list')
        print(id_list)
        if(',' in id_list):
            id_list = id_list[1:-1].split(',')
        else:
            id_list = [id_list[1:-1]]
        print(id_list)
        cur_user_id = request.user.id
        info_list = []
        for item in id_list:
            item = int(item)
            result = Follow.objects.filter(id=item)
            if(len(result) != 1):
                # error
                continue
            follow = result.values('user_id', 'post_time', 'edit_time', 'content', 'pos_eva_count', 'neg_eva_count')[0]
            follow['username'] = User.objects.get(id=follow['user_id']).username
            if(follow['user_id'] == cur_user_id):
                follow['is_poster'] = True
            else:
                follow['is_poster'] = False
            if(cur_user_id == None):
                follow['evaluated_grade'] = 0
            else:
                result = Follow_Evaluation.objects.filter(user_id=cur_user_id, follow_id=item).values_list('grade', flat=True)
                if(len(result) == 0):
                    follow['evaluated_grade'] = 0
                else:
                    follow['evaluated_grade'] = result[0]
            info_list.append(follow)
            # print(info_list)
        return HttpResponse(json.dumps({'info_list':info_list},cls=ComplexEncoder))

# get follow content by user_id and post_id
# URL: /follow/get/userpost/
@csrf_exempt
def userid_postid_get_follow(request):
    if(request.method == 'POST'):
        data = request.POST
        post_id = int(data.get('post_id'))
        user_id = int(data.get('user_id'))
        result = Follow.objects.filter(post_id=post_id,user_id=user_id).values('content', 'editor')
        if(len(result) != 1):
            # error
            return HttpResponse(json.dumps({'content':'', 'editor':-1}))
        return HttpResponse(json.dumps({'content':result[0]['content'], 'editor':result[0]['editor']}))

# Get Comment Id List Interface
# URL: /comment/id/list/
@csrf_exempt
def comment_id_list(request):
    if(request.method == 'POST'):
        follow_id = int(request.POST.get('follow_id'))
        id_list = list(Follow_Comment.objects.filter(follow_id=follow_id).order_by('-post_time').values_list('id', flat=True))
        return HttpResponse(json.dumps({'id_list': id_list}))

# Comment Information List Interface
# URL: /comment/info/list/
@csrf_exempt
def comment_info_list(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        id_list = data.get('id_list')
        if(',' in id_list):
            id_list = id_list[1:-1].split(',')
        else:
            id_list = [id_list[1:-1]]
        info_list = []
        for item in id_list:
            item = int(item)
            result = Follow_Comment.objects.filter(id=item)
            if(len(result) != 1):
                # error
                continue;
            follow_comment = result.values('user_id', 'to_comment_id', 'post_time', 'content')[0]
            follow_comment['username'] = User.objects.get(id=follow_comment['user_id']).username
            if(follow_comment['to_comment_id'] == -1):
                follow_comment['to_user_id'] = -1
                follow_comment['to_username'] = ''
            else:
                follow_comment['to_user_id'] = Follow_Comment.objects.get(id=follow_comment['to_comment_id']).user_id
                follow_comment['to_username'] = User.objects.get(id=follow_comment['to_user_id']).username
            info_list.append(follow_comment)
        return HttpResponse(json.dumps({'info_list': info_list}, cls=ComplexEncoder))

# get top list_len post id list order by update time
# URL: 暂时未定
@csrf_exempt
def post_id_list_by_update_time(request):
    if(request.method == 'POST'):
        list_len = int(request.POST.get('list_len'))
        result = Post.objects.all().order_by('-update_time').values_list('id', flat=True)
        id_list = []
        count = 0
        for i in result:
            id_list.append(i)
            count = count + 1
            if(count == list_len):
                break
        return HttpResponse(json.dumps({'id_list': id_list}))

# get top list_len post id list order by click count
# URL: 暂时未定
@csrf_exempt
def post_id_list_by_click_count(request):
    if(request.method == 'POST'):
        list_len = int(request.POST.get('list_len'))
        result = Post.objects.all().order_by('-click_count','-update_time').values_list('id', flat=True)
        id_list = []
        count = 0
        for i in result:
            id_list.append(i)
            count = count + 1
            if(count == list_len):
                break
        return HttpResponse(json.dumps({'id_list': id_list}))

#---------------------------------------------------------------
# 根据用户对资源的打分进行数据更新
# REQUIRES:      变量名|类型|说明
#          resource_id|int|资源id
#              user_id|int|用户id
#                grade|int|评分，0~5
# MODIFIES: None
# EFFECTS: 更新到数据库backend_evualtion
# modified by xindetai 12.8
@csrf_exempt
def resource_evaluate(request): #resource_id, user_id, grade:
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        
        resource_id = str(data.get('resource_id'))
        user_id = str(request.user.id)
        grade = int(data.get('grade'))
        
        print ('resource_id: ' + resource_id + 'user_id: '+ user_id + 'grade: ' +str(grade))
        if (grade >= 1 and grade <= 5): #评分必须在1-5之间
            eva = Resource_Evaluation()
            eva.resource_id = resource_id
            eva.user_id = user_id
            eva.grade = grade
            eva.save()
            return HttpResponse(json.dumps({'error':0}))
        return HttpResponse(json.dumps({'error':1}))

#---------------------------------------------------------------
# 查看用户对资源的评分情况，返回两个值，一个是查看这个资源的平均评分，一个是用户给这个资源的评分
# REQUIRES:      变量名|类型|说明
#          resource_id|int|资源id
#              user_id|int|用户id
# MODIFIES: None
# EFFECTS: 返回两个值：1、avg_grade即评价平均分，浮点型(float), 没有一个人评价就是-1
#                    2、user_grade，用户给予的评价，int型号，未评价返回-1
# URL:/resource/evaluation/grade/count/
# modified by xdt 12.9
@csrf_exempt
def resource_evaluation_grade_count(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        
        resource_id = str(data.get('resource_id'))
        user_id = request.user.id
        result = Resource_Evaluation.objects.filter(resource_id = resource_id, user_id = user_id)
        
        user_grade = -1 #没有人评价，个人评价值默认为-1
        if (len(result) != 0):
            user_grade = result[0].grade #每个人只允许评价一次，即防止刷评价现象，所以只要去除result[0]
    
        result2 = Resource_Evaluation.objects.filter(resource_id = resource_id)
        
        tot_grade = 0
        avg_grade = -1 #没有人评价，平均值默认值为-1
        if (len(result2) != 0):
            for i in range(0, len(result2)):
                tot_grade += result2[i].grade
                avg_grade = float(tot_grade) / float(len(result2))
        print("tot_grade = ",tot_grade,"avg_grade = ", avg_grade)
        return HttpResponse(json.dumps({'avg_grade': avg_grade, 'user_grade': user_grade, 'grade_count': len(result2)}))


#求某个资源的评分的平均分
def avg_score(resource_id):
    result2 = Resource_Evaluation.objects.filter(resource_id = resource_id)
    tot_grade = 0
    avg_grade = -1 #没有人评价，平均值默认值为-1
    if (len(result2) != 0):
        for i in range(0, len(result2)):
            tot_grade += result2[i].grade
            avg_grade = float(tot_grade) / float(len(result2))
    print("tot_grade = ",tot_grade,"avg_grade = ", avg_grade)
    return avg_grade

#---------------------------------------------------------------
# 获取课程贡献分列表
# REQUIRES:      变量名|类型|说明
#            course_id|int|课程id
#          资源id必须是存在资源的id，否则返回error:1
# MODIFIES: None
# EFFECTS:
#        返回contri_list	list[dict{}]	课程贡献度字典，按照contri从高到低排序
#        字典包括：
#        变量名|类型|说明
#        :-:|:-:|:-:
#        user_id|int|用户id
#        username|str|用户名
#        contri|float|贡献度（保留一位小数）
    #某用户在某一课程下贡献度计算公式：（即同一用户在不同课程下贡献度可能不同）
    #资源贡献度 = 上传资源数∑(下载量*评分平均值/10)
    #论坛贡献度 = 发布帖子数∑(点击量/10) + 发布跟帖数∑((赞同数2) / (赞同数+反对数))
    #总贡献度 = 资源贡献度 + 论坛贡献度
# url: /course/contri/
# modified by xindetai 12.9
@csrf_exempt
def course_contri_list(request):
    
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        
        course_id = str(data.get('course_id'))
        
        c = interface.course_information(course_id)
        if (not c): #如果c为空，代表不存在这样id的课程
            return HttpResponse(json.dumps({'error':1}))
        course_code = c["course_code"]

        users = User.objects.filter()
        resources = Resource.objects.filter(course_code = course_code)
        print(len(resources))
        dict = {}
        for i in range(0, len(resources)): #遍历所有资源
            download_count = resources[i].download_count
            grade = avg_score(resources[i].id)
            if (grade == -1):
                grade = 5 #没有人评价，评分就设置为5
            contrib_r = float(download_count) * float(grade) / 10.0

            if (not resources[i].upload_user_id in dict):
                dict[resources[i].upload_user_id] = contrib_r
            else:
                dict[resources[i].upload_user_id] = dict[resources[i].upload_user_id] + contrib_r


        posts = Post.objects.filter(course_id = course_id)
        for i in range(0, len(posts)): #遍历所有帖子
            click_count = posts[i].click_count
            tmp = Follow.objects.filter(id = posts[i].main_follow_id)
            
            post_user_id = tmp[0].user_id
            if (not post_user_id in dict):
                dict[post_user_id] = float(click_count/10.0)
            else:
                dict[post_user_id] = dict[post_user_id] + float(click_count/10.0)

            posts_follow = Follow.objects.filter(post_id = posts[i].id)
            for j in range(0, len(posts_follow)): #遍历该帖子下的所有跟帖
                pos_eva_count = posts_follow[j].pos_eva_count
                neg_eav_count = posts_follow[j].neg_eva_count
                if (not posts_follow[j].user_id in dict):
                    dict[posts_follow[j].user_id] = float(pos_eva_count*pos_eva_count/(pos_eva_count+neg_eav_count))
                else:
                    dict[posts_follow[j].user_id] = dict[posts_follow[j].user_id] + float(2.0*(pos_eva_count)/(pos_eva_count+neg_eav_count))

        ans = sorted(dict.items(), key=lambda item:item[1],reverse=True)
        dict_list = []
        print(ans)

        for id, score in ans:
            dict_tmp = {}
            u_name = interface.get_username_by_id(id)
            if (not u_name): #返回的是”“ 即不存在该用户，跳过
                continue
#            if (u_name == "iCourse"): #跳过iCourse用户
#               continue
            dict_tmp["username"] = u_name
            dict_tmp["user_id"] = id
            dict_tmp["contri"] = round(score, 1)
            
            dict_list.append(dict_tmp)
        print(dict_list)

        return HttpResponse(json.dumps({'contri_list': dict_list}, cls=ComplexEncoder))


#---------------------------------------------------------------
# 获取某一类别资源
# REQUIRES:      变量名|类型|说明
#            course_id|int|课程id
#          资源id必须是存在资源的id，否则返回error:1
#           type|int|资源类别: ppt、doc(txt)、pdf、pict、other、all
# MODIFIES: None
# EFFECTS: 返回resource\_class\_id\_list|list[int]|该课程下的资源id列表
@csrf_exempt
def resource_class_id_list(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
    
        course_id = str(data.get('course_id'))
        type = str(data.get('type'))

        c = interface.course_information(course_id)
        if (not c): #如果c为空，代表不存在这样id的课程
            return HttpResponse(json.dumps({'error':1}))

        course_code = c["course_code"]
            
        resources = Resource.objects.filter(course_code = course_code)
        ans = []
        for i in range(0, len(resources)):
            name = resources[i].name
            pos = name.rfind('.')
            if (pos == -1):
                continue
            if (name[pos+1:len(name)] == type):
                ans.append(resources[i].id)

        print(ans)
        return HttpResponse(json.dumps({'resource_class_id_list': ans}, cls=ComplexEncoder))


#---------------------------------------------------------------
# 根据课程列别获取课程
# REQUIRES:      变量名|类型|说明
#              type|string|课程类别:'工程基础类','数学与自然科学类','语言类','博雅类','核心通识类','体育类','一般通识类','核心专业类','一般专业类'
#               必须是这9个之一，否则返回error:1
# MODIFIES: None
# EFFECTS: 返回course\_type\_list|list[int]|该类别下的课程的list,其中每个都是一个字典，存着课程的信息
#          query_list is a list whose element is dicts like (user_id, total scores),
#          such as {'credit': Decimal('3.0'), 'class_id': 1, 'teacher': '杨振宇', 'name': '弹性力学*(全汉语)', 'college_id': 5, 'hours': None, 'visit_count': 0, 'id': 1733, 'course_code': 'B3B05314B'}
@csrf_exempt
def course_type_list(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        type = str(data.get('type'))
        
        dict = {'工程基础类': 1, '数学与自然科学类': 2, '语言类':3, '博雅类':4, '核心通识类': 5, '体育类': 6, '一般通识类': 7, '核心专业类': 8, '一般专业类':9}
        if (not type in dict):
            return HttpResponse(json.dumps({'error':1}))
        type_id = dict[type]
        
        courses = Course.objects.filter(class_id = type_id)
        ans = []
        for i in range(0, len(courses)):
            course_info = {}
            course_info["id"] = courses[i].id
            course_info["name"] = courses[i].name
            course_info["college_id"] = courses[i].college_id
            course_info["class_id"] = courses[i].class_id
            course_info["hours"] = courses[i].hours
            course_info["course_code"] = courses[i].course_code
            course_info["visit_count"] = courses[i].visit_count
            course_info["teacher"] = courses[i].teacher
            course_info["credit"] = float(courses[i].credit)
            ans.append(course_info)

        print(ans)
        return HttpResponse(json.dumps({'course_type_list': ans}, cls=ComplexEncoder))


#---------------------------------------------------------------
# 资源收藏
# REQUIRES:      变量名|类型|说明
#          resource_id|int|资源id
#              user_id|int|用户id
# MODIFIES: None
# EFFECTS: error|int|0 1:失败
@csrf_exempt
def resource_like(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        
        resource_id = str(data.get('resource_id'))
        user_id = str(data.get('user_id'))
        
        likes = R_Resource_User_Like.objects.filter(resource_id = resource_id, user_id = user_id) #filter相当于SQL中的WHERE，可设置条件过滤结果
        if (len(likes) > 0): #之前喜欢过，报错
            return HttpResponse(json.dumps({'error':1}))
        
        like = R_Resource_User_Like()
        like.user_id = user_id
        like.resource_id = resource_id
        like.save()
        return HttpResponse(json.dumps({'error':0}))

#---------------------------------------------------------------
# 获取资源收藏情况
# REQUIRES:         变量名|类型|说明
#             resource_id|int|资源id
#                 user_id|int|用户id
# MODIFIES: None
# EFFECTS:  like_resource|int|收藏数
#                    like|int|0:未收藏 1:已收藏
@csrf_exempt
def resource_like_count(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        
        resource_id = str(data.get('resource_id'))
        user_id = str(data.get('user_id'))
                    
        likes = R_Resource_User_Like.objects.filter(resource_id = resource_id)
        ans_likes = len(likes)
        likes = R_Resource_User_Like.objects.filter(resource_id = resource_id, user_id = user_id)
        user_like = int(len(likes) > 0)
        return HttpResponse(json.dumps({'like_resource': ans_likes, 'like': user_like}))

#---------------------------------------------------------------
# 资源收藏
# REQUIRES:      变量名|类型|说明
#                course_id|int|课程id
#                user_id|int|用户id
# MODIFIES: None
# EFFECTS: error|int|0 1:失败
@csrf_exempt
def course_like(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        
        course_id = str(data.get('course_id'))
        user_id = str(data.get('user_id'))
    
        likes = R_Course_User_Like.objects.filter(course_id = course_id, user_id = user_id) #filter相当于SQL中的WHERE，可设置条件过滤结果
        if (len(likes) > 0): #之前喜欢过，报错
            return HttpResponse(json.dumps({'error':1}))
        
        like = R_Course_User_Like()
        like.user_id = user_id
        like.course_id = course_id
        like.save()
        return HttpResponse(json.dumps({'error':0}))

#---------------------------------------------------------------
# 课程取消收藏
# REQUIRES:         变量名|类型|说明
#               course_id|int|课程id
#                 user_id|int|用户id
# MODIFIES: None
# EFFECTS:          error|int|0 1:失败
@csrf_exempt
def course_cancel_like(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        
        course_id = str(data.get('course_id'))
        user_id = str(data.get('user_id'))
        
        likes = R_Course_User_Like.objects.filter(course_id = course_id, user_id = user_id) #filter相当于SQL中的WHERE，可设置条件过滤结果
        if (len(likes) == 0):
            return HttpResponse(json.dumps({'error':1}))
        
        like = R_Course_User_Like.objects.get(course_id = course_id, user_id = user_id) #GET获取单个对象
        like.delete()

        return HttpResponse(json.dumps({'error':0}))

#---------------------------------------------------------------
# 获取课程收藏情况
# REQUIRES:         变量名|类型|说明
#               course_id|int|课程id
#                 user_id|int|用户id
# MODIFIES: None
# EFFECTS:     like_count|int|收藏数
#                   liked|int|0:未收藏 1:已收藏
@csrf_exempt
def course_like_count(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
    
        course_id = str(data.get('course_id'))
        user_id = str(data.get('user_id'))

        likes = R_Course_User_Like.objects.filter(course_id = course_id)
        ans_likes = len(likes)
        likes = R_Course_User_Like.objects.filter(course_id = course_id, user_id = user_id)
        user_like = int(len(likes) > 0)
        return HttpResponse(json.dumps({'like_course': ans_likes, 'like': user_like}))

class ActiveUserView(View):
    def get(self, request, active_code):
    # 用code在数据库中过滤处信息
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                # 通过邮箱查找到对应的用户
                user = User.objects.get(email=email)
                # 激活用户
                user.is_active = True
                user.save()
        else:
            return HttpResponse(json.dumps({'error': 104, 'msg':'用户激活失败'})) # activated fail
        return HttpResponse(json.dumps({'error': 0, 'msg':'用户激活成功'}))
    
    
# Upload User Photo Interface
# URL: 
@csrf_exempt
def upload_user_photo(request):
    if(request.method == 'POST'):
        size = request.FILES['user_photo'].size
        user_photo_form = UserPhotoForm({'size': size})
        if(user_photo_form.is_valid()):
            userprofile = UserProfile.objects.get(user_id=request.user.id)
            if(userprofile.user_photo != None):
                link = userprofile.user_photo.url
                t = link.split("/")
                t.remove(t[0])
                file_path = "/".join(t)
                if(os.path.exists(file_path)):
                    os.remove(file_path)
            userprofile.user_photo = request.FILES['user_photo']
            userprofile.save()
            handle_upload_resource(request.FILES['user_photo'], userprofile.user_photo.url)
            return HttpResponse(json.dumps({'error': 0}))
        else:
            return HttpResponse(json.dumps({'error': 1}))

#---------------------------------------------------------------
# 获取最多下载量的资源id列表
# REQUIRES:         变量名|类型|说明
#                   number|int|资源数量
# MODIFIES: None
# EFFECTS:     result|list[dict{}]|返回资源信息列表
#                   资源信息字典：
#                   变量名|类型|说明
#                   :-:|:-:|:-:
#           resource_id|int|资源id
#              username|str|上传者
#        download_count|int|下载量
#                  name|str|资源名称
@csrf_exempt
def most_download_resource_list(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        
        number = str(data.get('number'))
        
        resources = Resource.objects.filter(~Q(download_count = 0)).order_by('-download_count') #取下载量不等于0的filter,然后按下载量降序排序
        ans = []
        cnt = 0
        i = 0
        while (i < len(resources)):
            dict = {}
            if (cnt == number):
                break
            u_id = resources[i].upload_user_id
            u_i = User.objects.filter(id = u_id)
            if (len(u_i) == 0):
                i = i+1
                continue
            u_info = User.objects.get(id = u_id)
            cnt = cnt+1
            i = i+1
            dict["username"] = User.objects.get(id = u_id).username
            dict["download_count"] = resources[i].download_count
            dict["resource_id"] = resources[i].id
            dict["name"] = resources[i].name
            ans.append(dict)
        print(ans)
        return HttpResponse(json.dumps({'result': ans}))

# get most downloaded resource id list of one course
# URL:
@csrf_exempt
def most_download_resource_of_course(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        course_id = int(data.get('course_id'))
        number = str(data.get('number'))
        course_code = Course.objects.get(id=course_id).course_code
        result = Resource.objects.filter(course_code=course_code).order_by('-download_count').values_list('id',flat=True)
        count = 0
        id_list = []
        for item in result:
            id_list.append(item)
            count += 1
            if(count == number):
                break
    return HttpResponse(json.dumps({'id_list': id_list}))


#---------------------------------------------------------------
# 同袍的登录接口，跳转到同袍的登录界面，感觉不需要POST
#@csrf_exempt
def login_tongpao(request):
    url = 'https://tongpao.qinix.com/auths/send_params'
    headers = {'Tongpao-Auth-appid': 'c643da987bdc3ec74efbb0ef7927f7ea', 'Tongpao-Auth-secret': 'GNcP_Pa0Z3nFjjsQa8sd8VCUmUEiIZBa6Rue682LDsMyUIx7iwPplQ'}
    data = { #需要
        #"code":"BElkqvTZCkO924Za-hh8YcWmIDwGCwLXo7n3PrrYXD6lItvlX__b4DbZBgiXaV0ySHZytqlH2swvrbDca4X_MD1v6a2TPw",
        "redirect": "http://127.0.0.1:8000/tongpao/",#https://questionor.cn/problemsets",
        "need_phone_number": 1,
        "need_email": 1,
        "need_personal": 1,
        "need_school_info": 1,
        "need_identification": 1
    }
    r = requests.post(url, headers = headers,  data=json.dumps(data))

    print(r.text)
    json_code = json.loads(r.text)
    print(json_code)
    token = str(json_code['token'])
    print(token) #返回这个token给前端跳？
    return HttpResponseRedirect("https://tongpao.qinix.com/auths/login?token="+token) #HttpResponse(json.dumps({'error': 0}))

#---------------------------------------------------------------
# 获取同袍用户信息的接口，目前是GET，可以post回信息
# 可以获取到的信息例如如下：
# "tongpao_username":"14011100","phone_number":["17801016282"],"email":"291045048@qq.com","real_name":"赵奕","birthday":"1996-10-31","gender":"男","grade":2015,"student_id":"14011100","college":"计算机学院","major":"计算机科学与技术","class_name":"150617","identification":"320982199610312298"}
def tongpao(request):
    print("TONGPAO!!!")
    code = str(request.GET["code"])
    print("code = ",code)
    url = 'https://tongpao.qinix.com/auths/get_data'
    headers = {'Tongpao-Auth-appid': 'c643da987bdc3ec74efbb0ef7927f7ea', 'Tongpao-Auth-secret': 'GNcP_Pa0Z3nFjjsQa8sd8VCUmUEiIZBa6Rue682LDsMyUIx7iwPplQ'}
    data = {
        "code":code,
    }
    print(data)
    r = requests.post(url, headers = headers, data=data)
    print(r.text)
    json_text = json.loads(r.text)
    profile = json_text["data"]
    print(profile)
    print("$$$", type(profile))

    student_id = profile["student_id"]

    students = User.objects.filter(username = student_id)
    if (len(students) > 0): #之前已经登录过
        print(student_id, " Has Registered!")
        return HttpResponse(json.dumps({'error':0}))

    tongpao_username = profile["tongpao_username"]
    phone_number = profile["phone_number"]
    print(phone_number)
    phone_number = int(phone_number[0])
    print(phone_number)
    email = profile["email"]
    real_name = profile["real_name"]
    birthday = profile["birthday"]
    gender = profile["gender"]
    grade = profile["grade"]
    college = profile["college"]
    major = profile["major"]
    class_name = profile["class_name"]
    identification = profile["identification"]

    user = User()
    user.username = student_id
    print("!!!!username=",student_id)
    user.email = email
    user.is_active = False
    user.first_name = "TongPao"
    user.save()

    user_profile = UserProfile()
    gender_dict = {"男":0, "女":1}
    user_profile.user_id = user.id
    user_profile.gender = gender_dict[gender]
    print("gender=",gender,"value:",gender_dict[gender])
    user_profile.nickname = ""
    user_profile.info = ""
    user_profile.save()

    tp_u = Tongpao_Userprofile()
    tp_u.student_id = student_id
    tp_u.tongpao_username = tongpao_username
    tp_u.phone_number = phone_number
    tp_u.email = email
    tp_u.real_name = real_name
    tp_u.gender = gender
    tp_u.birthday = birthday
    tp_u.grade = grade
    tp_u.college = college
    tp_u.major = major
    tp_u.class_name = class_name
    tp_u.identification = identification
    tp_u.save()

    return HttpResponseRedirect("/")
    
#return HttpResponseRedirect("/")#http://127.0.0.1:8000/")


# 忘记密码-提交申请-发送邮件
# URL:/user/forget/password/send/
@csrf_exempt
def user_forget_password_send(request):
    if(request.method == 'POST'):
        email = str(request.POST.get('email'))
        send_reset_pswd_email(email, 'reset pswd')

# 忘记密码-重置密码
# URL:/user/forget/password/set/
@csrf_exempt
def user_forget_password_set(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        email = str(data.get('email'))
        code = str(data.get('code'))
        new_pw1 = str(data.get('new_pw1'))
        new_pw2 = str(data.get('new_pw2'))
        if(new_pw1 != new_pw2):
            return HttpResponse(json.dumps({'error': 1}))
        all_records = EmailVerifyRecord.objects.filter(email=email, code=code, send_type='reset pswd')
        if(len(all_records) < 1):
            return HttpResponse(json.dumps({'error': 1}))
        user = User.objects.get(email=email)
        user.set_password(new_pw1)
        user.save()
        return HttpResponse(json.dumps({'error': 0}))

# 修改密码
# URL: /user/modify/password/
@csrf_exempt
def user_modify_password(request):
    if(request.method == 'POST'):
        if(not request.user.is_authenticated()):
            return HttpResponse(json.dumps({'error': 1}))
        data = json.dumps(request.POST)
        data = json.loads(data)
        user_id = request.user.id
        old_pw = str(data.get('old_pw'))
        new_pw1 = str(data.get('new_pw1'))
        new_pw2 = str(data.get('new_pw2'))
        if(new_pw1 != new_pw2):
            return HttpResponse(json.dumps({'error': 1}))
        user = User.objects.get(id=user_id)
        cb = CustomBackend()
        result = cb.authenticate(username=user.username, password=old_pw)
        if(result is not None and result.is_active):
            user.set_password(new_pw1)
            user.save()
            auth.logout(request)
            return HttpResponse(json.dumps({'error': 0}))
        return HttpResponse(json.dumps({'error': 1}))

