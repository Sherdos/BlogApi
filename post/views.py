from django.forms.models import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import Post
from post.serializers import PostSerializer

# Create your views here.

# class PostListViewApi(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
# class PostListAPIView(APIView):
    
#     def get(self, request):
#         posts = Post.objects.all()
#         return Response({'posts':PostSerializer(posts, many=True).data})
    
#     def post(self, request):
#         serializer = PostSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post':serializer.data})

#     def put(self,request,*arg, **kwarg):
#         pk = kwarg.get('pk',None)
#         if not pk:
#             return Response({'error':'Method Put not allowed'})
#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({'error':'Object not found'})
#         serializer = PostSerializer(instance=instance, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post':serializer.data})
        
#     def delete(self, request, *arg, **kwarg):
#         pk = kwarg.get('pk',None)
#         if not pk:
#             return Response({'error':'Method Delete not allowed'})
#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({'error':'Object not found'})
#         instance.delete()
#         return Response({'post': f'deleted post {pk}'})

class PostCreateListAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
class PostDetailAPIView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()