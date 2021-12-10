from rest_framework import generics
from .serializers import CategorySerializer
from .models import *

# Create your views here.
class CategoryListView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    