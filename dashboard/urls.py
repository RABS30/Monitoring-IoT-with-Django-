from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('waktu/<int:id>/', views.hapusDataWaktu, name='hapusWaktu'),
    path('getSensorData/<int:id>/<str:time>/', views.getSensorData, name='sensorData'),
]



app_name = 'dashboard'