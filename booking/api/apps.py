from django.apps import AppConfig


class HotelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'


    def ready(self):
        import api.signals
