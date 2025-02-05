from django.contrib import admin
from django.urls import path, include

from apiData.views import sensorViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', sensorViewSet, basename='sensor')


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',            include('dashboard.urls', namespace='dashboard')),
    path('accounts/',   include('allauth.urls')),
    path('api-auth/',   include('rest_framework.urls', namespace='rest_framwork')),
    path('bot/',        include('apiData.urls')),
    path('profile/',    include('profileUser.urls' , namespace='profile')),
    path('sensor/',     include(router.urls)),
]