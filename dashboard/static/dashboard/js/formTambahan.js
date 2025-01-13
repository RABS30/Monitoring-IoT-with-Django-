var jenisPenyiraman     = document.getElementById('jenisPenyiraman')
var manual              = document.getElementById('Manual');
var aturWaktu           = document.getElementById('Berdasarkan Waktu');
var sensorPenyiraman    = document.getElementById('Berdasarkan Sensor');
var daftarWaktu         = document.getElementById('daftarWaktu');
var siramAir            = document.getElementById('siram')


// Aktif saat HTML dipanggil pertama kali
if (jenisPenyiraman.options[jenisPenyiraman.selectedIndex].text == 'Manual'){
    manual.classList.remove('hidden');
    siramAir.classList.remove('hidden');
}else if(jenisPenyiraman.options[jenisPenyiraman.selectedIndex].text == 'Berdasarkan Waktu'){
    if(daftarWaktu.childElementCount == 4){
        var ganti = document.createElement('div')
        ganti.textContent = 'Pengaturan waktu sudah mencapai maksimal. Hapus waktu yang tersedia jika ingin menambahkan'
        ganti.className ='text-white mt-5'
        aturWaktu.replaceChildren(ganti)
        aturWaktu.classList.remove('w-2/5')

    }
    
    aturWaktu.classList.remove('hidden');
    daftarWaktu.classList.remove('hidden');
    daftarWaktu.classList.add('grid');
}else if(jenisPenyiraman.options[jenisPenyiraman.selectedIndex].text == 'Berdasarkan Sensor'){
    sensorPenyiraman.classList.remove('hidden');



}

// Aktif saat ada perubahan di bagian jenis penyiraman
jenisPenyiraman.addEventListener('change', () =>{
    manual.classList.add('hidden');
    aturWaktu.classList.add('hidden');
    daftarWaktu.classList.add('hidden');
    sensorPenyiraman.classList.add('hidden');

    if(jenisPenyiraman.options[jenisPenyiraman.selectedIndex].text == 'Manual'){
        manual.classList.remove('hidden');
    }else if(jenisPenyiraman.options[jenisPenyiraman.selectedIndex].text == 'Berdasarkan Waktu'){
        if(daftarWaktu.childElementCount < 4){
            aturWaktu.classList.remove('hidden');
        }
        daftarWaktu.classList.remove('hidden');
        daftarWaktu.classList.add('grid');

    }else if(jenisPenyiraman.options[jenisPenyiraman.selectedIndex].text == 'Berdasarkan Sensor'){
        sensorPenyiraman.classList.remove('hidden');
    }   
})



var opsiPerangkat = document.getElementById('opsiPerangkat');

opsiPerangkat.addEventListener('submit', (event) => {
    if(!confirm("Konfirmasi untuk mengirim")){
        event.preventDefault();
        console.log('Hello');
    };
});