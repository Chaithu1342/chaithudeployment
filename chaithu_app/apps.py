from django.apps import AppConfig


class ChaithuAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chaithu_app'
# apps.py
from django.apps import AppConfig

class ChaithuAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chaithu_app'

    def ready(self):
        import chaithu_app.signals
