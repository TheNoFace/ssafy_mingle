from django.urls import path
from . import views

urlpatterns = [
    path('movies/<str:standard>/', views.get_movie_list),
    path('movies/detail/<int:tmdb_id>/', views.movie_detail),
    path('movies/detail/<int:tmdb_id>/review/', views.movie_review)
]
