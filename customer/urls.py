from django.urls import path
from .views import UserRegisterView, UserLoginView, ProfileListAPIView,ProfileUpdateDestroyAPIView

urlpatterns = [
    path('register/',UserRegisterView.as_view()),
    path('login/',UserLoginView.as_view()),
    path('profile/',ProfileListAPIView.as_view()),
    path('profile/<int:pk>/',ProfileUpdateDestroyAPIView.as_view()),
    # path('profile/<int:pk>/update/',ProfileUpdateAPIView.as_view()),
    # path('profile/<int:pk>/delete/',ProfileDestroyAPIView.as_view()),
    ]
