import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from post.models import Post

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = '__all__'

# class PostModel():
#     def __init__(self, title, description) -> None:
#         self.title = title
#         self.description = description


# def encode():
#     model = PostModel('hello', 'hello2, hi1,')
#     model_sr = PostSerializer(model)
#     json = JSONRenderer().render(model_sr.data)
#     print(json, type(json), sep='\n')

# def decode():
#     json = io.BytesIO(b'{"title":"hello","description":"hello2, hi1,"}')
#     data = JSONParser().parse(json)
#     serializer = PostSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data, type(serializer), sep='\n')

# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     description = serializers.CharField()
#     count_like = serializers.IntegerField(default = 0)
#     category_id = serializers.IntegerField()
#     created = serializers.DateTimeField(read_only=True)
#     image = serializers.ImageField(read_only = True)
    
#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)
    
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.count_like = validated_data.get('count_like', instance.count_like)
#         instance.category_id = validated_data.get('category_id', instance.category_id)
#         instance.image = validated_data.get('image', instance.image)
#         instance.save()
#         return instance


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =  '__all__'
