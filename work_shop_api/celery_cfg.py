import os

from django.apps import AppConfig, apps

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'work_shop_api.settings')

app = Celery('work_shop_api')

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


class CeleryAppConfig(AppConfig):
    name = 'tasks'
    verbose_name = 'Celery Config'

    def ready(self):
        installed_apps = [app_config.name for app_config in apps.get_app_configs()]
        app.autodiscover_tasks(lambda: installed_apps, force=True)

