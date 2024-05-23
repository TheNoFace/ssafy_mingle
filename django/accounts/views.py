# django imports
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

# rest_framework imports
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

# knox imports
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication

# local apps import
from .serializers import *

from movies.models import Genre

User = get_user_model()


class CreateUserView(generics.CreateAPIView):
    # Create user API view
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        genres = list(map(int, self.request.data.get("genres").split(",")))
        for genre_id in genres:
            print(genre_id)
            genre = get_object_or_404(Genre, pk=genre_id)
            user.liked_genres.add(genre)
        return Response(user, status=status.HTTP_201_CREATED)


class LoginView(KnoxLoginView):
    # login view extending KnoxLoginView
    serializer_class = AuthSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data["user"]
            login(request, user)
            return super(LoginView, self).post(request, format=None)


class UserUpdateView(generics.UpdateAPIView):
    """
    Manage the authenticated user
    """

    serializer_class = UserUpdateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """
        Retrieve and return authenticated user data
        """
        return self.request.user

    def update(self, request, *args, **kwargs):
        """
        Retrieve request data and update authenticated user data
        """
        serializer = self.serializer_class(
            request.user, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


class UserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    lookup_field = "username"


class UserCheckView(APIView):
    """
    Check ownership of profile detail page
    """

    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()

    def get_object(self):
        target_user = get_object_or_404(self.queryset, username=self.kwargs["username"])
        return target_user

    def get(self, request, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        target_user = self.get_object()
        if self.request.user == target_user:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)


class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    lookup_field = "username"


class UserRelationView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()

    def get_object(self):
        target_user = get_object_or_404(self.queryset, username=self.kwargs["username"])
        return target_user

    def put(self, request, **kwargs):
        target_user = self.get_object()
        if self.request.user != target_user:
            if target_user.followers.filter(pk=self.request.user.pk).exists():
                target_user.followers.remove(self.request.user)
            else:
                target_user.followers.add(self.request.user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
