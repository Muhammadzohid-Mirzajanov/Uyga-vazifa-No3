from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(verbose_name=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,verbose_name=None)

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    comment = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name


