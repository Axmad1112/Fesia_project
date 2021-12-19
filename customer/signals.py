from customer.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from bank.models import CoinBase
from customer.models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        bank = CoinBase.objects.first()
        bank.coin-=1000
        bank.save()
        Profile.objects.create(email=instance.email,  user=instance)
        

# @receiver(post_save, sender=Profile)
# def create_profile_profile(sender, instance, created, **kwargs):
#     if created:
#         Wallet.objects.create(profile=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

@receiver(post_delete, sender=Profile)
def delete_user_profile(sender, instance, **kwargs):
    if instance.user:
        user = User.objects.get(username=instance.user.username)
        user.delete()
        
    print(instance)