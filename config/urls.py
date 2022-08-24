from django.contrib import admin
from django.urls import path, include
from config.swagger import urlpatterns as swagger_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('config.routing'))
]
urlpatterns += swagger_urls
