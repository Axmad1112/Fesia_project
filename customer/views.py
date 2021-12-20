from django.db.models.query import QuerySet
from rest_framework import generics,views
from rest_framework.response import Response

from api.models import Course
from .serializers import UserLoginSerializer, UserRegisterSerializer,ProfileModelSerializer
from .models import User, Profile


class UserRegisterView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

class UserLoginView(views.APIView):
    def post(self,request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileModelSerializer

class ProfileUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileModelSerializer

   

