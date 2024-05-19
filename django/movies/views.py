from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Movie, Genre, Review, Comment

from .serializer import MovieListSerializer

import random

# Create your views here.
@api_view(["GET"])
def get_movie_list(request, standard):
    if request.method == "GET":
        if standard == "popularity":
            movies = get_list_or_404(Movie.objects.order_by('-popularity'))[:10]
            serializer = MovieListSerializer(movies, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)

        elif standard == "release_date":
            movies = get_list_or_404(Movie.objects.order_by('-release_date'))[:10]
            serializer = MovieListSerializer(movies, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)

        elif standard == "category":
            all_category = Genre.objects.all()

            random_category = list(all_category)[:5]
            random.shuffle(random_category)
            
            movie_list = []
            for category in random_category:
                movie_list_inner = [category.name]
                movies = category.movies.all()[:10]
                serializer = MovieListSerializer(movies, many = True)
                movie_list_inner.append(serializer.data)
                movie_list.append(movie_list_inner)
            
            return Response(movie_list, status = status.HTTP_200_OK)