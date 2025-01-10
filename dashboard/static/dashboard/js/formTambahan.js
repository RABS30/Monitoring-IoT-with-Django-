var jenisPenyiraman     = document.getElementById('jenisPenyiraman')
var manual              = document.getElementById('manual');
var aturWaktu           = document.getElementById('aturWaktu');
var sensorPenyiraman    = document.getElementById('pilihSensorPenyiraman');

if (jenisPenyiraman.value == 'manual'){
    manual.classList.remove('hidden');
}else if(jenisPenyiraman.value == 'aturWaktu'){
    aturWaktu.classList.remove('hidden');
}else if(jenisPenyiraman.value == 'berdasarkanSensor'){
    sensorPenyiraman.classList.remove('hidden');
}


jenisPenyiraman.addEventListener('change', () =>{
    manual.classList.add('hidden');
    aturWaktu.classList.add('hidden');
    sensorPenyiraman.classList.add('hidden');
    

    if(jenisPenyiraman.value == 'manual'){
        manual.classList.remove('hidden');

    }else if(jenisPenyiraman.value == 'aturWaktu'){
        aturWaktu.classList.remove('hidden');

    }else if(jenisPenyiraman.value == 'berdasarkanSensor'){
        sensorPenyiraman.classList.remove('hidden');
    }   
})
