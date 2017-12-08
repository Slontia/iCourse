#from bokeh.themes import default 方科栋的代码我暂时先注释了 张安澜 2017.11.1
'''
NAME_LENGTH = 30
UPLOAD_USERIF_LENGTH = 10
COURSEID_LENGTH=10
LINK_LENGTH = 100

from django.db import models

class Resource( models.Model ):
    name = models.CharField(max_length=NAME_LENGTH)
    introduce = models.TextField(null=True)
    size = models.IntegerField()
    uploadTime = models.DateTimeField()
    link = models.CharField(max_length=LINK_LENGTH, null=True)
    upload_user_id=models.IntegerField(default=-1)
    course_id=models.IntegerField(default=-1)
    
    def __str__(self):
        return self.name

USERNAME_LENGTH=20
PASSWORD_LENGTH=20
EMAIL_USERNAME_LENGTH=20
NICKNAME_LENGTH=20

class User( models.Model ):
    username = models.CharField(max_length=USERNAME_LENGTH)
    password=models.CharField(max_length=PASSWORD_LENGTH, null=True)
    gender=models.IntegerField(null=True)
    email_username=models.CharField(max_length=EMAIL_USERNAME_LENGTH, null=True)
    nickname=models.CharField(max_length=NICKNAME_LENGTH, null=True)
    intro = models.TextField(null=True)
    
    def __str__(self):
        return self.username
'''

from django.db import models
from django.contrib.auth.models import User

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
