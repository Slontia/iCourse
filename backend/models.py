from bokeh.themes import default

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

