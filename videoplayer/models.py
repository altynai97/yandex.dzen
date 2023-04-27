from django.db import models
from django.contrib.auth.models import AbstractUser


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')


class User(AbstractUser):
    pass
