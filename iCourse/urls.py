"""iCourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView
#from iCourse import testdb
from django.conf.urls import include, url
from backend import views as backend_views


urlpatterns = [
    url(r'^index/$', backend_views.home, name='index'),
    url(r'^course/$', backend_views.course, name='course'),
    url(r'^contact/$', backend_views.contact, name='contact'), 
    url(r'^sign/register/$', backend_views.userRegister, name='userRegister'),    # for user register
    url(r'^course/college_course/$', backend_views.course_by_college, name='course_by_college'),    # for searching course list by college_id
    url(r'^course/classification_course/$', backend_views.course_by_class, name='course_by_class'),    # for searching course list by class_id
    url(r'^course/course_info/$', backend_views.course_information, name='course_information'),    # for course information
    url(r'^sign/get_user/$', backend_views.get_user, name='get_user'),    # for check user status
    url(r'^sign/login/$', backend_views.userLogin, name='userLogin'),    # for user login
    url(r'^sign/logout/$', backend_views.userLogout, name='userLogout'),    # for user logout

    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html')), # NEW
    # url(r'^course/$', backend_views.course, name='course'),
    # url(r'^contact/$', backend_views.contact, name='contact'),
    #url(r'^api/', include('backend.urls', namespace='api')) # NEW
    #url( r'^testdb$', testdb.test ),

    url(r'^sign/logged_in/$', backend_views.isLoggedIn, name='isLoggedIn'),
    #url(r'^/user/[username]/home/$')
    url(r'^user/information/$', backend_views.user_information, name='user_information'),
    url(r'^course/searching/$', backend_views.course_query, name='course_searching'),
    url(r'^user/home/.*/$', backend_views.home),
    url(r'^course/page/.*/$', backend_views.home)
]
