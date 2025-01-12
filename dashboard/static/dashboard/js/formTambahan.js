var jenisPenyiraman     = document.getElementById('jenisPenyiraman')
var manual              = document.getElementById('Manual');
var aturWaktu           = document.getElementById('Berdasarkan Waktu');
var sensorPenyiraman    = document.getElementById('Berdasarkan Sensor');




if (jenisPenyiraman.options[jenisPenyiraman.selectedIndex].text == 'Manual'){
    manual.classList.remove('hidden');
}else if(jenisPenyiraman.options[jenisPenyiraman.selectedIndex].text == 'Berdasarkan Waktu'){
    aturWaktu.classList.remove('hidden');
}else if(jenisPenyiraman.options[jenisPenyiraman.selectedIndex].text == 'Berdasarkan Sensor'){
    sensorPenyiraman.classList.remove('hidden');
}

jenisPenyiraman.addEventListener('change', () =>{
    manual.classList.add('hidden');
    aturWaktu.classList.add('hidden');
    sensorPenyiraman.classList.add('hidden');
    
    console.log(`Ini adalah opsi ${jenisPenyiraman.options[jenisPenyiraman.selectedIndex].text}`)

    if(jenisPenyiraman.options[jenisPenyiraman.selectedIndex].text == 'Manual'){
        manual.classList.remove('hidden');

    }else if(jenisPenyiraman.options[jenisPenyiraman.selectedIndex].text == 'Berdasarkan Waktu'){
        aturWaktu.classList.remove('hidden');

    }else if(jenisPenyiraman.options[jenisPenyiraman.selectedIndex].text == 'Berdasarkan Sensor'){
        sensorPenyiraman.classList.remove('hidden');
    }   
})
