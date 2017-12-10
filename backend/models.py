# 方科栋的代码我暂时先注释了 张安澜 2017.11.1
# 方科栋的代码我先删除了 方科栋2017.12.08

from django.db import models
from django.contrib.auth.models import User
import datetime


# Course Model
class Course(models.Model):
    name = models.CharField(max_length=30)
    college_id = models.PositiveIntegerField()
    class_id = models.PositiveSmallIntegerField()
    hours = models.SmallIntegerField()
    credit = models.DecimalField(max_digits=2, decimal_places=1)
    course_code = models.CharField(max_length=10)
    visit_count = models.IntegerField()
    teacher = models.CharField(max_length=100, null=True)
    elective = models.SmallIntegerField(default=0)

    def __str__(self):
        return str(self.id)

# Resource Model
class Resource(models.Model):
    size = models.IntegerField(blank=False)
    link = models.FileField(blank=True, upload_to='uploads/%Y/%m')
    name = models.CharField(blank=False,max_length=300)
    intro = models.TextField()
    upload_user_id = models.PositiveIntegerField(blank=False)
    #course_id = models.PositiveIntegerField(blank=False)
    upload_time = models.DateTimeField(auto_now_add=True)
    only_url = models.BooleanField(blank=False)           # if only_url is True, link = None && url = uploaded url; else url = None && link = uploaded file.url
    url = models.CharField(blank=True, max_length=1000)
    course_code = models.CharField(blank=True, max_length=10)
    download_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

# Teacher Model
class Teacher(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)

# College Model
class College(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id)

# Course_Class Model
class Course_Class(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)

# R_Course_User_Contribution Model
class R_Course_User_Contribution(models.Model):
    score = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    course_id = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)

# R_Course_User_Like Model
class R_Course_User_Like(models.Model):
    user_id = models.PositiveIntegerField()
    course_id = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)

# UserProfile Model: extend info of User
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, verbose_name=('User'))
    gender = models.CharField(max_length=1)
    nickname = models.CharField(max_length=20)
    intro = models.TextField()
    college_id = models.PositiveIntegerField(blank=True, default=None)
    user_photo = models.ImageField(upload_to='user_photo', null=True, blank=True)

    def __str__(self):
        return str(self.user.id)

class Resource_Evaluation(models.Model):
    user_id = models.IntegerField()
    resource_id = models.IntegerField()
    grade = models.SmallIntegerField()

    def __str__(self):
        return str(self.id)

# R_Resource_User_Like Model
class R_Resource_User_Like(models.Model):
    user_id = models.PositiveIntegerField()
    resource_id = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)

# Report Model
class Report(models.Model):
    report_time = models.DateTimeField(auto_now_add=True)
    report_user_id = models.PositiveIntegerField(blank=True)
    be_reported_resource_id = models.PositiveIntegerField(blank=False)
    already_handle = models.BooleanField(blank=False, default=False)    # this field represents that if the administrator has handled the report, default=False, after handling, alter this field to True

    def __str__(self):
        return str(self.id)

class IpVisitInfo(models.Model):
    ip = models.CharField(max_length=20)
    early_date = models.CharField(max_length=20)
    latest_date = models.CharField(max_length=20)
    visit_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

class Post(models.Model):
    course_id = models.IntegerField(blank=False)
    category = models.IntegerField(blank=False)
    title = models.CharField(max_length=30, blank=False)
    main_follow_id = models.IntegerField()
    update_time = models.DateTimeField(auto_now=True)
    follow_count = models.IntegerField(default=0)
    click_count = models.IntegerField(default=0)
    intro = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

class Follow(models.Model):
    post_id = models.IntegerField(blank=False)
    user_id = models.IntegerField(blank=False)
    content = models.TextField(blank=False)
    post_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)
    editor = models.IntegerField(blank=False)
    is_main = models.BooleanField(blank=False)
    pos_eva_count = models.IntegerField(default=0)
    neg_eva_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.id)

class Follow_Evaluation(models.Model):
    user_id = models.IntegerField(blank=False)
    follow_id = models.IntegerField(blank=False)
    grade = models.SmallIntegerField(blank=False)

    def __str__(self):
        return str(self.id)

class Follow_Comment(models.Model):
    user_id = models.IntegerField(blank=False)
    follow_id = models.IntegerField(blank=False)
    to_comment_id = models.IntegerField(null=True)
    content = models.TextField(blank=False)
    post_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class EmailVerifyRecord(models.Model):
    # 验证码
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    # 包含注册验证和找回验证
    send_type = models.CharField(verbose_name=u"验证码类型", max_length=10, choices=(("register",u"注册"), ("forget",u"找回密码")))
    send_time = models.DateTimeField(verbose_name=u"发送时间", auto_now_add=True)
    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)

