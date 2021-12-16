from django.db import models
from rest_framework.validators import ValidationError
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