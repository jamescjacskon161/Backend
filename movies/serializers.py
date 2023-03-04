from rest_framework import serializers
from .models import Movies

class MovieSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields= '__all__'