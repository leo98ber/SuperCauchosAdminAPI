#Django
from django.apps import AppConfig


class ClientAppConfig(AppConfig):
    """Users app config."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clients'
    verbose_name = 'Clients'
