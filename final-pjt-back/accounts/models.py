from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')
    image = ProcessedImageField(
        blank=True,
        upload_to='profile_images/%Y/%m/%d/',
        processors=[ResizeToFill(200,200)],
        format='JPEG',
        options={'quality': 100}
        )

    def __str__(self) :
        return self.username
