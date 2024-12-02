from django.contrib import admin

from django.contrib import admin
from .models import Course,Student,Comment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','updated_at')
    search_fields = ('title','description')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'course', 'enrolled_at')
    search_fields = ('name', 'email')
    list_filter = ('enrolled_at', 'course')
    ordering = ('-enrolled_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'comment', 'created_at')
    search_fields = ('comment',)
    list_filter = ('created_at', 'course')
    ordering = ('-created_at',)

