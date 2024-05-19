from rest_framework import serializers
from .models import Movie, Genre, Review, Comment

class MovieListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = '__all__'

