from rest_framework import serializers
from .models import Movie, Genre, Review, Comment
from accounts.serializers import UserSerializer


class GenreNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            "tmdb_id",
            "name",
        )


class GenreMovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class MovieImageSerializer(serializers.ModelSerializer):
    genres = GenreNameSerializer(many = True, read_only = True)
    
    class Meta:
        model = Movie
        fields = ("poster_path", "tmdb_id", "title", 'vote_average', 'release_date', 'genres',)


class ReviewCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    class Meta:
        model = Comment
        fields = ("content", 'user', 'liked_users', 'created_at', )


class MovieReviewListSerializer(serializers.ModelSerializer):
    movie = MovieImageSerializer(read_only=True)
    liked_users_count = serializers.IntegerField(
        source="liked_users.count", read_only=True
    )
    comment_set = ReviewCommentSerializer(read_only=True, many=True)
    comment_count = serializers.IntegerField(source="comment_set.count", read_only=True)

    class Meta:
        model = Review
        fields = "__all__"


class ReviewListSerializer(serializers.ModelSerializer):
    movie = MovieImageSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    comment_set = ReviewCommentSerializer(read_only=True, many=True)

    class Meta:
        model = Review
        fields = "__all__"


class MovieListSerializer(serializers.ModelSerializer):
    genres = GenreNameSerializer(many=True, read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source="review_set.count", read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"
