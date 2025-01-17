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
        }
    }catch(err){
        console.log(message)
    }
});


// Function untuk mengirim data 

var loading = `                                    
<div class="flex items-center justify-center w-56 h-56 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-800 dark:border-gray-700">
<div class="px-3 py-1 text-sm font-medium leading-none text-center text-blue-800 bg-blue-200 rounded-full animate-pulse dark:bg-blue-900 dark:text-blue-200">loading...</div>
</div>
`

    // Jika Siram di click
    var siram           = document.getElementById('siram')
    var childSiram      = siram.cloneNode(true)
    var disabledSiram   = false;

    siram.addEventListener('click', (event) => {
        if(!disabledSiram){
            disabledSiram = true;

            // Data yang akan dikirim
            const message = {
                'message' : 'Siram'
            }

            const jsonMessage = JSON.stringify(message)

            // Mengirim data 
            client.publish('sensor/tanaman2', jsonMessage, (err) => {
                if (err) {
                    console.log('Gagal mengirim data');
                    disabledSiram = false;
                }else{
                    siram.replaceChildren()
                    siram.innerHTML = loading
                    console.log('Berhasil mengirim data');

                    setTimeout(() => {
                        siram.replaceChildren(childSiram);
                        disabledSiram = false;    
                    }, 4000);                    
                }
            })
        }

    })



    // Jika Isi Air di click
    var isiAir          = document.getElementById('isiAir')
    var childIsiAir     = isiAir.cloneNode(true)
    var disabledIsiAir  = false;

    isiAir.addEventListener('click', (event) => {
        if(!disabledIsiAir){
            disabledIsiAir = true;

            // Data yang akan dikirim
            const message = {
                'message' : 'Isi Air'
            }

            const jsonMessage = JSON.stringify(message)

            // Mengirim data 
            client.publish('sensor/tanaman2', jsonMessage, (err) => {
                if (err) {
                    console.log('Gagal mengirim data');
                    disabledIsiAir = false;
                }else{
                    isiAir.replaceChildren()
                    isiAir.innerHTML = loading
                    console.log('Berhasil mengirim data');

                    setTimeout(() => {
                        isiAir.replaceChildren(childIsiAir);
                        disabledIsiAir = false;    
                    }, 4000);                    
                }
            })
        }

    })