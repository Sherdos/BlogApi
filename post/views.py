from django.shortcuts import render
from rest_framework import generics
from post.seralaizers import PostSerializer
from post.models import Post
# Create your views here.

class PostListViewApi(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
