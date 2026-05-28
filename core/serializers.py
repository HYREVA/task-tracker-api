from rest_framework import serializers
from .models import Category, Tag, Task, TaskComment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    tags = serializers.StringRelatedField(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), source='tags', many=True, write_only=True
    )

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'is_completed', 'deadline', 'created_at', 'category', 'category_id', 'tags', 'tag_ids']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = '__all__'