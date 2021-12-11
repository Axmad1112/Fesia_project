from django.urls import path
from .views import CategoryListView,TaskListViewListCreateAPIView,HomeworkViewListCreateAPIView

urlpatterns = [
    path("category/", CategoryListView.as_view()),
    path("task/", TaskListViewListCreateAPIView.as_view()),
    path("homework/", HomeworkViewListCreateAPIView.as_view()),
]
