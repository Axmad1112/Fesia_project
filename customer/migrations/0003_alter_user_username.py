# Generated by Django 4.0 on 2021-12-16 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_profile_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
