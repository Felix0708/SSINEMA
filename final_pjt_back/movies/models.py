from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    genre_id = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.pk}: {self.name}'


class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    popularity = models.FloatField(null=True)
    release_date = models.DateField(null=True)
    overview = models.TextField(null=True)
    video_path = models.CharField(max_length=200, null=True)
    poster_path = models.CharField(max_length=200, null=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name = 'favorite_movies',
    )
    genres = models.ManyToManyField(Genre, related_name='genre')

    def __str__(self):
        return f'{self.pk}: {self.title}'

class Review(models.Model):
    # RANKS = [
    #     (1, '★'),
    #     (2, '★★'),
    #     (3, '★★★'),
    #     (4, '★★★★'),
    #     (5, '★★★★★'),
    # ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name = 'reviews'
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    # rank = models.IntegerField(choices=RANKS, default=5)
    rank = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk}: {self.content}'