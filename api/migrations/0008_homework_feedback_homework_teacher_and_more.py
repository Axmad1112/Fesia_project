# Generated by Django 4.0 on 2021-12-19 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_task_file_remove_task_github_link_homework'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='feedback',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homework',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.teacher'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='homework'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='github_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
