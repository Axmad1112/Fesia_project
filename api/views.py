from rest_framework import generics
from .serializers import CategorySerializer,TaskSerializer,HomeworkSerializer
from .models import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CategoryListView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer


class TaskListViewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class HomeworkViewListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

