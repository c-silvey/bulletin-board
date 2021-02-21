from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('', include('my_app.urls')),
    path(os.getenv('ADMIN_URL') + '/admin/', admin.site.urls),
]

if settings.DEBUG: # denotes in DEVELOPMENT not PRODUCTION!!!
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
