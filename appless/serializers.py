from rest_framework import serializers
from .models import Product, Lesson

class ProductSerializer(serializers.ModelSerializer):
    # Сериализатор для продукта
    class Meta:
        model = Product
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    # Сериализатор для урока
    class Meta:
        model = Lesson
        fields = '__all__'
