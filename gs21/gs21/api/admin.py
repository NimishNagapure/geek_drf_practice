from django.contrib import admin

from .models import ApiStudent

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']  