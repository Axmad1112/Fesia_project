from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    ENLISH_LEVEL=[
        ("Beginner","Beginner"),
        ("Intermedite","Intermedite"),
        ("Advanced","Advanced")
    ]
    image = models.ImageField(upload_to="profile_image")
    english_degree = models.CharField(choices=ENLISH_LEVEL,max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ManyToManyField("api.Course")
    coin = models.IntegerField(default=1000)
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return self.user.username
 

