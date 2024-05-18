from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework import serializers


User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    """
    회원 가입 Serializer
    """

    class Meta:
        model = User
        fields = ("username", "nickname", "password")
        extra_kwargs = {"password": {"write_only": True, "min_length": 6}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    회원 정보 수정 Serializer
    """

    class Meta:
        model = User
        fields = ("username", "nickname", "password")
        extra_kwargs = {
            "username": {"read_only": True},
            "password": {"write_only": True, "min_length": 6},
        }

    def update(self, instance, validated_data):
        if not validated_data.get("password"):
            raise serializers.ValidationError(
                {"password": "Password field is required."}
            )
        else:
            instance.set_password(validated_data["password"])
            instance.nickname = validated_data["nickname"]
            instance.save()
            return instance


class UserSerializer(serializers.ModelSerializer):
    """
    회원 정보 Serializer
    """

    class Meta:
        model = User
        fields = ("username", "nickname")


class AuthSerializer(serializers.Serializer):
    """
    로그인 Serializer
    """

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)

        if not user:
            msg = "Unable to authenticate with provided credentials"
            raise serializers.ValidationError(msg, code="authentication")
        else:
            return user
