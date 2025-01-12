from django.shortcuts import redirect, render

from .forms import formBerdasarkanWaktu, formBerdasarkanSensor, formOpsiPerangkat
from .models import jenisPenyiraman, opsiPerangkat, berdasarkanSensor, berdasarkanWaktu

def dashboard(request):
    # Method POST
    if request.method == 'POST' :
        print(request.POST)

        # Ambil data Jenis Penyiraman dari request
        idJenisPenyiraman       = request.POST['jenisPenyiraman']
        opsiPerangkatSaatIni    = opsiPerangkat.objects.get(id=opsiPerangkat.objects.values_list('id', flat=True)[0])
        jenisPenyiramanUpdate   = jenisPenyiraman.objects.get(id=idJenisPenyiraman)
        
  
        # Bandingkan dengan jenis penyiraman yang ada di opsi perangkat
        if opsiPerangkatSaatIni.jenisPenyiraman.pk != jenisPenyiramanUpdate.pk : 
            print('berbeda : ',jenisPenyiramanUpdate)

            # jenis Penyiraman == Manual
            if (jenisPenyiramanUpdate.nama == 'Manual') :
                opsiPerangkatSaatIni.jenisPenyiraman = jenisPenyiramanUpdate
                opsiPerangkatSaatIni.save()
                
            elif (jenisPenyiramanUpdate.nama == 'Berdasarkan Waktu'):
                daftarWaktu = berdasarkanWaktu.objects.all()
                opsiPerangkatSaatIni.jenisPenyiraman = jenisPenyiramanUpdate
                opsiPerangkatSaatIni.save()
                
            elif (jenisPenyiramanUpdate.nama == 'Berdasarkan Sensor'):
                daftarWaktu = berdasarkanSensor.objects.all()
                opsiPerangkatSaatIni.jenisPenyiraman = jenisPenyiramanUpdate
                opsiPerangkatSaatIni.save()
                                 
        return redirect('dashboard:dashboard')
        
    # Method GET

    # opsi jenis penyiraman saat ini
    idOpsiPerangkat = opsiPerangkat.objects.values_list('id', flat=True)[0]
    opsi = opsiPerangkat.objects.get(id=idOpsiPerangkat)
    
    # Daftar Waktu saat ini
    daftarWaktu = berdasarkanWaktu.objects.values_list('waktu', flat=True)
    # Daftar Sensor saat ini
    daftarWaktu = berdasarkanSensor.objects.first()

    
    context = {
        'title': 'Dashboard',
        'form': formOpsiPerangkat(request.POST or None, instance=opsi),
        'formBerdasarkanWaktu': formBerdasarkanWaktu,
        'formBerdasarkanSensor' : formBerdasarkanSensor(request.POST or None, instance=daftarWaktu),
        'daftarWaktu': daftarWaktu,
    }
    return render(request, 'dashboard/dashboard.html', context)
