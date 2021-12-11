from rest_framework import generics
from .serializers import CategorySerializer,TaskSerializer,HomeworkSerializer,TeacherSerializer
from .models import Categories, Teacher, Course, Video, Task, Homework
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

#GET and POST
class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

# GET_ID
class TeacherRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


# PUT_ID
class TeacherUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


# DELETE_ID
class TeacherDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

# Create your views here.
class CategoryListView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

class TaskListViewListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class HomeworkViewListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        


