from django.urls import path
from . import views

urlpatterns = [
    path("movies/<str:standard>/", views.get_movie_list),
    path("movies/detail/<int:tmdb_id>/", views.movie_detail),
    path("movies/detail/<int:tmdb_id>/review/", views.movie_review),
    path("movies/recommend/category/", views.get_category),
    path("movies/recommend/category/<int:genre_pk>/", views.get_category_movie),
    path("movies/recommend/review/", views.get_review_list),
    path("movies/review/detail/<int:review_pk>/", views.review_detail),
    path("movies/comment/<int:comment_pk>/", views.comment_manage),
    path("movies/like/<str:target_model>/<int:target_pk>/", views.like_target),
    path("movies/search/tmdb/", views.search_movie),
    path('movies/like/movie/', views.liked_movie),
    path('movies/like/category/movie/', views.liked_category_movie),
]
