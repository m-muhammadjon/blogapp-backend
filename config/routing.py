from django.urls import path, include

urlpatterns = [
    path('', include('account.urls')),
    path('', include('blogpost.urls')),
]
