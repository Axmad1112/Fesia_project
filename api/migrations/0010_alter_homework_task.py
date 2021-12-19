# Generated by Django 4.0 on 2021-12-19 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_teacher_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homework_task', to='api.task'),
        ),
    ]
