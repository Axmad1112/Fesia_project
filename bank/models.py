from django.db import models
from rest_framework.validators import ValidationError
from api.models import Course, Task
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

class SpentCoin(models.Model):
    from_profile = models.ForeignKey("customer.Profile", on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey("api.Course",on_delete=models.SET_NULL, null=True)
    bank = models.ForeignKey(CoinBase,on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    create_at = models.DateTimeField(auto_now=True)
    
    def __str__(self): 
        return f"{self.from_profile} profil egasi '{self.course}' kurs sotib oldi| coin: {self.amount} va bazada {self.bank}"

class EarnCoin(models.Model):
    to_profile = models.ForeignKey("customer.Profile", on_delete=models.SET_NULL, null=True)
    task = models.ForeignKey("api.Task",on_delete=models.SET_NULL,null=True)
    bank = models.ForeignKey(CoinBase,on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    create_at = models.DateTimeField(auto_now=True)
    
    def __str__(self): 
        return f"{self.to_profile}-profil egasi {self.task} topshiriqdan| {self.amount} coinga erishdi "