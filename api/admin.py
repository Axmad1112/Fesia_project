from django.contrib import admin
from .models import *
from customer.models import Profile
# Register your models here.
admin.site.register(Teacher)
admin.site.register(Categories)
admin.site.register(Course)
admin.site.register(Task)
admin.site.register(Video)
admin.site.register(Homework)
admin.site.register(Profile)