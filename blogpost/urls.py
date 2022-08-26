from django.urls import path

from blogpost import views

app_name = 'blogpost'

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<int:id>', views.PostDetail.as_view(), name='post_detail'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:id>', views.CommentDetail.as_view(), name='comment_detail'),
]
