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
    url(r'^course/resource/download/most/info/$',backend_views.most_download_resource_of_course_info),
    
    url(r'^user/information/$', backend_views.user_information, name='user_information'),
    url(r'^course/contri/$', backend_views.course_contri_list, name='course_contri_list'),
    # test by ohazyi(GET)
    url(r'^resource/evaluate/$', backend_views.resource_evaluate, name='resource_evaluate'),
    url(r'^resource/evaluation/grade/count/$', backend_views.resource_evaluation_grade_count, name='resource_evaluation_grade_count'),
    url(r'^resource/class/id/list/$', backend_views.resource_class_id_list, name='resource_class_id_list'),
    url(r'^course/type/list/$', backend_views.course_type_list, name='course_type_list'),
    url(r'^resource/like/add/$', backend_views.resource_like, name='resource_like'),
    url(r'^resource/like/count/$', backend_views.resource_like_count, name='resource_like_count'),
    url(r'^course/like/add/$', backend_views.course_like, name='course_like'),
    url(r'^course/like/cancel/$', backend_views.course_cancel_like, name='course_cancel_like'),
    url(r'^course/like/count/$', backend_views.course_like_count, name='course_like_count'),
    url(r'^resource/download/most/$', backend_views.most_download_resource_list, name='most_download_resource_list'),
    url(r'^login_tongpao/$', backend_views.login_tongpao, name='login_tongpao'),
    url(r'^tongpao/$', backend_views.tongpao, name='tongpao'),
    url(r'^resource/upload/latest/$', backend_views.latest_upload_resource_list, name='latest_upload_resource_list'),
               
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
    url(r'^post/click_count/$', backend_views.refresh_click_post_count),
    url(r'^follow/id/list/$', backend_views.follow_id_list, name='follow_id_list'),
    url(r'^follow/info/list/$', backend_views.follow_info_list, name='follow_info_list'),
    url(r'^comment/id/list/$', backend_views.comment_id_list,name='comment_id_list'),
    url(r'^comment/info/list/$', backend_views.comment_info_list,name='comment_info_list'),
    url(r'^user/modify/info/$',backend_views.user_modify_info,name='user_modify_info'),
    # notifications
    url(r'^notifications/', include(notifications.urls, namespace='notifications')),

    # home
    url(r'^post/hot/idlist/$', backend_views.post_id_list_by_click_count),
    url(r'^post/latest/idlist/$', backend_views.post_id_list_by_update_time),
    # url(r'^resource/upload/latest/', backend_views.most_upload_latest_list),
    url(r'^resource/download/most/$', backend_views.most_download_resource_list),


    #email verify
    url(r'^active/(?P<active_code>.*)/$', backend_views.ActiveUserView.as_view(), name="user_active"),  # 提取出active后的所有字符赋给active_code
]
