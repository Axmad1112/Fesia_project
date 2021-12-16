from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
from django.conf import settings
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(null=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']
        
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    @property
    def token(self):
        try:
            token = Token.objects.get(user=self)
        except Token.DoesNotExist:
            token = Token.objects.create(user=self)
        return token.key


class Profile(models.Model):
    ENLISH_LEVEL=[
        ("Beginner","Beginner"),
        ("Intermedite","Intermedite"),
        ("Advanced","Advanced")
    ]
    image = models.ImageField(upload_to="profile_image")
    english_degree = models.CharField(choices=ENLISH_LEVEL,max_length=200)
    user = models.OneToOneField("customer.User",on_delete=models.CASCADE)
    course = models.ManyToManyField("api.Course")
    coin = models.IntegerField(default=1000)
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.user.email}"
 

