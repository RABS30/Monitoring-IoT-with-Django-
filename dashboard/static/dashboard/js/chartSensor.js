class createChart{
    createdChart = null;
    constructor(elementId, 
        typeChart='bar',
        labels= ['Chart'], 
        datasets= [{
            label: 'Chart',
            data: [50],
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 0.2)',
            borderWidth: 1
        }], 
        scales={
        y: {
            beginAtZero: true,
            min: 0,
            max: 100,
        }
    }) {
    this.elementId = elementId;
    this.typeChart = typeChart;
    this.labels = labels;
    this.datasets = datasets;
    this.scales = scales;
    this.createdChart = this.#create()
    }

    #create(){
        return new Chart(document.getElementById(elementId).getContext('2d'), {
            type: this.typeChart,
            data: {
                labels: this.labels, 
                datasets: this.datasets
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales:this.scales,
            },
        })
    }

    update = (value) => {
        if(this.typeChart === 'bar'){
            this.createdChart.data.datasets[0].data             = [value];
            this.createdChart.data.datasets[0].backgroundColor  = [value >= 60 ? 'rgba(75, 192, 192, 0.2)' : 'rgba(255, 99, 132, 0.2)'], 
            this.createdChart.data.datasets[0].borderColor      = [value >= 60 ? 'rgba(255, 99, 132, 1)' : 'rgba(75, 192, 192, 1)'],
            this.createdChart.data.labels  = [`${this.labels[0]} = ${value}`];
            this.createdChart.update();
        }else if(this.typeChart === 'doughnut'){
            this.createdChart.data.datasets[0].data = [value, 14-value];
            this.createdChart.data.labels  = [`${this.labels[0]} = ${value}`];
            this.createdChart.update();
        }
    };
}

// variable chart
var elementId ;
var typeChart ; 
var labels;
var datasets;
var scales;

// Sensor Kelembapan Tanah
const kelembapanTanah = new createChart(elementId = 'sensorKelembapan', 'bar', ['Kelembapan'], [{
    label: 'Kelembapan Tanah',
    data: [0],
    backgroundColor: [14 >= 7 ? 'rgba(75, 192, 192, 0.2)' : 'rgba(255, 99, 132, 0.2)'], 
    borderColor: [14 >= 7 ? 'rgba(255, 99, 132, 1)'  : 'rgba(75, 192, 192, 1)'], 
    borderWidth: 1}], {
    y: {
        beginAtZero: true,
        min: 0,
        max: 100
    },
});


// Sensor Suhu Tanah
const suhuTanah = new createChart(elementId = 'sensorSuhuTanah', 'bar', ['Suhu Tanah'], [{
    label: 'Sensor Suhu Tanah',
    data: [0],
    backgroundColor: [14 >= 7 ? 'rgba(75, 192, 192, 0.2)' : 'rgba(255, 99, 132, 0.2)'], 
    borderColor: [14 >= 7 ? 'rgba(255, 99, 132, 1)'  : 'rgba(75, 192, 192, 1)'], 
    borderWidth: 1
    }], 
    {
        y: {
            beginAtZero: true,
            min: 0,
            max: 100
        }
}); 

// Sensor Ph
const sensorPh = new createChart(elementId='sensorPh', 'doughnut', ['Ph'], [{
    label: 'Sensor Ph',
    data: [0, 14-0],
    backgroundColor: [ 'rgba(75, 192, 192, 0.2)', 'rgba(255, 99, 132, 0.2)',], 
    borderColor: ['rgba(255, 99, 132, 1)', 'rgba(75, 192, 192, 1)',], 
    borderWidth: 1
    }],
    {
    y: {
            beginAtZero: true,
            min: 0,
            max: 14,
        }}
);


// Sensor Nutrisi Tanah
const sensorNutrisiTanah = new createChart(elementId='sensorNutrisiTanah', 'doughnut', ['Nutrisi Tanah'], [{
    label: 'Sensor Nutrisi Tanah',
    data: [0, 14-0],
    backgroundColor: [ 'rgba(75, 192, 192, 0.2)', 'rgba(255, 99, 132, 0.2)',], 
    borderColor: ['rgba(255, 99, 132, 1)', 'rgba(75, 192, 192, 1)',], 
    borderWidth: 1
    }],
    {
        y:{
            beginAtZero: true,
            min: 0,
            max: 100,
        }
    },
);

