from django.urls import include, path
from .views import ProtectedView, telegramWebhook, login_view

# JWT Token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('webhook/', telegramWebhook.as_view(), name='telegramWebhook'),
    # JWT Token
    path('token/', TokenObtainPairView.as_view(), name='tokenObtainPair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='tokenRefresh'),
    
    path('login/', login_view, name='loginTelegram'),
    path('verification/', ProtectedView.as_view(), name='verification'),
    
    
]


