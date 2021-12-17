from rest_framework import generics,views
from rest_framework.response import Response
from .serializers import UserLoginSerializer, UserRegisterSerializer, ProfileSerializer
from .models import User, Profile


class UserRegisterView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

class UserLoginView(views.APIView):
    def post(self,request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class ProfileRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class ProfileUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class ProfileDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer