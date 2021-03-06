from rest_framework import generics, serializers, viewsets, permissions
from .serializers import CategorySerializer,TaskSerializer,TeacherSerializer,VideoSerializer,CourseSerializer,CourseOpenUpdateSerializer,HomeworkSerializer
from .models import Categories, Teacher, Course, Video, Task, Homework
from customer.models import Profile
from bank.models import SpentCoin, CoinBase
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import filters, validators
from django.shortcuts import get_object_or_404
from django.db.models import Q


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

class VideoListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class TaskListViewListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def perform_create(self, serializer):
            serializer.save(user=self.request.user)

class TaskDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    


class HomeworkViewListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_serializer_context(self):
        context = super(HomeworkViewListCreateAPIView, self).get_serializer_context()
        context.update({"request": self.request})
        return context
        
class HomeworkRetrieveAPIView(generics.RetrieveUpdateAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer

#Course
class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','teacher_id']
    
    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        # todo = Course.objects.filter(~Q(profile=profile))
        todo = Course.objects.all()
        return todo
    
#banned kurslar
class MyCourseViewSet(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','teacher_id']
    
    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        todo = Course.objects.filter(profile=profile)
        return todo
    
#Course open view
class CourseOpenUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course
    serializer_class = CourseOpenUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    
    def get_coin(self,cost):
        coin_base = CoinBase.objects.first()
        coin_base.coin+=cost
        course=Course.objects.get(id=self.kwargs['pk'])
        profile_coin = Profile.objects.get(user=self.request.user)
        profile_coin.coin=profile_coin.coin-cost
        
        
        if profile_coin.coin>=0:
            spent_coin = SpentCoin(from_profile=profile_coin,amount=cost,course=course, bank=coin_base)
            spent_coin.save()
            profile_coin.save()
            coin_base.save()
            # profile_coin.course.add(Course.objects.get(id=self.kwargs['pk']))
            course.profile.add(profile_coin)
            course.save()
            return True
        return False
    
    def perform_update(self, serializer):
        costs = self.get_coin(serializer.instance.cost)
        if costs is True:
            serializer.save()
        else:
            raise validators.ValidationError("nimadir hato")
        return super().perform_update(serializer)
    



