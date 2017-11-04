from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
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

def home(request):
    return render(request, 'index.html')

def course(request):
    return render(request, 'course.html')

def contact(request):
    return render(request, 'contact.html')

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
                return HttpResponse(json.dumps({'error': 201}))

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
        data = json.loads(request.POST)
        #data = json.loads(request.body.decode())
        college_id = int(data.get('college_id'))
        course_id_list = interface.college_course_list(6)
        print(course_id_list)
        return HttpResponse(json.dumps({'course_id_list': course_id_list}))

# the Interface of search course list by class id
# REQUIRES: the ajax data should be json data {'class_id': class_id}
# MODIFIES: None
# EFFECTS: return json data {'course_id_list': course_id_list}, course_id_list is a list
# URL: /course/classification_course/
@csrf_exempt
def course_by_class(request):
    if(request.method == "POST"):
        data = json.loads(request.POST)
        #data = json.loads(request.body.decode())
        class_id = int(data.get('class_id'))
        course_id_list = interface.classification_course_list(class_id)
        return HttpResponse(json.dumps({'course_id_list': course_id_list}))

# Course Information Interface
# REQUIRES: the ajax data should be json data {'course_id': class_id}
# MODIFIES: None
# EFFECTS: return json data {'course_info': course_info}, course_info is a dict
# URL: /course/course_info/
@csrf_exempt
def course_information(request):
    if(request.method == "POST"):
        data = json.loads(request.POST)
        #data = json.loads(request.body.decode())
        course_id = int(data.get('course_id','0'))
        course_info = interface.course_information(course_id)
        return HttpResponse(json.dumps({'course_info': course_info}))

# User Information Interface
# REQUIRES: the ajax data should be json data {'username': username}
# MODIFIES: NONE
# EFFECTS: return json data {'user_info': user_info}, user_info is a dict
@csrf_exempt
def user_information(request):
    if(request.method == "POST"):
        data = json.loads(request.POST)
        #data = json.loads(request.body.decode())
        username = str(data.get('username'))
        user_info = interface.user_information(username)
        return HttpResponse(json.dumps({'user_info': user_info}))

# Resource Information Interface
# REQUIRES: the ajax data should be json data {'resource_id': resource_id}
# MODIFIES: None
# EFFECTS: return json data {'resource_info': resource_info}, resource_info is a dict
# URL:
@csrf_exempt
def resource_information(request):
    if(request.method == "POST"):
        data = json.loads(request.POST)
        #data = json.loads(request.body.decode())
        resource_id = int(data.get('resource_id'))
        resource_info = interface.resource_information(resource_id)
        return HttpResponse(json.dumps({'resource_info': resource_info}))

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
        return HttpResponse(json.dumps({'contrib_list': contrib_list})) 

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
        return HttpResponse(json.dumps({'is_login': is_login}))

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
                return HttpResponse(json.dumps({'error': 0}))
            else:
                return HttpResponse(json.dumps({'error': 101})) # username not exists
        else:
            return HttpResponse(json.dumps({'error': 102})) # password error

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