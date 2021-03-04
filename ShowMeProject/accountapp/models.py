from django.db import models
from django.contrib.auth.models import User

class UploadVideoModel(models.Model):
    root_user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_caption = models.CharField(max_length=500)
    video_file = models.FileField(upload_to='uploaded_videos', null=True, blank=True)
    video_url = models.CharField(max_length=1000, null=True, blank=True)
    video_tags = models.TextField(max_length=2000, null=True, blank=True)
    video_likes = models.ManyToManyField(User, related_name='video_like')
    video_dislikes = models.ManyToManyField(User, related_name='video_dislike')

    def __str__(self):
        return self.video_caption
class UsrRegModel(models.Model):
    root_user = models.OneToOneField(User, on_delete=models.CASCADE)
    usr_name = models.CharField(max_length=500)
    usr_email = models.CharField(max_length=500, null=True, blank=True)
    usr_email_password = models.CharField(max_length=10, null=True, blank=True)
    usr_ph_otp = models.PositiveIntegerField(max_length=6, null=True, blank=True)
    usr_email_otp = models.PositiveIntegerField(max_length=6, null=True, blank=True)





