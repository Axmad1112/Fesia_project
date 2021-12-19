from api.models import Homework, Lesson
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

@receiver(post_save, sender=Homework)
def update_lesson_banned(sender, instance, created, **kwargs):
    print(instance.task.lesson.course,"lesson pesson kemadimi")
    print(instance.correct,"nima keldi")

    if instance.task.lesson.course.banned is False:
        if instance.correct is True:
            queryset = Lesson.objects.filter(course=instance.task.lesson.course)
            for obj in queryset:
                # if instance.task.lesson == obj:
                if obj.banned is True:
                    obj.banned=False
                    obj.save()
                    break