from api.models import Homework, Lesson
from customer.models import Profile
from bank.models import CoinBase, EarnCoin
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import validators

@receiver(post_save, sender=Homework)
def update_lesson_banned(sender, instance, created, **kwargs):
    
    profile_coin = Profile.objects.get(user=instance.user)
    if profile_coin in instance.task.lesson.course.profile.all():
        bank = CoinBase.objects.first()
        if instance.correct is True:
            bank.coin-=instance.task.bonus_coin
            profile_coin.coin+=instance.task.bonus_coin
            earn_coin = EarnCoin(to_profile=profile_coin,task=instance.task,amount=instance.task.bonus_coin,bank=bank)
            earn_coin.save()
            print(earn_coin)
            bank.save()
            profile_coin.save()
            queryset = Lesson.objects.filter(course=instance.task.lesson.course)
            for i in range(len(queryset)):
                print(queryset[i])
                if queryset[i]==instance.task.lesson:
                    if queryset[i+1]:
                        queryset[i+1].profile.add(profile_coin)
                
