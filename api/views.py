from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Posts, Todos, Comments
from .serializers import UserSerializer, PostsSerializer, TodosSerializer, CommentsSerializer

class UsersViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de User
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostsViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Posts
    """
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class TodosViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Todos
    """
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Todos
    """
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
