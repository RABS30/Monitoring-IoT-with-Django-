import {client} from './mqttConnect.js'


// Function saat menerima data
client.on('message', (topic, message) => {
    try {
        message = JSON.parse(message);
        if(message['penyiramanBerhasil']){   
            siramAirButton.stopTimerButton("Siram Tanaman");
            updateTime('penyiramanTerakhir')
        }
        if(message['pemberianPupukBerhasil']){
            beriPupukButton.stopTimerButton("Beri Pupuk");
            updateTime('pemberianPupukTerakhir')
        }
        if(message['pengisianAirBerhasil']){
            isiAirButton.stopTimerButton("Isi Tangki Air");
        }

    }catch(err){
        console.log(message)
    }
});

// ===== Class Click Button ===== //
class createClickButton{
    constructor(id, type, message, delay, topic){
        this.id = id;
        this.type = type;
        this.message = message;
        this.delay = delay;
        this.topic = topic;
        this.timer;
        this.button;
    }

    startClickButton(){
        this.button          = document.getElementById(this.id)   // Tag Button
        var childButton      = this.button.cloneNode(true)        // Clone Child Element dari Button
        var disabledButton   = false;                             // Button tidak dapat diaktifkan
    
        // Ubah ChildButton menjadi loading saat proses berjalan
        var loading = `
            <div class="flex items-center justify-center w-56 h-56 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-800 dark:border-gray-700">
            <div class="px-3 py-1 text-sm font-medium leading-none text-center text-blue-800 bg-blue-200 rounded-full animate-pulse dark:bg-blue-900 dark:text-blue-200">loading...</div>
            </div>
        `   
        
        // Saat button di click
        this.button.addEventListener(this.type, ()=> {
            // Jika disabledButton False, maka jalankan function
            if(!disabledButton){
                // Button tidak dapat diaktifkan 
                disabledButton = true; 
    
                // Data yang ingin di kirim
                var jsonMessage = {
                    "message" : this.message
                }
                jsonMessage = JSON.stringify(jsonMessage)
    
                // Kirim data ke MQTT
                client.publish(this.topic, jsonMessage, (err) => {
                    if(err){
                        disabledButton = false; // Button dapat di click
                    }else{
                        // Ganti ChildButton menjadi loading
                        this.button.replaceChildren();
                        this.button.innerHTML = loading;
    
                        // Menunggu konfirmasi dari MQTT selama waktu yang ditentukan
                        this.timer = setTimeout(()=> {
                            // Ubah child Button dari loading kesebelumnya
                            this.button.replaceChildren(childButton);    
                            // Button dapat di click
                            disabledButton = false; 
                        }, this.delay)
                    }
                })
            }
        })
    
    }

    stopTimerButton = (textContent) => {
        var buttonTag = `<button type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">${textContent}</button>`

        if(this.timer){
            clearTimeout(this.timer);
            this.button.innerHTML = buttonTag;
        }
        this.startClickButton()
    }
}

// ===== Mengaktifkan fungsi button ===== //
const siramAirButton    = new createClickButton('siram', 'click', 'Siram', 10000, 'sensor/tanaman2');
const isiAirButton      = new createClickButton('isiAir', 'click', 'Isi Air', 10000, 'sensor/tanaman2');
const beriPupukButton   = new createClickButton('beriPupuk', 'click', 'Beri Pupuk', 10000, 'sensor/tanaman2');

siramAirButton.startClickButton();
isiAirButton.startClickButton();
beriPupukButton.startClickButton();


/* ``` ===== Update Informasi penyiraman dan pemberian pupuk terakhir ===== */
function updateTime(id){
    var dateElement = document.getElementById(id);
    var date =formatTime(new Date());
    dateElement.textContent = `${date} WIB`

}
function formatTime(date) {
    const days = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jum'at", "Sabtu"];
    const months = [
      "Januari", "Februari", "Maret", "April", "Mei", "Juni", 
      "Juli", "Agustus", "September", "Oktober", "November", "Desember"
    ];

    const dayName = days[date.getDay()];
    const day = String(date.getDate()).padStart(2, "0");
    const monthName = months[date.getMonth()];
    const year = date.getFullYear();
    const hours = String(date.getHours()).padStart(2, "0");
    const minutes = String(date.getMinutes()).padStart(2, "0");

    return `${dayName}, ${day} ${monthName} ${year}, ${hours}:${minutes}`;
}



