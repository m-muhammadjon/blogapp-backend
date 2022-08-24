from django.urls import path

from account import views

urlpatterns = [
    path('user-create', views.user_create, name='user_create'),
    path('user-update', views.user_update, name='user_update'),
    path('user-login', views.user_login, name='user_login'),
    path('get-user', views.get_user, name='get_user'),
]
