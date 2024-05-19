from django.urls import path
from . import views

urlpatterns = [
    path('movies/<str:standard>/', views.get_movie_list),
]
