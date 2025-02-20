// Jenis Penyiraman
var jenisPenyiraman     = document.getElementById('jenisPenyiraman');
var manual              = document.getElementById('Manual');
var sensorPenyiraman    = document.getElementById('Berdasarkan Sensor');
var daftarWaktu         = document.getElementById('daftarWaktu');
var daftarWaktu         = document.getElementById('daftarWaktu');

var inputWaktu          = document.getElementById('Berdasarkan Waktu');
var informasiWaktu      = document.getElementById('informasiWaktu')
// Tag untuk hapus waktu
var hapusWaktu          = document.getElementsByName('hapusWaktu');


/* ``` ===== Menampilkan Daftar Jenis Penyiraman ===== ``` */
    // Aktif saat pertama kali menampilkan Template
if (jenisPenyiraman.options[jenisPenyiraman.selectedIndex].text == 'Manual'){
    manual.classList.remove('hidden');

}else if(jenisPenyiraman.options[jenisPenyiraman.selectedIndex].text == 'Berdasarkan Sensor'){
    sensorPenyiraman.classList.remove('hidden');
}
   // Aktif saat ada perubahan di bagian jenis penyiraman
jenisPenyiraman.addEventListener('change', () =>{
    manual.classList.add('hidden');
    sensorPenyiraman.classList.add('hidden');


    if(jenisPenyiraman.options[jenisPenyiraman.selectedIndex].text == 'Manual'){
        manual.classList.remove('hidden');
        
        if (inputWaktu){
            inputWaktu.classList.add('hidden');
        }

        if (informasiWaktu){
            informasiWaktu.classList.add('hidden');
        }

        daftarWaktu.classList.remove('grid');
        daftarWaktu.classList.add('hidden');

    }else if(jenisPenyiraman.options[jenisPenyiraman.selectedIndex].text == 'Berdasarkan Sensor'){
        sensorPenyiraman.classList.remove('hidden');
        
        if (inputWaktu){
            inputWaktu.classList.add('hidden');
        }

        if (informasiWaktu){
            informasiWaktu.classList.add('hidden');
        }
        
        daftarWaktu.classList.remove('grid');
        daftarWaktu.classList.add('hidden'); 

    }else{
        if (inputWaktu){
            inputWaktu.classList.remove('hidden');
        }
        
        if (informasiWaktu){
            informasiWaktu.classList.add('hidden');
        }

        daftarWaktu.classList.add('grid');
        daftarWaktu.classList.remove('hidden'); 

    }
})



/* ``` ===== Menonaktifkan fitur Hapus Waktu saat tidak memilih berdasarkan waktu ===== ``` */
if (jenisPenyiraman.options[jenisPenyiraman.selectedIndex].text != 'Berdasarkan Waktu'){
    hapusWaktu.forEach((a, index) => {
        a.href = "javascript:void(0);"
    })
}


/* ``` ===== Konfirmasi perubahan Opsi perangkat ===== ``` */
    // Konfirmasi perubahan 
var submitOpsi = document.getElementById('submitOpsi');

submitOpsi.addEventListener('click', (event) => {
    if(!confirm("Apakah anda yakin ingin mengubah Opsi ? ")){
        event.preventDefault();
        console.log('Hello');
    };
});


