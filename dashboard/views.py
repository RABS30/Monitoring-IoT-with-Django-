from django.shortcuts import render
import paho.mqtt.client as mqtt 


def dashboard(request):
    context = {
        'title': 'Dashboard',
    }
    return render(request, 'dashboard/dashboard.html', context)
