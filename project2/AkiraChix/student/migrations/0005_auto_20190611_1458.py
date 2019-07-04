# Generated by Django 2.2.1 on 2019-06-11 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20190611_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='student_image'),
        ),
    ]
