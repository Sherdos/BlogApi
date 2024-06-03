import io
from rest_framework import serializers
from post.models import Post

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = '__all__'

class PostModel():
    def __init__(self, title, description) -> None:
        self.title = title
        self.description = description


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

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    count_like = serializers.IntegerField(default = 0)
    category_id = serializers.IntegerField()
    created = serializers.DateTimeField(read_only=True)
    image = serializers.ImageField(read_only = True)
    