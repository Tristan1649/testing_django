# appless/urls.py

from django.urls import path
from .views import ProductListAPIView, LessonListAPIView, ProductAccessAPIView

urlpatterns = [
    path('products/',ProductListAPIView.as_view(), name='product-list'),
    path('lessons/',LessonListAPIView.as_view(), name='lesson-list'),
    path('product/<int:pk>/access/', ProductAccessAPIView.as_view(), name='product-access'),
    # Добавьте другие маршруты, если необходимо
]