// Sensor Nutrisi Tanah
const sensorCahaya = new createChart(elementId='sensorCahaya', 'bar', ['Intensitas Cahaya'], [{
    label: 'Instensitas Cahaya',
    data: [0],
    backgroundColor: [ 'rgba(75, 192, 192, 0.2)'], 
    borderColor: ['rgba(255, 99, 132, 1)'], 
    borderWidth: 1
    }],
    {
        y:{
            beginAtZero: true,
            min: 0,
            max: 100,
        }
    },
);

// MQTT Connect
const client = mqtt.connect("wss://broker.emqx.io:8084/mqtt");

// Function saat berhasil terhubung dan subscribe topic
client.on('connect', () => {
    console.log('Berhasil terhubung ke MQTT');
    client.subscribe('sensor/tanaman', (err) => {
        if(!err){
            console.log('Berhasil subscribe ke topic sensor/tanaman');
        };
    })
})



// Function saat menerima data
client.on('message', (topic, message) => {
    try {
        message = JSON.parse(message);
        if(message['kelembapanTanah']){
            kelembapanTanah.update(message['kelembapanTanah']);
        }
        if(message['suhuTanah']){
            suhuTanah.update(message['suhuTanah']);
        }    
        if(message['Ph']){
            sensorPh.update(message['Ph']);
        }
        if(message['nutrisiTanah']){
            sensorNutrisiTanah.update(message['nutrisiTanah']);
        }
        if(message['kelembapanTanah']){
            sensorCahaya.update(message['kelembapanTanah']);
        if(message['volumeTangki']){
            document.getElementById('volumeTangki').textContent = message['volumeTangki'];
        }
        }if(message['penyiramanBerhasil']){   
            clearClickButton(batasWaktuPenyiraman, 'siram', 'click', 'Siram', 10000, 'sensor/tanaman2', "Siram Tanaman")
        }if(message['pengisianAirBerhasil']){
            clearClickButton(batasWaktuPenyiraman, 'isiAir', 'click', 'Isi Air', 10000, 'sensor/tanaman2', "Isi Tangki Air")
        }
    }catch(err){
        console.log(message)
    }
});





// ===== Mengaktifkan fungsi button ===== //
function clickButton(id, type, message, time, topic){
    var button           = document.getElementById(id)   // Tag Button
    var childButton      = button.cloneNode(true)        // Clone Child Element dari Button
    var disabledButton   = false;                        // Button tidak dapat diaktifkan

    // Ubah ChildButton menjadi loading saat proses berjalan
    var loading = `
        <div class="flex items-center justify-center w-56 h-56 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-800 dark:border-gray-700">
        <div class="px-3 py-1 text-sm font-medium leading-none text-center text-blue-800 bg-blue-200 rounded-full animate-pulse dark:bg-blue-900 dark:text-blue-200">loading...</div>
        </div>
    `   
    
    // Saat button di click
    button.addEventListener(type, ()=> {
        // Jika disabledButton False, maka jalankan function
        if(!disabledButton){
            // Button tidak dapat diaktifkan 
            disabledButton = true; 

            // Data yang ingin di kirim
            var jsonMessage = {
                "message" : message
            }
            jsonMessage = JSON.stringify(jsonMessage)

            // Kirim data ke MQTT
            client.publish(topic, jsonMessage, (err) => {
                if(err){
                    disabledButton = false; // Button dapat di click
                }else{
                    // Ganti ChildButton menjadi loading
                    button.replaceChildren();
                    button.innerHTML = loading;

                    // Menunggu konfirmasi dari MQTT selama waktu yang ditentukan
                    batasWaktuPenyiraman = setTimeout(()=> {
                        // Ubah child Button dari loading kesebelumnya
                        button.replaceChildren(childButton);    
                        // Button dapat di click
                        disabledButton = false; 
                    }, time)
                }
            })
        }
    })

}

function clearClickButton(batasWaktu, id, type, message, time, topic, textContent){
    var button = document.getElementById(id);
    var buttonTag = `<button type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">${textContent}</button>`

    if(batasWaktu){
        clearTimeout(batasWaktu);
        button.innerHTML = buttonTag;
    }
    clickButton(id, type, message, time, topic)
}

var batasWaktuPenyiraman;
var batasWaktuPengisianAir;
var batasWaktuBeriPupuk ;

clickButton('siram', 'click', 'Siram', 10000, 'sensor/tanaman2')
clickButton('isiAir', 'click', 'Isi Air', 10000, 'sensor/tanaman2')
clickButton('beriPupuk', 'click', 'beriPupuk', 10000, 'sensor/tanaman2')
