# Generated by Django 3.0.2 on 2020-08-17 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0006_auto_20200816_2314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadvideomodel',
            name='user_name',
        ),
    ]
