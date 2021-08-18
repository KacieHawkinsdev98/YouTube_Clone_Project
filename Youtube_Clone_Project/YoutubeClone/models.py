from django.db import models

# Create your models here.


class Comments(models.Model):
    videoID = None
    comment = models.CharField(max_length=500)
    replies = models.CharField(max_length=500)
    likes = models.IntegerField()
    dislikes = models.IntegerField()