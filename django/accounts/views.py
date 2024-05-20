# django imports
from django.contrib.auth import login
from django.contrib.auth import get_user_model

# rest_framework imports
from rest_framework import status
from rest_framework import generics, authentication, permissions
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authentication import SessionAuthentication

# knox imports
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication

# local apps import
from .serializers import *

User = get_user_model()


class CreateUserView(generics.CreateAPIView):
    # Create user API view
    serializer_class = UserCreateSerializer


class LoginView(KnoxLoginView):
    # login view extending KnoxLoginView
    serializer_class = AuthSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data["user"]
            login(request, user)
            return super(LoginView, self).post(request, format=None)


class UpdateUserView(generics.UpdateAPIView):
    """
    Manage the authenticated user
    """

    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

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
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    lookup_field = "username"
