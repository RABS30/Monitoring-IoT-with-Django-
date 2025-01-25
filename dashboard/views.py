from datetime import date, datetime
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Avg
from django.db.models.functions import TruncMinute

from .forms import (formBerdasarkanWaktu, 
                    formBerdasarkanSensor, 
                    formOpsiPerangkat)

from .models import (jenisPenyiraman, nilaiSensor, 
                     opsiPerangkat, 
                     berdasarkanSensor, 
                     berdasarkanWaktu, 
                     penyiramanTerakhir, 
                     pemberianPupukTerakhir, 
                     tanggalTanaman)

def dashboard(request):  
    # Method GET
    ''' ====== SIAPKAN FORM UNTUK TEMPLATE ====== '''
    # Form Opsi Perangkat 
    opsi            = opsiPerangkat.objects.first()    
    # Daftar Waktu yang tersedia
    daftarWaktu     = berdasarkanWaktu.objects.all()
    # Daftar Sensor yang tersedia
    daftarSensor    = berdasarkanSensor.objects.first()
    # Penyiraman Terakhir
    penyiraman      = penyiramanTerakhir.objects.first()
    # Pemberian Pupuk Terakhir
    pemberianPupuk  = pemberianPupukTerakhir.objects.first()
    # Tanggal Penanaman
    tanggalPenanaman = tanggalTanaman.objects.first()


    # Method POST
    if request.method == 'POST' :
        print(request.POST)
        ''' ===== UPDATE DATA OPSI PERANGKAT ===== '''
        # Update Opsi Perangkat 
        formUpdate = formOpsiPerangkat(request.POST or None, instance=opsi)
        if formUpdate.is_valid():
            formUpdate.save()
            
        # Update Jenis Penyiraman
        idJenisPenyiraman       = request.POST['jenisPenyiraman']
        opsiPerangkatSaatIni    = opsiPerangkat.objects.first()
        jenisPenyiramanUpdate   = jenisPenyiraman.objects.get(id=idJenisPenyiraman)
        
        # Update jenis Penyiraman => Berdasarkan Waktu
        if (jenisPenyiramanUpdate.nama == 'Berdasarkan Waktu'):
            # Jumlah waktu yang ada di database
            jumlahWaktu = berdasarkanWaktu.objects.all().__len__() 
            
            # Masukkan data input waktu ke form dari request.POST
            formBerdasarkanWaktuUpdate = formBerdasarkanWaktu(request.POST)
            
            # Validasi, jika data valid dan jumlah kurang dari 4 maka simpan data tersebut
            if formBerdasarkanWaktuUpdate.is_valid() and request.POST.get('waktu') != '' and jumlahWaktu < 4:
                formBerdasarkanWaktuUpdate.save()
            else :
                print(formBerdasarkanWaktuUpdate.errors)
                
        # Update jenis Penyiraman => Berdasarkan Sensor
        elif (jenisPenyiramanUpdate.nama == 'Berdasarkan Sensor'):
            # Masukkan data input sensor dari request.POST 
            formBerdasarkanSensorUpdate = formBerdasarkanSensor(request.POST or None, instance=daftarSensor)
            # Validasi, jika data valid maka simpan data tersebut
            if formBerdasarkanSensorUpdate.is_valid():
                print('Data Valid Sensor Valid')
                formBerdasarkanSensorUpdate.save()
            else :
                print(formBerdasarkanSensorUpdate.errors)
                
                
        # redirect ke dashboard
        return redirect('dashboard:dashboard')
        
    context = {
        'title': 'Dashboard',
        'form': formOpsiPerangkat(request.POST or None, instance=opsi),
        'formBerdasarkanWaktu': formBerdasarkanWaktu,
        'formBerdasarkanSensor' : formBerdasarkanSensor(request.POST or None, instance=daftarSensor),
        'daftarWaktu': daftarWaktu,
        'penyiramanTerakhir': penyiraman,
        'pemberianPupukTerakhir': pemberianPupuk,
        'tanggalPenanaman': tanggalPenanaman,
        'usiaTanaman' : tanggalPenanaman.tanggal.strftime("%Y-%m-%d") #type:ignore
    }
    return render(request, 'dashboard/dashboard.html', context)


def hapusDataWaktu(request, id):
    print('Hallo')
    try :
        waktu = berdasarkanWaktu.objects.get(id=id)
        waktu.delete()
        print('Berhasil hapus')
    except Exception as message:
        print(f'error : {message}')
    return redirect(('dashboard:dashboard'))


def get_sensor_data(request):
    nowaday = timezone.now() - timezone.timedelta(hours=timezone.now().hour, 
                                              minutes=timezone.now().minute, 
                                              seconds=timezone.now().second) + timezone.timedelta(days=1) - timezone.timedelta(hours=7)
    dataSensor = nilaiSensor.objects.filter(sensor_id=110, 
                                            waktu__gte=nowaday).order_by('-waktu')

    
    
    dataSensor = dataSensor.annotate(minute=TruncMinute('waktu')).values('minute').annotate(avg_value=Avg('nilai'))


    response = { 
                'waktu': [entry['minute'].strftime('%d-%m-%Y %H:%M') for entry in dataSensor], 
                'nilai': [int(entry['avg_value']) for entry in dataSensor]
                }
    return JsonResponse(response, safe=False)

