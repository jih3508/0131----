from rest_framework import generics
from rest_framework.response import Response
from .serializers import TodoSerializer, CommentSerializer
from .models import Todo, Comment


class TodoApi(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todo


class CommentAPI(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = Comment


class TodoCreateApi(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todo


class CommentCreateApi(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = Comment


class TodoUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todo


class CommentUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = Comment


class TodoDeleteApi(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todo


class CommentDeleteApi(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = Comment
