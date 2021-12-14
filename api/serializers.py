from rest_framework import serializers
from .models import Categories, Teacher, Course, Video, Task, Homework

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
    
class HomeworkSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Homework
        fields = "__all__"

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"