import requests
from movies.models import Movie, Genre
from decouple import config
import datetime

class TMDBHelper:
    """API 요청에 필요한 기능들을 제공합니다.
    """

    def __init__(self):
        self.api_key = config('API_KEY')


    def create_movies(self):
        URL = f"https://api.themoviedb.org/3/movie/popular?api_key={self.api_key}&language=ko-KR&page="
        for pageNum in range(1, 101):
        # for pageNum in range(1, 2):
            res = requests.get(URL + str(pageNum)).json()

            movie_list = res['results']
            for movie in movie_list:
                movie_id = movie['id']

                if Movie.objects.filter(movie_id=movie_id).exists():
                    continue

                else:
                    title = movie['title']
                    vote_average = movie['vote_average']
                    vote_count = movie['vote_count']
                    popularity = movie['popularity']      
                    overview = movie["overview"]
                    poster_path = movie["poster_path"]
                    genre_ids_list = movie["genre_ids"]

                    try:
                        release_date = datetime.datetime.strptime(movie["release_date"], "%Y-%m-%d").date()
                        VIDEO_URL = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={self.api_key}&append_to_response=videos"
                        video_res = requests.get(VIDEO_URL).json()
                        video_result = video_res["videos"]["results"]
                        if video_result:
                            video_path = video_result[0]['key']

                    except:
                        continue

                    movie = Movie.objects.create(
                        movie_id = movie_id,
                        title = title,
                        vote_average = vote_average,
                        vote_count = vote_count,
                        popularity = popularity,
                        release_date = release_date,
                        overview = overview,
                        poster_path = poster_path,
                        video_path = video_path
                    )

                    for genre in genre_ids_list:
                        genre_object = Genre.objects.get(genre_id=genre)
                        movie.genres.add(genre_object)

        return print('complete_movie_saved')