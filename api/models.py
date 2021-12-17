from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.fields import CharField
# from customer.models import User

class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    age = models.IntegerField()
    description = models.TextField()
    img = models.ImageField(upload_to="teacher_image")
    messanger = models.URLField()

    def __str__(self):
        return self.full_name

class Categories(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type


class Course(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="courses_image", height_field=None, width_field=None, max_length=None)
    category_id = models.ForeignKey("api.Categories", on_delete=models.CASCADE,related_name="courses")
    teacher_id = models.ForeignKey("api.Teacher", on_delete=models.SET_NULL, related_name="courses",null=True)
    cost = models.IntegerField()
    banned = models.BooleanField(default=False)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey("api.Course", on_delete=models.CASCADE,related_name="course", null=True)
    banned = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Video(models.Model):
    name = models.CharField(max_length=255)
    lesson = models.ForeignKey("api.Lesson", on_delete=models.CASCADE,related_name="video_lesson", null=True)
    video_file = models.FileField(null=True)
    
    
    def __str__(self):
        return self.name

class Task(models.Model):
    user = models.ForeignKey("customer.User",on_delete=models.CASCADE,related_name="user", null=True)
    lesson = models.ForeignKey("api.Lesson", on_delete=models.CASCADE, related_name="task_lesson",null=True)
    text = models.TextField()
    file = models.FileField(upload_to="homework",null=True, blank=True)
    github_link = models.URLField(null=True,blank=True)
    create_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.text

# class Homework(models.Model):
#     user = models.ForeignKey("customer.User",on_delete=models.CASCADE,related_name="user")
#     task = models.ForeignKey("api.Task",on_delete=models.CASCADE,related_name="task")
#     file = models.FileField(upload_to="homework")
#     github_link = models.URLField(null=True)
    

#     def __str__(self):
#         return f"{self.task}"








