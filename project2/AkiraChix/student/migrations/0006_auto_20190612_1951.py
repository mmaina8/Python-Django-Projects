# Generated by Django 2.2.1 on 2019-06-12 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20190611_1458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='image',
            new_name='profile_picture',
        ),
    ]
