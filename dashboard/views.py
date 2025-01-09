from django.shortcuts import render
import paho.mqtt.client as mqtt 

from .forms import formsOpsiPerangkat
from .models import opsiPerangkat, sensorTanaman

def dashboard(request):
    if request.method == 'POST':
        print(request.POST)
        form = formsOpsiPerangkat(request.POST, instance=opsiPerangkat.objects.get(id=1))
        if form.is_valid():
            form.save()
            print("Data berhasil disimpan:", form.cleaned_data)
        else:
            print("Form tidak valid:", form.errors)
            
    
    context = {
        'title': 'Dashboard',
        'opsiPerangkat': formsOpsiPerangkat(instance=opsiPerangkat.objects.get(id=1)),
        'sensor': sensorTanaman.objects.values_list('nama', flat=True)
    }
    


    return render(request, 'dashboard/dashboard.html', context)
