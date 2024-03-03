# djangless/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('appless.urls')),
    # Добавьте другие URL-маршруты, если необходимо
]
