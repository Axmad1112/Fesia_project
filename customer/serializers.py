from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.fields import ReadOnlyField
from .models import Profile
from api.serializers import CourseSerializer

User = get_user_model()

class UserRegisterSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=64,read_only=True)
    email = serializers.EmailField(max_length=255)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=200,write_only=True)
    password2 = serializers.CharField(max_length=200,write_only=True)

    def create(self, validated_data):
        email = validated_data.pop('email',None)
        username = validated_data.pop('username',None)
        password = validated_data.pop('password',None)
        password2 = validated_data.pop('password2',None)

        if password!=password2:
            raise serializers.ValidationError({"message":"password not matched"})
        if User.objects.filter(email=email).count()>0:
            raise serializers.ValidationError({"message":"Email already exist"})
        user = User(email=email,username=username,**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255,write_only=True)
    token = serializers.CharField(max_length=64,read_only=True)
    password = serializers.CharField(max_length=200,write_only=True)
    
    def validate(self, attrs):
        email = attrs.get("email",None)
        password = attrs.get("password",None)
        user = authenticate(email=email,password=password)
        if user is None:
            raise serializers.ValidationError({"message":"email or password error"})
        return user

class ProfileModelSerializer(serializers.ModelSerializer):
    coin = serializers.ReadOnlyField()
    user = UserRegisterSerializer(read_only=True)
    course = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = "__all__"

