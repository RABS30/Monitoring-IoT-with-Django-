from django.urls import include, path
from .views import telegramWebhook



urlpatterns = [
    path('webhook/', telegramWebhook.as_view(), name='telegramWebhook'),
]



