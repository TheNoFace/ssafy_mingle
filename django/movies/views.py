from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Movie, Genre, Review, Comment

from .serializer import (
    MovieListSerializer,
    MovieReviewListSerializer,
    GenreNameSerializer,
    GenreMovieListSerializer,
    ReviewListSerializer,
)

import random


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
                movies = category.movies.all()[:10]
                serializer = MovieListSerializer(movies, many=True)
                movie_list[category.name] = serializer.data

            return Response(movie_list, status=status.HTTP_200_OK)


@api_view(["GET"])
def movie_detail(request, tmdb_id):
    if request.method == "GET":
        movie = Movie.objects.get(pk=tmdb_id)
        serializer = MovieListSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def movie_review(request, tmdb_id):
    if request.method == "GET":
        movie = Movie.objects.get(pk=tmdb_id)
        review_list = [movie.title]
        reviews = movie.review_set.all()
        serializer = MovieReviewListSerializer(reviews, many=True)
        review_list.append(serializer.data)
        return Response(review_list, status=status.HTTP_200_OK)


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

@api_view(['GET'])
def get_review_list(request):
    if request.method == "GET":
        reviews = Review.objects.all().order_by('-vote')[:1000]
        serializer = ReviewListSerializer(reviews, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def review_detail(request, review_pk):
    if request.method == "GET":
        review = Review.objects.get(pk = review_pk)
        serializer = ReviewListSerializer(review)
        return Response(serializer.data, status = status.HTTP_200_OK)