from django.urls import path
from knox import views as knox_views
from .views import *

urlpatterns = [
    path("create/", CreateUserView.as_view(), name="create"),
    path("profile/<str:username>/", UserView.as_view(), name="profile"),
    path("profile/<str:username>/check/", UserCheckView.as_view(), name="profile-check"),
    path("profile/<str:username>/detail/", UserDetailView.as_view(), name="profile-detail"),
    path("profile/<str:username>/follow/", UserRelationView.as_view(), name="profile-follow"),
    path("update/", UserUpdateView.as_view(), name="profile-update"),
    path("login/", LoginView.as_view(), name="knox_login"),
    path("logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path("logoutall/", knox_views.LogoutAllView.as_view(), name="knox_logoutall"),
]
