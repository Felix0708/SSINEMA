from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    genre_id = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.pk}: {self.name}'

class Movie(models.Model):
    title = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    vote_average = models.FloatField()
    overview = models.TextField()
    video_path = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre, related_name='genre')

    def __str__(self):
        return f'{self.pk}: {self.title}'

class Review(models.Model):
    RANKS = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="review")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    rank = models.IntegerField(choices=RANKS, default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}: {self.title}'