from django.http import request
from rest_framework import serializers, validators
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
    
class HomeworkSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    teacher = TeacherSerializer(read_only=True)
    feedback = serializers.ReadOnlyField()
    correct = serializers.ReadOnlyField()
    
    class Meta:
        model = Homework
        fields = "__all__"
    
    def create(self, validated_data):
        queryset = Homework.objects.filter(user=self.context['request'].user)
        # print(str(queryset[1].task))
        current_task = validated_data.get('task', None)
        print(validated_data)
        print(current_task, "xozirgi task")
        for obj in queryset:
            if str(obj.task)==str(current_task):
                raise validators.ValidationError('You have already applyed homework')
        return super().create(validated_data)

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