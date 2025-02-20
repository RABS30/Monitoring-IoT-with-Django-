from django.urls import re_path
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/socket-server/", consumers.ChatConsumer.as_asgi())
]