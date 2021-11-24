import requests
from decouple import config
from movies.models import Movie

import random
from django.db.models import Q

class weatherHelper:
    def __init__(self):
        self.worldId = config('WORLD_ID')

    def movieRecommendByWeather(self):

        weather_url = f"https://www.metaweather.com/api/location/{self.worldId}/"

        response = requests.get(weather_url).json()
        data = response['consolidated_weather'][1]
        weather_type = data['weather_state_abbr']
        month = data['applicable_date'].split("-")[1]
        
        summer = ['6', '7', '8', '9']
        winter = ['11', '12', '1', '2']
        genre_winter = [3, 4, 8, 9, 14]
        winter_random = random.sample(genre_winter, 2)

        weather_nice = ['c', 'lc', 'hc']
        genre_nice = [1, 2, 4, 5, 9, 15]
        nice_random = random.sample(genre_nice, 2)

        weather_rain = ['h', 't', 'hr', 'lr', 's']
        genre_rain = [1, 11, 13, 14, 17]
        rain_random = random.sample(genre_rain, 2)

        if month in winter:
            return Movie.objects.filter(
                (Q(release_date__month=11) | Q(release_date__month=12) | Q(release_date__month=1) | Q(release_date__month=2)) & 
                (Q(genres=winter_random[0]) | Q(genres=winter_random[1]))).order_by('?')[:50]

        elif month in summer:
            return Movie.objects.filter(
                (Q(release_date__month='06') | Q(release_date__month='07') | Q(release_date__month='08') | Q(release_date__month='09')) & 
                (Q(genres=rain_random[0]) | Q(genres=rain_random[1]))).order_by('?')[:50]

        elif weather_type in weather_nice:
            return Movie.objects.filter(
                Q(genres=nice_random[0]) | Q(genres=nice_random[1])).order_by('?')[:50]

        elif weather_type in weather_rain:
            return Movie.objects.filter(
                Q(genres=rain_random[0]) | Q(genres=rain_random[1])).order_by('?')[:50]