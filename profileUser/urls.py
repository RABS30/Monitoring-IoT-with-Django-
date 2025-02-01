from django.urls import path

from . import views
urlpatterns = [
    path('', views.profile, name='profile'),
]

app_name = 'profile'
