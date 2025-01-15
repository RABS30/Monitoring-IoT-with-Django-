from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('waktu/<int:id>/', views.hapusDataWaktu, name='hapusWaktu'),
]



app_name = 'dashboard'