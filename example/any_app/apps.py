from django.apps import AppConfig


class AnyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'any_app'
