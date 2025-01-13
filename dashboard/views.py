from django.shortcuts import redirect, render

from .forms import formBerdasarkanWaktu, formBerdasarkanSensor, formOpsiPerangkat
from .models import jenisPenyiraman, opsiPerangkat, berdasarkanSensor, berdasarkanWaktu

def dashboard(request):
    # Method GET

    # opsi jenis penyiraman saat ini
    opsi = opsiPerangkat.objects.first()    
    # Daftar Waktu saat ini
    daftarWaktu  = berdasarkanWaktu.objects.values_list('waktu', flat=True)
    # Daftar Sensor saat ini
    daftarSensor = berdasarkanSensor.objects.first()


    # Method POST
    if request.method == 'POST' :
        print(request.POST)

        # Ambil data Jenis Penyiraman dari request
        idJenisPenyiraman       = request.POST['jenisPenyiraman']
        opsiPerangkatSaatIni    = opsiPerangkat.objects.get(id=opsiPerangkat.objects.values_list('id', flat=True)[0])
        jenisPenyiramanUpdate   = jenisPenyiraman.objects.get(id=idJenisPenyiraman)
        
  
        # jenis Penyiraman == Manual
        if (jenisPenyiramanUpdate.nama == 'Manual') :
            formUpdate = formOpsiPerangkat(request.POST or None, instance=opsi)
            if formUpdate.is_valid():
                formUpdate.save()

        # jenis Penyiraman == Berdasarkan Waktu
        elif (jenisPenyiramanUpdate.nama == 'Berdasarkan Waktu'):
            jumlahWaktu = berdasarkanWaktu.objects.all().__len__()
            formUpdate = formOpsiPerangkat(request.POST or None, instance=opsi)
            if formUpdate.is_valid():
                formUpdate.save() 
                
            formBerdasarkanWaktuUpdate = formBerdasarkanWaktu(request.POST)
            if formBerdasarkanWaktuUpdate.is_valid() and request.POST.get('waktu') != '' and jumlahWaktu < 4:
                print('Ini waktu : ', request.POST.get('waktu'))
                print(f'Ini juga waktu : {"waktu" in request.POST}')
                formBerdasarkanWaktuUpdate.save()
            else :
                print('Ini waktu : ', request.POST.get('waktu'))
                print(f'Ini juga waktu : {"waktu" in request.POST}')
                print(formBerdasarkanWaktuUpdate.errors)
            
        # jenis Penyiraman == Berdasarkan Sensor
        elif (jenisPenyiramanUpdate.nama == 'Berdasarkan Sensor'):
            formUpdate = formOpsiPerangkat(request.POST or None, instance=opsi)
            if formUpdate.is_valid():
                formUpdate.save()
            
            formBerdasarkanSensorUpdate = formBerdasarkanSensor(request.POST or None, instance=daftarSensor)
            if formBerdasarkanSensorUpdate.is_valid():
                print('Data Valid Sensor Valid')
                formBerdasarkanSensorUpdate.save()
            else :
                print(formBerdasarkanSensorUpdate.errors)
                                 
        return redirect('dashboard:dashboard')
        

    
    context = {
        'title': 'Dashboard',
        'form': formOpsiPerangkat(request.POST or None, instance=opsi),
        'formBerdasarkanWaktu': formBerdasarkanWaktu,
        'formBerdasarkanSensor' : formBerdasarkanSensor(request.POST or None, instance=daftarSensor),
        'daftarWaktu': daftarWaktu,
    }
    return render(request, 'dashboard/dashboard.html', context)






