from django.db import models
from django.contrib.auth.models import AbstractUser
# from imagekit.models import ProcessedImageField
# from imagekit.processors import ResizeToFill


class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')

    def __str__(self) :
        return self.username
