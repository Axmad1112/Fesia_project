from django.db import models
from rest_framework.validators import ValidationError
# from api.models import Course
# from customer.models import Profile
# Create your models here.

class CoinBase(models.Model):
    coin = models.PositiveBigIntegerField()
    
    def __str__(self):
        return f"{self.coin} coin"
    
    def save(self, *args, **kwargs):
        if not self.pk and CoinBase.objects.exists():
        # if you'll not check for self.pk 
        # then error will also raised in update of exists model
            raise ValidationError({'error':'There is can be only one JuicerBaseSettings instance'})
        return super(CoinBase, self).save(*args, **kwargs)

# class Report(models.Model):
#     from_profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="from_profile")
#     course = models.ForeignKey(Course,on_delete=models.SET_NULL, null=True, related_name="course")
#     bank = models.ForeignKey(CoinBase,on_delete=models.SET_NULL, null=True, related_name="bank")
#     amount = models.IntegerField()
#     create_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self): 
#         return f"{self.from_profile}->{self.course} | {self.amount}"