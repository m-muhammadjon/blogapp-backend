from rest_framework import serializers
from blogpost.models import Post, Comment


class CommentShortSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('user', 'body',)

    def get_user(self, obj):
        return obj.user.username


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    author = serializers.ReadOnlyField(source='author.username')
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'image', 'created_at', 'updated_at', 'comments', 'likes')

    def get_comments(self, obj):
        return CommentShortSerializer(obj.comments, many=True).data

    def get_likes(self, obj):
        return obj.get_total_likes()


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = '__all__'
