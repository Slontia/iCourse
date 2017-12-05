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
import notifications.urls

urlpatterns = [
    # interface
    url(r'^sign/register/$', backend_views.userRegister, name='userRegister'),    # for user register
    url(r'^sign/get_user/$', backend_views.get_user, name='get_user'),    # for check user status
    url(r'^sign/login/$', backend_views.userLogin, name='userLogin'),    # for user login
    url(r'^sign/logout/$', backend_views.userLogout, name='userLogout'),    # for user logout
    url(r'^sign/iprecord/$',backend_views.ip_record),
    url(r'^sign/logged_in/$', backend_views.isLoggedIn, name='isLoggedIn'),
    url(r'^course/college_course/$', backend_views.course_by_college, name='course_by_college'),    # for searching course list by college_id
    url(r'^course/classification_course/$', backend_views.course_by_class, name='course_by_class'),    # for searching course list by class_id
    url(r'^course/course_info/$', backend_views.course_information, name='course_information'),    # for course information
    url(r'^course/visit_count/$', backend_views.refresh_visit_course_count),
    url(r'^course/searching/$', backend_views.course_query, name='course_searching'),
    url(r'^download/(\d+)/$', backend_views.download, name='download'),
    url(r'^resource/information/$', backend_views.resource_information, name='resource_information'),
    url(r'^resource/id/list/$', backend_views.resource_id_list, name='resource_id_list'),
    url(r'^resource/latest/$',backend_views.latest_resource_info,name='latest_resource_info'),
    url(r'^resourceUpload/$',backend_views.resourceUpload,name='resourceUpload'),
    url(r'^resource/download_count/$',backend_views.refresh_download_resource_count),
    url(r'^user/information/$', backend_views.user_information, name='user_information'),

    url(r'^resource/evaluate/$', backend_views.resource_evaluate, name='resource_evaluate'),
    url(r'^resource/evaluation/grade/count/$', backend_views.resource_evaluation_grade_count, name='resource_evaluation_grade_count'),
    url(r'^resource/id/list/$', backend_views.resource_id_list, name='resource_id_list'),
               
    # page
    url(r'^$', TemplateView.as_view(template_name='index.html')), # NEW
    url(r'^index/$', backend_views.home, name='index'),
    url(r'^course/$', backend_views.course, name='course'),
    url(r'^resource/$', backend_views.course, name='course'),
    url(r'^contact/$', backend_views.contact, name='contact'), 
    url(r'^admin/', admin.site.urls),
    url(r'^user/home/.*/$', backend_views.home),
    url(r'^course/page/.*/$', backend_views.home),
    url(r'^course/page/.*/resource/$', backend_views.home),

    # post follow follow_comment follow_evaluation
    url(r'^post/posting/publish/$', backend_views.posting_publish, name='posting_publish'),
    url(r'^post/follow/publish/$', backend_views.follow_publish, name='follow_publish'),
    url(r'^post/comment/publish/$', backend_views.comment_publish, name='comment_publish'),
    url(r'^post/follow/evaluate/$', backend_views.follow_evaluate, name='follow_evaluate'),
    url(r'^post/id/list/$', backend_views.post_id_list, name='post_id_list'),
    url(r'^post/information/list/$', backend_views.post_infor_list, name='post_infor_list'),
    url(r'^follow/id/list/$', backend_views.follow_id_list, name='follow_id_list'),
    url(r'^follow/info/list/$', backend_views.follow_info_list, name='follow_info_list'),
    url(r'^comment/id/list/$', backend_views.comment_id_list,name='comment_id_list'),
    url(r'^comment/info/list/$', backend_views.comment_info_list,name='comment_info_list'),

    # notifications
    url(r'^notifications/', include(notifications.urls, namespace='notifications')),
]
