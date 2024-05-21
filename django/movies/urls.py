from django.urls import path
from . import views

urlpatterns = [
    path("movies/<str:standard>/", views.get_movie_list),
    path("movies/detail/<int:tmdb_id>/", views.movie_detail),
    path("movies/detail/<int:tmdb_id>/review/", views.movie_review),
    path("movies/recommend/category/", views.get_category),
    path("movies/recommend/category/<int:genre_pk>/", views.get_category_movie),
]
