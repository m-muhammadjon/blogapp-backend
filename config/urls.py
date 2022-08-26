from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config.swagger import urlpatterns as swagger_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('config.routing'))
]

urlpatterns += swagger_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
