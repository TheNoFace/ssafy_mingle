from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Movie, Genre, Review, Comment

from .serializer import *

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
        reviews = Review.objects.all().order_by("-vote")[:1000]
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
