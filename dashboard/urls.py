from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('waktu/<int:id>/', views.hapusDataWaktu, name='hapusWaktu'),
    path('get_sensor_data/', views.get_sensor_data, name='sensorData'),
]



app_name = 'dashboard'