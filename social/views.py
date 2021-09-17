from django.db.models import Avg
from django.shortcuts import render

# Create your views here.
from django_filters import filters
from rest_framework import generics
from rest_framework.response import Response

from social.filters import PostFilterset
from social.models import Post
from social.serializers import PostSerializer
from datetime import datetime, timedelta


class PostDetail(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    post_filterset = PostFilterset

    def get(self, request, *args, **kwargs):
        query_params = request.query_params

        filterset = self.post_filterset(
            data=query_params,
            queryset=self.queryset
        )
        serializer = self.serializer_class(filterset.qs, many=True)
        return Response(serializer.data)




class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LikesAverage(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    post_filterset = PostFilterset

    def get(self, request, *args, **kwargs):
        query_params = request.query_params

        filterset = self.post_filterset(
            data=query_params,
            queryset=self.queryset
        )
        queryset = filterset.qs.filter(post_date__gte=datetime.today() - timedelta(days=90)).aggregate(Avg('likes_count'))

        return Response(queryset)

