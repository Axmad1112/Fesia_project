# Generated by Django 4.0 on 2021-12-15 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='course',
            field=models.ManyToManyField(to='api.Course'),
        ),
    ]