# Generated by Django 3.1 on 2020-10-04 15:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accountapp', '0008_usrregmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadvideomodel',
            name='video_dislikes',
            field=models.ManyToManyField(related_name='video_dislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='uploadvideomodel',
            name='video_likes',
        ),
        migrations.AddField(
            model_name='uploadvideomodel',
            name='video_likes',
            field=models.ManyToManyField(related_name='video_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
