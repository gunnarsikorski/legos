from django.shortcuts import render
from rest_framework import viewsets
from .models import Lego, Review
from .serializers import LegoSerializer, ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class LegoViewSet(viewsets.ModelViewSet):
    queryset = Lego.objects.all()
    serializer_class = LegoSerializer
