from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Course, Resource, Report

class ProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False

class UserProfileAdmin(UserAdmin):
    inlines = [ProfileInline, ]

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'college_id', 'class_id')

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'upload_time', 'download_count')

class ReportAdmin(admin.ModelAdmin):
    list_display = ('be_reported_resource_id', 'report_user_id', 'report_time', 'already_handle')

admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Report, ReportAdmin)

