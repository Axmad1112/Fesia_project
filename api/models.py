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
    user = models.OneToOneField("customer.User",on_delete=models.SET_NULL,null=True)

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
    profile = models.ManyToManyField("customer.Profile",  blank=True)
    # banned = models.BooleanField(default=False)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.teacher_id} ning {self.name} kursi"


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey("api.Course", on_delete=models.CASCADE,related_name="lesson_course", null=True)
    profile = models.ManyToManyField("customer.Profile",  blank=True)
    # banned = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.course} kursining {self.name} lessoni"
    
class Video(models.Model):
    name = models.CharField(max_length=255)
    lesson = models.ForeignKey("api.Lesson", on_delete=models.CASCADE,related_name="video_lesson", null=True)
    video_file = models.FileField(null=True)
    
    
    def __str__(self):
        return f"{self.lesson} videosi nomi {self.name}"

class Task(models.Model):
    user = models.ForeignKey("customer.User",on_delete=models.CASCADE,related_name="user", null=True)
    lesson = models.ForeignKey("api.Lesson", on_delete=models.CASCADE, related_name="task_lesson",null=True)
    text = models.TextField()
    create_at = models.DateTimeField(auto_now=True)
    bonus_coin = models.IntegerField(null=True)
    

    def __str__(self):
        return f"{self.lesson} lessoni topshirig'i {self.text}"

class Homework(models.Model):
    user = models.ForeignKey("customer.User",on_delete=models.CASCADE,related_name="homework_user")
    task = models.ForeignKey("api.Task",on_delete=models.CASCADE,related_name="homework_task")
    file = models.FileField(upload_to="homework", null=True, blank=True)
    github_link = models.URLField(null=True,blank=True)
    create_at = models.DateTimeField(auto_now=True)
    teacher = models.ForeignKey("api.Teacher",on_delete=models.SET_NULL, null=True, blank=True)
    feedback = models.TextField(blank=True, null=True)
    correct = models.BooleanField(default=False, null=True)



    def __str__(self):
        return f"{self.task} ni-> {self.user} bajardi"








