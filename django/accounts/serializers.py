from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework import serializers
from movies.models import Genre, Movie, Review, Comment

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
        fields = ("id", "username", "nickname")


class UserDetailSerializer(serializers.ModelSerializer):
    """
    회원 프로필 페이지 Serializer
    """

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ("name",)

    class MovieSerialzier(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = (
                "title",
                "poster_path",
                "tmdb_id",
            )

    class ReviewSerializer(serializers.ModelSerializer):
        class MovieImageSerializer(serializers.ModelSerializer):
            class Meta:
                model = Movie
                fields = ("poster_path", "tmdb_id")

        class ReviewCommentSerializer(serializers.ModelSerializer):
            class Meta:
                model = Comment
                fields = ("content",)

        user = UserSerializer(read_only = True)
        movie = MovieImageSerializer(read_only=True)
        comment_set = ReviewCommentSerializer(many=True, read_only=True)

        class Meta:
            model = Review
            fields = "__all__"

    class CommentSerializer(serializers.ModelSerializer):
        user = UserSerializer(read_only=True)

        class Meta:
            model = Comment
            fields = (
                "content",
                "created_at",
                "liked_users",
                "user",
            )

    liked_movies = MovieSerialzier(read_only=True, many=True)
    liked_genres = GenreSerializer(many=True, read_only=True)
    liked_reviews = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    liked_comments = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    review_set = ReviewSerializer(read_only=True, many=True)
    comment_set = CommentSerializer(read_only=True, many=True)

    followers = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = User
        fields = (
            "username",
            "nickname",
            "followings",
            "followers",
            "liked_movies",
            "liked_genres",
            "liked_reviews",
            "liked_comments",
            "review_set",
            "comment_set",
        )


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
