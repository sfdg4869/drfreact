from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
class PublicPostListAPIView(APIView):
    def get(self, request):
        qs = Post.objects.filter(is_public=True)
        seializer = PostSerializer(qs, many=True)
        return Response()
    
# @api_view(['GET'])
# def public_post_list(request):
#     qs = Post.objects.filter(is_public=True)
#     serializer = PostSerializer(qs, many=True)
#     return Response(serializer.data)


# class PublicPostListAPIView(generics.ListCreateAPIView):
#     queryset = Post.objects.filter(is_public=True) 
#     serializer_class = PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def dispathch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)