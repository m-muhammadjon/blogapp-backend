from django.shortcuts import render

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated

from blogpost import models, serializers
from blogpost.utils import create_or_delete_action
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_like(request):
    print(request.data)

    try:
        post = models.Post.objects.get(id=request.data.get('post'))
        action = request.data.get('action')
        if post and action:
            if action == 'like':
                post.likes.add(request.user)
                create_or_delete_action(request.user, 'liked', post)
                return Response({'status: ok'}, status=status.HTTP_200_OK)
            else:
                post.likes.remove(request.user)
                create_or_delete_action(request.user, 'liked', post, False)
                return Response({'status: error'}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'status': 'error'}, status=status.HTTP_400_BAD_REQUEST)
