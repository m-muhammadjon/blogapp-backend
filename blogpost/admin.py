from django.contrib import admin
from blogpost.models import Post, Comment, Action

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Action)
