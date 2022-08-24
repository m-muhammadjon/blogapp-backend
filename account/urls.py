from django.urls import path

from account import views

urlpatterns = [
    path('user-login', views.user_login, name='user_login'),
    path('get-user', views.get_user, name='get_user'),
]
