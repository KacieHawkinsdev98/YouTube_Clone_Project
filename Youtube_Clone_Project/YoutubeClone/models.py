from django.db import models

# Create your models here.


class Comments(models.Model):
    video_id = models.CharField(max_length=50, default='')
    body = models.CharField(max_length=500)
    replies = models.CharField(max_length=500)
    likes = models.IntegerField()
    dislikes = models.IntegerField()

class Reply(models.Model):
    comment = models.ForeignKey(Comments, blank=True, null=True, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)


class Video(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    path = models.CharField(max_length=70)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)


class Channel(models.Model):
    channel_name = models.CharField(max_length=50, blank=False, null=False)
    subscribers = models.IntegerField(default=0, blank=False, null=False)
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)
