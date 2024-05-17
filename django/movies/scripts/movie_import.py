import requests
import json
from ..models import Movie, Genre

token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3M2E3YjFlNjM4ZmMyZWM1NzUwZmRhZGYxNDI1OWZkYiIsInN1YiI6IjY2Mjc0Y2Q1N2E5N2FiMDE2MzhkZmIwYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.GkpTQr0h12G2EdZ7kYmn3-d1Md3EQN_XoFcYP9xoMRM"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {token}"
}

genre_url = "https://api.themoviedb.org/3/genre/movie/list?language=ko"
response = requests.get(genre_url, headers=headers)
response = json.loads(response.text)

for result in response["genres"]:
    Genre.objects.create(
        tmdb_id = result['id'],
        name = result['name']
    )
print(f'장르 추가 완료')

target = 100
for page in range(1, target + 1):
    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=ko-KR&page={page}&sort_by=popularity.desc"
    response = requests.get(url, headers=headers)
    response = json.loads(response.text)
    
    for result in response['results']:
        if Movie.objects.filter(pk=result['id']):
            continue

        Movie.objects.create(
            tmdb_id = result['id'],
            backdrop_path = result['backdrop_path'],
            poster_path = result['poster_path'],
            overview = result['overview'],
            popularity = result['popularity'],
            release_date = result['release_date'] if result['release_date'] else None,
            title = result['title'],
            original_title = result['original_title'],
            vote_average = result['vote_average'],
            vote_count = result['vote_count']
        )

        movie = Movie.objects.get(pk=result['id'])
        genres = result['genre_ids']
        
        for genre_id in genres:
            genre = Genre.objects.get(pk=genre_id)
            movie.genres.add(genre)

    print(f'페이지 {page} 완료')
