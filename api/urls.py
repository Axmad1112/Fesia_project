from django.urls import path
from .views import CategoryListView, TaskDetail,TaskListViewListCreateAPIView,HomeworkViewListCreateAPIView,TeacherListCreateView

urlpatterns = [
    path("category/", CategoryListView.as_view()),
    path("teachers/", TeacherListCreateView.as_view()),
    path("task/", TaskListViewListCreateAPIView.as_view()),
    path("task/<int:pk>/", TaskDetail.as_view()),
    path("homework/", HomeworkViewListCreateAPIView.as_view()),
]
