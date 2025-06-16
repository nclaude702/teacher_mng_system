from django.contrib import admin
from .models import Teacher, Users

class TeacherAdmin(admin.ModelAdmin):
    list_display = ("tname", "subject", "qualification", "contact", "leave_record")

admin.site.register(Teacher, TeacherAdmin)

class UsersAdmin(admin.ModelAdmin):
    list_display = ("names", "username", "password")

admin.site.register(Users, UsersAdmin)
