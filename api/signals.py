from api.models import Homework, Lesson
from customer.models import Profile
from bank.models import CoinBase, EarnCoin
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Homework)
def update_lesson_banned(sender, instance, created, **kwargs):
    print(instance.task.lesson.course,"lesson pesson kemadimi")
    print(instance.correct,"nima keldi")

    if instance.task.lesson.course.banned is False:
        bank = CoinBase.objects.first()
        if instance.correct is True:
            bank.coin-=instance.task.bonus_coin
            profile_coin = Profile.objects.get(user=instance.user)
            profile_coin.coin+=instance.task.bonus_coin
            earn_coin = EarnCoin(to_profile=profile_coin,task=instance.task,amount=instance.task.bonus_coin,bank=bank)
            earn_coin.save()
            print(earn_coin)
            bank.save()
            profile_coin.save()
            queryset = Lesson.objects.filter(course=instance.task.lesson.course)
            for obj in queryset:
                # if instance.task.lesson == obj:
                if obj.banned is True:
                    obj.banned=False
                    obj.save()
                    break