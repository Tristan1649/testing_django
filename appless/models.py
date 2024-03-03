from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    # Модель для представления продукта
    creator = models.ForeignKey(User, on_delete=models.CASCADE)  # Создатель продукта
    name = models.CharField(max_length=255)  # Название продукта
    start_date = models.DateTimeField()  # Дата и время начала продукта
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Стоимость продукта

class Lesson(models.Model):
    # Модель для представления урока
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Продукт, к которому принадлежит урок
    title = models.CharField(max_length=255)  # Название урока
    video_link = models.URLField()  # Ссылка на видео

class Group(models.Model):
    # Модель для представления группы пользователей
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Продукт, к которому принадлежит группа
    name = models.CharField(max_length=255)  # Название группы
    min_users = models.PositiveIntegerField()  # Минимальное количество участников в группе
    max_users = models.PositiveIntegerField()  # Максимальное количество участников в группе

class UserGroup(models.Model):
    # Модель для отображения связи между пользователем и группой
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь
    group = models.ForeignKey(Group, on_delete=models.CASCADE)  # Группа, к которой принадлежит пользователь
