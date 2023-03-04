from django.http import HttpResponse
from rest_framework import generics
from .serializers import CategorySerilizer
from .models import Category
# Create your views here.
class CategoryList(generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerilizer

class CategoryDetail(generics.RetrieveAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerilizer