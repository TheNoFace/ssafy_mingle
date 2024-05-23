from django.shortcuts import get_list_or_404, get_object_or_404
from django.apps import apps
from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Movie, Genre, Review, Comment

from .serializers import *

import random
import requests
import json

BASE_DIR = settings.BASE_DIR

env_file = json.load(open(f"{BASE_DIR}/.env", "r"))

User = get_user_model()


# Create your views here.
@api_view(["GET"])
def get_movie_list(request, standard):
    if request.method == "GET":
        if standard == "popularity":
            movies = get_list_or_404(Movie.objects.order_by("-popularity"))[:10]
            serializer = MovieListSerializer(movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif standard == "release_date":
            movies = get_list_or_404(Movie.objects.order_by("-release_date"))[:10]
            serializer = MovieListSerializer(movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif standard == "category":
            categories = random.choices(get_list_or_404(Genre), k=5)

            movie_list = {}
            for category in categories:
                movies = category.movies.all().order_by("-release_date")[:10]
                serializer = MovieListSerializer(movies, many=True)
                movie_list[category.name] = serializer.data

            return Response(movie_list, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def movie_detail(request, tmdb_id):
    if request.method == "GET":
        movie = Movie.objects.get(pk=tmdb_id)
        serializer = MovieListSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def movie_review(request, tmdb_id):
    movie = get_object_or_404(Movie, pk=tmdb_id)
    if request.method == "GET":
        review_list = [movie.title]
        reviews = movie.review_set.all()
        serializer = MovieReviewListSerializer(reviews, many=True)
        review_list.append(serializer.data)
        return Response(review_list, status=status.HTTP_200_OK)
    elif request.method == "POST":
        if request.user.is_authenticated:
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user, movie=movie)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(["GET"])
def get_category(request):
    if request.method == "GET":
        genres = Genre.objects.all()
        serializer = GenreNameSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_category_movie(request, genre_pk):
    if request.method == "GET":
        genre = Genre.objects.get(pk=genre_pk)
        movie_list = [genre.name]
        movies = genre.movies.all().order_by("-popularity")[:10]
        serializer = MovieListSerializer(movies, many=True)
        movie_list.append(serializer.data)
        return Response(movie_list, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_review_list(request):
    if request.method == "GET":
        count = int(request.GET.get("page")) * 10
        reviews = get_list_or_404(Review.objects.order_by("-vote"))[:count]
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "POST", "DELETE", "PUT"])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == "GET":
        serializer = ReviewListSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.user.is_authenticated:
        # POST 메서드일 경우 댓글 작성, 이외 메서드는 리뷰 조작
        if request.method == "POST":
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(review=review, user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif request.user == review.user:
            if request.method == "DELETE":
                review.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            elif request.method == "PUT":
                serializer = ReviewSerializer(
                    instance=review, data=request.data, partial=True
                )
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(["DELETE", "PUT"])
def comment_manage(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user.is_authenticated:
        if request.user == comment.user:
            if request.method == "DELETE":
                comment.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            elif request.method == "PUT":
                serializer = CommentSerializer(
                    instance=comment, data=request.data, partial=True
                )
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(["POST"])
def like_target(request, target_model, target_pk):
    if request.user.is_authenticated:
        model = apps.get_model("movies", target_model.capitalize())
        target = get_object_or_404(model, pk=target_pk)
        if target.liked_users.filter(pk=request.user.pk).exists():
            target.liked_users.remove(request.user)
        else:
            target.liked_users.add(request.user)
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(["GET"])
def search_movie(request):
    token = env_file["TMDB_Token"]
    query = request.GET.get("query")
    page = 1
    url = f"https://api.themoviedb.org/3/search/movie?query={query}&include_adult=true&language=ko-KR&page={page}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        if response.headers.get("Content-Type") == "application/json;charset=utf-8":
            response = response.json()
            # count = 0
            for movie in response["results"]:
                if not Movie.objects.filter(pk=movie["id"]).exists():
                    created_movie = Movie.objects.create(
                        tmdb_id=movie["id"],
                        backdrop_path=movie["backdrop_path"],
                        poster_path=movie["poster_path"],
                        overview=movie["overview"],
                        popularity=movie["popularity"],
                        release_date=(
                            movie["release_date"] if movie["release_date"] else None
                        ),
                        title=movie["title"],
                        original_title=movie["original_title"],
                        vote_average=movie["vote_average"],
                        vote_count=movie["vote_count"],
                    )

                    genres = movie["genre_ids"]
                    for genre_id in genres:
                        genre = Genre.objects.get(pk=genre_id)
                        created_movie.genres.add(genre)
                    # print(f"Added movie {movie['id']}")
                    # count += 1
                # else:
                # print(f"Skipped adding movie {movie['id']}")
            # print(f'Added total {count} movie(s)')
            return Response(response, status=status.HTTP_200_OK)
        else:
            err_msg = {"Unexpected content type": response.headers.get("Content-Type")}

    except requests.exceptions.HTTPError as http_err:
        err_msg = {"HTTP error occurred": f"{http_err}"}
    except requests.exceptions.ConnectionError as conn_err:
        err_msg = {"Connection error occurred": f"{conn_err}"}
    except requests.exceptions.Timeout as timeout_err:
        err_msg = {"Timeout error occurred": f"{timeout_err}"}
    except requests.exceptions.RequestException as req_err:
        err_msg = {"An error occurred": f"{req_err}"}
    except ValueError as json_err:
        err_msg = {"JSON decode error": f"{json_err}"}
    except Exception as err:
        err_msg = {"An unexpected error occurred": f"{err}"}
    return Response(err_msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def liked_movie(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            movies = request.user.liked_movies.all()[:10]
            serializer = MovieListSerializer(movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def liked_category_movie(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            category_list = request.user.liked_genres.all()

            categories = random.choices(category_list, k=3)

            movie_list = {}
            for category in categories:
                movies = category.movies.all().order_by("-release_date")[:10]
                serializer = MovieListSerializer(movies, many=True)
                movie_list[category.name] = serializer.data

            return Response(movie_list, status=status.HTTP_200_OK)
