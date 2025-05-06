from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializar
from .models import Moviedata

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializar

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(genre='action')
    serializer_class = MovieSerializar