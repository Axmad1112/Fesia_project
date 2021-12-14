from django.urls import path
from .views import (
    CategoryListView, TaskListViewListCreateAPIView,TaskDetail,
    HomeworkViewListCreateAPIView, TeacherListCreateView,
    TeacherUpdateAPIView, TeacherDestroyAPIView,TeacherRetrieveAPIView,
    VideoListCreateAPIView,VideoRetrieveAPIView,
    VideoUpdateAPIView,VideoDestroyAPIView,
    HomeworkRetrieveAPIView,CourseViewSet,CourseOpenUpdateView,
    CourseBannedViewSet
    )
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"course",CourseViewSet)

urlpatterns = [
    path("category/", CategoryListView.as_view()),
    path("teachers/", TeacherListCreateView.as_view()),
    path("teachers/<int:pk>/", TeacherRetrieveAPIView.as_view()),
    path("teachers/<int:pk>/update/", TeacherUpdateAPIView.as_view()),
    path("teachers/<int:pk>/delete/", TeacherDestroyAPIView.as_view()),
    path("task/", TaskListViewListCreateAPIView.as_view()),
    path("task/<int:pk>/", TaskDetail.as_view()),
    path("homework/", HomeworkViewListCreateAPIView.as_view()),
    path("homework/<int:pk>/", HomeworkRetrieveAPIView.as_view()),
    path("video/",VideoListCreateAPIView.as_view()),
    path("video/<int:pk>/",VideoRetrieveAPIView.as_view()),
    path("video/<int:pk>/update/",VideoUpdateAPIView.as_view()),
    path("video/<int:pk>/delete/",VideoDestroyAPIView.as_view()),
    path("course/<int:pk>/open/",CourseOpenUpdateView.as_view()),
    path("course/banned/",CourseBannedViewSet.as_view()),
    
] + router.urls