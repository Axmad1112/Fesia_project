from django.urls import path
from .views import UserRegisterView, UserLoginView, ProfileRetrieveAPIView, ProfileUpdateAPIView, ProfileDestroyAPIView

urlpatterns = [
    path('register/',UserRegisterView.as_view()),
    path('login/',UserLoginView.as_view()),
    path('profile/<int:pk>/',ProfileRetrieveAPIView.as_view()),
    path('profile/<int:pk>/update/',ProfileUpdateAPIView.as_view()),
    path('profile/<int:pk>/delete/',ProfileDestroyAPIView.as_view()),
    ]
