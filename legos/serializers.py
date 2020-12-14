from rest_framework import serializers
from .models import Lego, Review


class ReviewSerializer(serializers.ModelSerializer):
    lego_name = serializers.ReadOnlyField(
        source = 'lego.name',
        read_only = True
    )

    class Meta:
        model = Review
        fields = ('id', 'title', 'lego', 'lego_name', 'body')


class LegoSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Lego
        fields = ('id', 'set_series', 'name', 'set_number', 'piece_count', 'source', 'release_year', 'minifigures', 'image_url', 'reviews')