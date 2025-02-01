from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('pengaturan/', views.pengaturan, name='pengaturan'),
    path('waktu/<int:id>/', views.hapusDataWaktu, name='hapusWaktu'),
    path('getSensorData/<int:id>/<str:time>/', views.getSensorData, name='sensorData'),
]



app_name = 'dashboard'