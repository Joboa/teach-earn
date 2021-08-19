from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import User, Student, Teacher

admin.site.register(User)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'comment']

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number']


admin.site.register(Student, StudentAdmin)

admin.site.register(Teacher, TeacherAdmin)
