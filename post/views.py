from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from post.serializers import PostSerializer
from post.models import Post
from rest_framework.response import Response
from django.forms.models import model_to_dict
# Create your views here.

# class PostListViewApi(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
class PostListViewApi(APIView):
    def get(self, request):
        posts = Post.objects.all()
        return Response({'posts':PostSerializer(posts, many=True).data})
    
    def post(self, request):
        serializer = PostSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        new_post = Post.objects.create(
            title=request.data['title'],
            description=request.data['description'],
            category_id=request.data['category_id'],
        )
        return Response({'post':PostSerializer(new_post).data})

    def put(self,request,*arg, **kwarg):
        pk = kwarg.get('pk',None)
        if not pk:
            return Response({'error':'Method Put not allowed'})
        try:
            instance = Post.objects.get(pk=pk)
        except:
            return Response({'error':'Object not found'})
        instance.title = request.data['title']
        instance.description = request.data['description']
        instance.category_id = request.data['category_id']
        instance.save()
        return Response({'post':PostSerializer(instance).data})
        
    