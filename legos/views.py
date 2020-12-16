from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from .models import Lego, Review
from .serializers import LegoSerializer, ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class LegoViewSet(viewsets.ModelViewSet):
    search_fields = ['name', 'minifigures', 'set_series', 'release_year', 'set_number']
    filter_backends = (filters.SearchFilter,)
    queryset = Lego.objects.all()
    serializer_class = LegoSerializer

# found how to add search endpoint to my API from a medium article, so sweet!