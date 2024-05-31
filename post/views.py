from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from post.seralaizers import PostSerializer
from post.models import Post
from rest_framework.response import Response
from django.forms.models import model_to_dict
# Create your views here.

# class PostListViewApi(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
class PostListViewApi(APIView):
    def get(self, request):
        posts = Post.objects.all().values()
        return Response({'posts':list(posts)})
    
    def post(self, request):
        new_post = Post.objects.create(
            title=request.data['title'],
            descrition=request.data['descrition'],
            category_id=request.data['category_id'],
        )
        return Response({'post':model_to_dict(new_post,('id','title','descrition','created'))})

    def put(self,request,*arg, **kwarg):
        pk = kwarg.get('pk',None)
        if not pk:
            return Response({'error':'Method Put not allowed'})
        try:
            instance = Post.objects.get(pk=pk)
        except:
            return Response({'error':'Object not found'})
        instance.title = request.data['title']
        instance.descrition = request.data['descrition']
        instance.category_id = request.data['category_id']
        instance.save()
        return Response({'post':model_to_dict(instance,('id','title','descrition','created'))})
        
    