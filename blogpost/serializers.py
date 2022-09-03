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
    author = serializers.ReadOnlyField(source='author.username')
    likes = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'image', 'created_at', 'updated_at', 'comments', 'likes', 'is_liked')

    def get_likes(self, obj):
        return obj.get_total_likes()

    def get_is_liked(self, obj):
        return self.context['request'].user in obj.likes.all()


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = '__all__'
