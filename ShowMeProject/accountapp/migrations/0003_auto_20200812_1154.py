# Generated by Django 3.0.2 on 2020-08-12 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0002_auto_20200812_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadvideomodel',
            name='video_tags',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]