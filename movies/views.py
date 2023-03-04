#from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import MovieSerilizer
from .models import Movies
# Create your views here.
class MovieList(generics.ListAPIView):
    queryset=Movies.objects.all()
    serializer_class=MovieSerilizer

class MovieDetail(generics.RetrieveAPIView):
    queryset=Movies.objects.all()
    serializer_class=MovieSerilizer
    

