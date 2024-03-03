from django.apps import AppConfig


class ApplessConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appless'
