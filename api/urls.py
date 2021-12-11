from django.urls import path
from .views import (
    CategoryListView, TaskListViewListCreateAPIView,TaskDetail,
    HomeworkViewListCreateAPIView, TeacherListCreateView,
    TeacherUpdateAPIView, TeacherDestroyAPIView,TeacherRetrieveAPIView
)


urlpatterns = [
    path("category/", CategoryListView.as_view()),
    path("teachers/", TeacherListCreateView.as_view()),
    path("teachers/<int:pk>/", TeacherRetrieveAPIView.as_view()),
    path("teachers/<int:pk>/update/", TeacherUpdateAPIView.as_view()),
    path("teachers/<int:pk>/delete/", TeacherDestroyAPIView.as_view()),
    path("task/", TaskListViewListCreateAPIView.as_view()),
    path("task/<int:pk>/", TaskDetail.as_view()),
    path("homework/", HomeworkViewListCreateAPIView.as_view()),
]
