from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.utils import timezone
from .models import Product, Lesson, Group, UserGroup
from .serializers import ProductSerializer, LessonSerializer

class ProductListAPIView(generics.ListAPIView):
    # API-представление для списка продуктов
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class LessonListAPIView(generics.ListAPIView):
    # API-представление для списка уроков по продукту
    serializer_class = LessonSerializer

    def get_queryset(self):
        # Получение доступных продуктов для пользователя
        user = self.request.user
        accessible_products = Product.objects.filter(start_date__lte=timezone.now()) # Replace with your actual filter
        return Lesson.objects.filter(product__in=accessible_products)
class ProductAccessAPIView(APIView):
    # API-представление для предоставления доступа к продукту и распределения пользователя в группы
    def post(self, request, pk):  # Добавлен аргумент pk
        user = request.user
        product = Product.objects.get(id=pk)

        # Проверка, что продукт еще не начался
        if product.start_date > timezone.now():
            # Пересборка групп для равномерного распределения
            self.rebalance_groups(product)

        # Попробуйте добавить пользователя в группу
        if self.add_user_to_group(product):
            return Response({"message": "Доступ предоставлен и пользователь добавлен в группу."},
                            status=status.HTTP_200_OK)
        else:
            return Response({"message": "Не удалось предоставить доступ."}, status=status.HTTP_400_BAD_REQUEST)

    def rebalance_groups(self, product):
        # Реализуйте логику пересборки групп
        # Здесь можно использовать различные алгоритмы для равномерного распределения
        pass

    def add_user_to_group(self, product):
        groups = Group.objects.filter(product=product).order_by('min_users', 'max_users')
        for group in groups:
            user_count = UserGroup.objects.filter(group=group).count()
            if group.min_users <= user_count < group.max_users:
                UserGroup.objects.create(user=user, group=group)
                return True
        return False
