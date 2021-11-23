from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = ProcessedImageField(
        blank=True,
        upload_to='articles_images/%Y/%m/%d/',
        processors=[ResizeToFill(960,1280)],
        format='JPEG',
        options={'quality': 100}
        )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.title}'

    @property
    def update_counter(self):
        self.view_count = self.view_count + 1
        self.save()

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.content}'
