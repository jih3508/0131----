from .models import Todo, Comment
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model =Todo
        fields = ['id', 'title', 'description', 'is_completed', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'contents', 'created_at', 'updated_at']
