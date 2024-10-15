#Django
from django.apps import AppConfig


class EventAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'events'
    verbose_name = 'Events'
