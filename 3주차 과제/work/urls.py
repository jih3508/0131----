from django.urls import path
from .api import TodoCreateApi, CommentCreateApi, TodoApi, CommentAPI, TodoUpdateApi, CommentUpdateApi, TodoDeleteApi, CommentDeleteApi

urlpatterns = [
    path('todo/', TodoCreateApi.as_view()), #Post
    path('comment/', CommentCreateApi.as_view()), #Post
    path('todo/', TodoApi.as_view()),  # Get
    path('comment/', CommentAPI.as_view()),  # Get
    path('todo/<int:pk>', TodoUpdateApi.as_view()), #PUT
    path('comment/<int:pk>', CommentUpdateApi.as_view()), # PUT
    path('todo/<int:pk>', TodoDeleteApi.as_view()),  # Delete
    path('comment/<int:pk>', CommentDeleteApi.as_view()),  # Delete
]