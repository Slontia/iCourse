'''
ID_LENGTH = 20
NAME_LENGTH = 20
UPLOAD_USERNAME_LENGTH = 20
UPLOAD_TIME_LENGTH = 40
LINK_LENGTH = 100
'''
from django.db import models

class Resource( models.Model ):
    resourceId = models.TextField( default = "" )
    name = models.TextField( default = "" )
    introduce = models.TextField( default = "" )
    size = models.TextField( default = "" )
    uploadTime = models.TextField( default = "" )
    link = models.TextField( default = "" )
    
    def __str__(self):
        return self.name

