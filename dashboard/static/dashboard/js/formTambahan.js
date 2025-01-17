// Jenis Penyiraman
var jenisPenyiraman     = document.getElementById('jenisPenyiraman')
var manual              = document.getElementById('Manual');
var aturWaktu           = document.getElementById('Berdasarkan Waktu');
var sensorPenyiraman    = document.getElementById('Berdasarkan Sensor');
var daftarWaktu         = document.getElementById('daftarWaktu');
// Siram Air
var siramAir            = document.getElementById('siram')

// Tag untuk hapus waktu
var hapusWaktu          = document.getElementsByName('hapusWaktu')


/* ``` ===== Menampilkan Daftar Jenis Penyiraman ===== ``` */
    // Aktif saat pertama kali menampilkan Template
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


/* ``` ===== Menampilkan tombol untuk mengisi Air =====```*/
var jenisPengisianAir = document.getElementById('jenisPengisianAir')
var isiAir = document.getElementById('isiAir')

if(jenisPengisianAir.options[jenisPengisianAir.selectedIndex].text === "Manual"){
    isiAir.classList.remove("hidden")
}