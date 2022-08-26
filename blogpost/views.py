from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from blogpost import models, serializers
from blogpost.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOrReadOnly]


class CommentList(generics.ListCreateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, is_active=True)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOrReadOnly]
