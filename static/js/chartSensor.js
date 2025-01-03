
const dataValue = 0;
// Sensor Kelembapan Tanah
const ctx = document.getElementById('sensorKelembapan');
const sensorKelembapan = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Kelembapan Tanah'],
        datasets: [{
        label: 'Sensor Kelembapan Tanah',
        data: [dataValue],
        // Ubah warna background berdasarkan kondisi
        backgroundColor: [dataValue >= 7 ? 'rgba(75, 192, 192, 0.2)' : 'rgba(255, 99, 132, 0.2)'], 
        // Border sesuai warna background
        borderColor: [dataValue >= 7 ? 'rgba(75, 192, 192, 1)' : 'rgba(255, 99, 132, 1)'], 
        borderWidth: 1
        }] 
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
        y: {
            beginAtZero: true,
            min: 0,
            max: 20,
        }
        }
    }
});

// Update Sensor Kelembapan Tanah
function updateChart(randomValue){
    sensorKelembapan.data.datasets[0].data[0] = randomValue;
    sensorKelembapan.data.datasets[0].backgroundColor = randomValue <= 15 ? 'rgba(75, 192, 192, 0.2)' : 'rgba(255, 99, 132, 0.2)';
    sensorKelembapan.data.datasets[0].borderColor = randomValue <= 15 ? 'rgba(75, 192, 192, 1)' : 'rgba(255, 99, 132, 1)';
    sensorKelembapan.data.datasets[0].borderColor = randomValue <= 15 ? 'rgba(75, 192, 192, 1)' : 'rgba(255, 99, 132, 1)';
    sensorKelembapan.update();
}

// Sensor Suhu Tanah
const ctx2 = document.getElementById('sensorSuhuTanah');
const sensorSuhuTanah = new Chart(ctx2, {
    type: 'bar',
    data: {
        labels: ['Suhu Tanah'],
        datasets: [{
        label: 'Sensor Suhu Tanah',
        data: [dataValue],
        // Ubah warna background berdasarkan kondisi
        backgroundColor: [dataValue >= 7 ? 'rgba(75, 192, 192, 0.2)' : 'rgba(255, 99, 132, 0.2)'], 
        // Border sesuai warna background
        borderColor: [dataValue >= 7 ? 'rgba(75, 192, 192, 1)' : 'rgba(255, 99, 132, 1)'], 
        borderWidth: 1
        }] 
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
        y: {
            beginAtZero: true,
            min: 0,
            max: 21,
        }
        }
    }
});

// Update Sensor Suhu Tanah
function updateChart2(randomValue){
    sensorSuhuTanah.data.datasets[0].data[0] = randomValue;
    sensorSuhuTanah.data.datasets[0].backgroundColor = randomValue <= 15 ? 'rgba(75, 192, 192, 0.2)' : 'rgba(255, 99, 132, 0.2)';
    sensorSuhuTanah.data.datasets[0].borderColor = randomValue <= 15 ? 'rgba(75, 192, 192, 1)' : 'rgba(255, 99, 132, 1)';
    sensorSuhuTanah.data.datasets[0].borderColor = randomValue <= 15 ? 'rgba(75, 192, 192, 1)' : 'rgba(255, 99, 132, 1)';
    sensorSuhuTanah.update();
}

// Chart Sensor Ph
const ctx3 = document.getElementById('sensorPh');
const sensorPh = new Chart(ctx3, {
    type: 'doughnut',
    data: {
        labels: ['pH Tanah'],
        datasets: [{
            label: 'Sensor PH air',
            data: [dataValue, 14-dataValue],
            // Ubah warna background berdasarkan kondisi
            backgroundColor: [
                'rgba(75, 192, 192, 0.2)',
                'rgba(255, 99, 132, 0.2)', 
            ], 
            // Border sesuai warna background
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(75, 192, 192, 1)',
            ], 
            borderWidth: 1
        }] 
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
        y: {
            beginAtZero: true,
            min: 0,
            max: 14,
        }
        }
    }
});

// Update Sensor Ph
function updateChart3(randomValue){
    sensorPh.data.datasets[0].data = [randomValue, 14-randomValue];
    sensorPh.data.labels  = ["pH Tanah = "+String(randomValue)];
    sensorPh.update();
}

// Chart Sensor Nutrisi Tanah
const ctx4 = document.getElementById('sensorNutrisiTanah');
const sensorNutrisiTanah = new Chart(ctx4, {
    type: 'doughnut',
    data: {
        labels: ['Nutrisi Tanah'],
        datasets: [{
            label: 'Sensor Nutrisi Tanah',
            data: [dataValue, 14-dataValue],
            // Ubah warna background berdasarkan kondisi
            backgroundColor: [
                'rgba(75, 192, 192, 0.2)',
                'rgba(255, 99, 132, 0.2)', 
            ], 
            // Border sesuai warna background
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(75, 192, 192, 1)',
            ], 
            borderWidth: 1
        }] 
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
        y: {
            beginAtZero: true,
            min: 0,
            max: 14,
        }
        }
    }
});

// Update Chart 3
function updateChart3(randomValue){
    sensorNutrisiTanah.data.datasets[0].data = [randomValue, 14-randomValue];
    sensorNutrisiTanah.data.labels  = ["pH Tanah = "+String(randomValue)];
    sensorNutrisiTanah.update();
}






setInterval(() => {
    const randomValue = Math.floor(Math.random() * 20);
    const randomPh = Math.floor(Math.random() * 14);
    updateChart(randomValue);
    updateChart2(randomValue+5);
    updateChart3(randomPh);
},500)