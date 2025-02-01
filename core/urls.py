from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('profile/', include('profileUser.urls' , namespace='profile')),
    path('', include('dashboard.urls', namespace='dashboard')),
]

