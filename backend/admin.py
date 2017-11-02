from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

class ProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False

class UserProfileAdmin(UserAdmin):
    inlines = [ProfileInline, ]

admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
