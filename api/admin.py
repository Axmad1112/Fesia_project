from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Teacher)
admin.site.register(Categories)
admin.site.register(Course)
admin.site.register(Task)
admin.site.register(Video)
admin.site.register(Homework)