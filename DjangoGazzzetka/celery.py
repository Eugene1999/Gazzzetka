from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установите переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoGazzzetka')

app = Celery('DjangoGazzzetka')

# Загрузите настройки из конфигурационного файла Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживайте задачи в файлах tasks.py
app.autodiscover_tasks()