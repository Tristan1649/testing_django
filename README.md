Документация по построению системы для обучения

1. Построение архитектуры

1.1. Создание сущности продукта
Создана сущность "Product" с полями:

creator (ForeignKey на пользователя-создателя)
name (название продукта)
start_date (дата и время начала продукта)
cost (стоимость продукта)

1.2. Определение доступа к продукту
Механизм определения доступа реализован через создание групп пользователей.

1.3. Создание сущности урока
Создана сущность "Lesson" с полями:

name (название урока)
video_link (ссылка на видео)
product (ForeignKey на продукт)

1.4. Создание сущности группы
Создана сущность "Group" с полями:

product (ForeignKey на продукт)
name (название группы)
min_users (минимальное количество участников)
max_users (максимальное количество участников)

2. Написание запросов и реализация логики распределения

2.1. Распределение пользователя в группы при доступе к продукту
Реализован алгоритм распределения, добавляющий пользователя в группу, учитывая минимальное и максимальное количество участников. Если продукт еще не начался, происходит пересборка групп для равномерного распределения.

2.2. API для списка продуктов
Реализован API, возвращающий список продуктов с основной информацией и количеством уроков, принадлежащих каждому продукту.

2.3. API для списка уроков по конкретному продукту
Реализован API, возвращающий список уроков по конкретному продукту, к которому у пользователя есть доступ.

3. Результат выполнения
Построена архитектура на базе данных SQLite с использованием Django.
Реализованы API на базе готовой архитектуры.
