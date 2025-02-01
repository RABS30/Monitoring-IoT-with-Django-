import {client} from './mqttConnect.js'


class createChart{
    createdChart = null;

    constructor(
        elementId, 

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
        return new Chart(document.getElementById(this.elementId).getContext('2d'), {
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

    update(value, labels){
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
        }else if(this.typeChart === 'line'){
            this.createdChart.data.datasets[0].data             = value;
            this.createdChart.data.labels                       = labels;
            this.createdChart.update();
        }
    };
}

// Sensor Kelembapan Tanah
const kelembapanTanah = new createChart(
    'sensorKelembapan', 
    'bar', 
    ['Kelembapan'], 
    [{
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
const suhuTanah = new createChart('sensorSuhuTanah', 'bar', ['Suhu Tanah'], [{
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
const sensorPh = new createChart('sensorPh', 'doughnut', ['Ph'], [{
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
const sensorNutrisiTanah = new createChart('sensorNutrisiTanah', 'doughnut', ['Nutrisi Tanah'], [{
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
const sensorCahaya = new createChart('sensorCahaya', 'bar', ['Intensitas Cahaya'], [{
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
            siramAirButton.stopTimerButton("Siram Tanaman");
            updateTime('penyiramanTerakhir')

        }if(message['pemberianPupukBerhasil']){
            beriPupukButton.stopTimerButton("Beri Pupuk");
            updateTime('pemberianPupukTerakhir')

        }if(message['pengisianAirBerhasil']){
            isiAirButton.stopTimerButton("Isi Tangki Air");
        }
    }catch(err){
        // console.log(message)

    }
});


export {createChart}

