from django.forms.models import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission, IsAuthenticated,IsAdminUser
from post.models import Post, Category  
from post.serializers import PostSerializer,CategorySerializer

# Create your views here.



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = (IsAuthenticated,)

    @action(methods=['get'], detail = True)
    def category(self, request, pk=None):
        cats = Category.objects.filter(post=pk)
        return Response(CategorySerializer(cats, many=True).data)



# class CategoryPostAPIListView(generics.ListAPIView):

#     serializer_class = PostSerializer


    # def get_queryset(self, *args, **kwargs):
    #     pk = self.kwargs.get('pk',None)
    #     posts = Post.objects.filter(category = pk)
    #     return posts
    
    
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

# class PostCreateListAPIView(generics.ListCreateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
    
# class PostDetailAPIView(generics.RetrieveAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()


# class PostCreateListApiView(generics.ListCreateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()


# class PostCRUD(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()


# class PostUpdate(generics.UpdateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

# class PostCreate(generics.CreateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

# class PostDelete(generics.DestroyAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

# class PostDetail(generics.RetrieveAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

# class PostAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post,objects.all()
#     serializer_class = PostSerializer

# class PostAPIListView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer