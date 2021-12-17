from django.http import request
from rest_framework import serializers
from .models import Categories, Teacher, Course, Video, Task

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    text = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    lesson = serializers.ReadOnlyField(source='lesson.name')
    
    class Meta:
        model = Task
        fields = "__all__"
    
    def update(self, instance, validated_data):
        if instance:
            self.user=instance.user
        return super().update(instance, validated_data)
    
# class HomeworkSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source='user.username')
#     user_id = serializers.ReadOnlyField(source='user.id')
#     class Meta:
#         model = Homework
#         fields = "__all__"

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

#Course Serializers
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class CourseOpenUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
        read_only_fields = ['name','image','category_id','teacher_id','cost','data','banned']