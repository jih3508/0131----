from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Comment, Todo
from .serializers import CommentSerializer, TodoSerializer


# Create your views here.

