import { socket } from "./websocketConnect.js";
import { graphIntensitasCahaya, graphKelembapanTanah, graphNutrisiTanah, graphSuhuTanah, Utils } from "./chartGraph.js";


const kelembapanTanah   = document.getElementById('selectGraphKelembapanTanah');
const intensitasCahaya  = document.getElementById('selectGraphIntensitasCahaya')
const nutrisiTanah      = document.getElementById('selectGraphNutrisiTanah')
const suhuTanah         = document.getElementById('selectGraphSuhuTanah')

let waktuKelembapanTanah  = kelembapanTanah.options[kelembapanTanah.selectedIndex].value
let waktuIntensitasCahaya = intensitasCahaya.options[intensitasCahaya.selectedIndex].value
let waktuNutrisiTanah     = intensitasCahaya.options[nutrisiTanah.selectedIndex].value
let waktuSuhuTanah        = intensitasCahaya.options[suhuTanah.selectedIndex].value  

kelembapanTanah.addEventListener('change', (event)=> {
    waktuKelembapanTanah  = kelembapanTanah.options[kelembapanTanah.selectedIndex].value
    if(waktuKelembapanTanah === 'day'){
        fetch(`${window.location.origin}/getSensorData/kelembapanTanah/day/`)
        .then(response => response.json())
        .then(response => {
            const { nilai, waktu } = response
            graphKelembapanTanah.update(nilai, waktu)
        }).catch(error => {
            console.error('Error fetching data:', error);
        });
    }
    if(waktuKelembapanTanah === 'week'){
        fetch(`${window.location.origin}/getSensorData/kelembapanTanah/week/`)
        .then(response => response.json())
        .then(response => {
            const { nilai, waktu } = response
            graphKelembapanTanah.update(nilai, waktu)

        }).catch(error => {
            console.error('Error fetching data:', error);
        });
    }
    if(waktuKelembapanTanah === 'month'){
        fetch(`${window.location.origin}/getSensorData/kelembapanTanah/month/`)
        .then(response => response.json())
        .then(response => {
            const { nilai, waktu } = response
            graphKelembapanTanah.update(nilai, waktu)

        }).catch(error => {
            console.error('Error fetching data:', error);
        });
    }
    if(waktuKelembapanTanah === 'year'){
        fetch(`${window.location.origin}/getSensorData/kelembapanTanah/year/`)
        .then(response => response.json())
        .then(response => {
            const { nilai, waktu } = response
            graphKelembapanTanah.update(nilai, waktu)

        }).catch(error => {
            console.error('Error fetching data:', error);
        });
    }
    

})
intensitasCahaya.addEventListener('change', (event)=> {
    waktuIntensitasCahaya = intensitasCahaya.options[intensitasCahaya.selectedIndex].value
    if(waktuIntensitasCahaya === 'day'){
        fetch(`${window.location.origin}/getSensorData/intensitasCahaya/day/`)
        .then(response => response.json())
        .then(response => {
            const { nilai, waktu } = response
            graphIntensitasCahaya.update(nilai, waktu)

        }).catch(error => {
            console.error('Error fetching data:', error);
        });
    }
    if(waktuIntensitasCahaya === 'week'){
        fetch(`${window.location.origin}/getSensorData/intensitasCahaya/week/`)
        .then(response => response.json())
        .then(response => {
            const { nilai, waktu } = response
            graphIntensitasCahaya.update(nilai, waktu)

        }).catch(error => {
            console.error('Error fetching data:', error);
        });
    }
    if(waktuIntensitasCahaya === 'month'){
        fetch(`${window.location.origin}/getSensorData/intensitasCahaya/month/`)
        .then(response => response.json())
        .then(response => {
            const { nilai, waktu } = response
            graphIntensitasCahaya.update(nilai, waktu)

        }).catch(error => {
            console.error('Error fetching data:', error);
        });
    }
    if(waktuIntensitasCahaya === 'year'){
        fetch(`${window.location.origin}/getSensorData/intensitasCahaya/year/`)
        .then(response => response.json())
        .then(response => {
            const { nilai, waktu } = response
            graphIntensitasCahaya.update(nilai, waktu)

        }).catch(error => {
            console.error('Error fetching data:', error);
        });
    }
})
nutrisiTanah.addEventListener('change', (event)=> {
    waktuNutrisiTanah     = nutrisiTanah.options[nutrisiTanah.selectedIndex].value;
    if(waktuNutrisiTanah === 'day'){
        fetch(`${window.location.origin}/getSensorData/nutrisiTanah/day/`)
        .then(response => response.json())
        .then(response => {
            const { nilai, waktu } = response
            graphNutrisiTanah.update(nilai, waktu)

        }).catch(error => {
            console.error('Error fetching data:', error);
        });
    }
    if(waktuNutrisiTanah === 'week'){
        fetch(`${window.location.origin}/getSensorData/nutrisiTanah/week/`)
        .then(response => response.json())
        .then(response => {
            const { nilai, waktu } = response
            graphNutrisiTanah.update(nilai, waktu)

        }).catch(error => {
            console.error('Error fetching data:', error);
        });
    }
    if(waktuNutrisiTanah === 'month'){
        fetch(`${window.location.origin}/getSensorData/nutrisiTanah/month/`)
        .then(response => response.json())
        .then(response => {
            const { nilai, waktu } = response
            graphNutrisiTanah.update(nilai, waktu)

        }).catch(error => {
            console.error('Error fetching data:', error);
        });
    }
    if(waktuNutrisiTanah === 'year'){
        fetch(`${window.location.origin}/getSensorData/nutrisiTanah/year/`)
        .then(response => response.json())
        .then(response => {
            const { nilai, waktu } = response
            graphNutrisiTanah.update(nilai, waktu)

        }).catch(error => {
            console.error('Error fetching data:', error);
        });
    }
})
suhuTanah.addEventListener('change', (event)=> {
    waktuSuhuTanah        = suhuTanah.options[suhuTanah.selectedIndex].value;
    if(waktuSuhuTanah === 'day'){
        fetch(`${window.location.origin}/getSensorData/suhuTanah/day/`)
        .then(response => response.json())
        .then(response => {
            const { nilai, waktu } = response
            graphSuhuTanah.update(nilai, waktu)

        }).catch(error => {
            console.error('Error fetching data:', error);
        });
    }
    if(waktuSuhuTanah === 'week'){
        fetch(`${window.location.origin}/getSensorData/suhuTanah/week/`)
        .then(response => response.json())
        .then(response => {
            const { nilai, waktu } = response
            graphSuhuTanah.update(nilai, waktu)

        }).catch(error => {
            console.error('Error fetching data:', error);
        });
    }
    if(waktuSuhuTanah === 'month'){
        fetch(`${window.location.origin}/getSensorData/suhuTanah/month/`)
        .then(response => response.json())
        .then(response => {
            const { nilai, waktu } = response
            graphSuhuTanah.update(nilai, waktu)

        }).catch(error => {
            console.error('Error fetching data:', error);
        });
    }
    if(waktuSuhuTanah === 'year'){
        fetch(`${window.location.origin}/getSensorData/suhuTanah/year/`)
        .then(response => response.json())
        .then(response => {
            const { nilai, waktu } = response
            graphSuhuTanah.update(nilai, waktu)

        }).catch(error => {
            console.error('Error fetching data:', error);
        });
    }
})

socket.onmessage = (e) => {
    if(e.data){
        const { status, data } = Utils.parseData(e);
        // Saat chart baru terhubung
        if (status === 'connected') {
            for (let i=0; i < data.length; i++){
                const { nama, sensor } = data[i]  
                if (nama === 'kelembapanTanah'){
                graphKelembapanTanah.update(sensor['nilai'], sensor['waktu'])
                }
                if (nama === 'nutrisiTanah'){
                graphNutrisiTanah.update(sensor['nilai'], sensor['waktu'])
                }
                if (nama === 'intensitasCahaya'){
                graphIntensitasCahaya.update(sensor['nilai'], sensor['waktu'])
                }
                if (nama === 'suhuTanah'){
                graphSuhuTanah.update(sensor['nilai'], sensor['waktu'])
                }
                if(nama === 'Ph'){
                
                }
            }
        }    
        if (status === 'updateData') {
            for (let i=0; i < data.length; i++){
                const { nama, sensor } = data[i]
                console.log('ini adalah nama dan sensor', nama, sensor)
                // Update Graph
                if (nama === 'kelembapanTanah'){
                    if(waktuKelembapanTanah === 'today'){
                        graphKelembapanTanah.update(sensor['nilai'], sensor['waktu'])
                    }
                }
                if (nama === 'nutrisiTanah'){
                    if(waktuNutrisiTanah === 'today'){
                        graphNutrisiTanah.update(sensor['nilai'], sensor['waktu'])
                    }
                }
                if (nama === 'intensitasCahaya'){
                    if(waktuIntensitasCahaya === 'today'){
                        graphIntensitasCahaya.update(sensor['nilai'], sensor['waktu'])
                    }
                }
                if (nama === 'suhuTanah'){
                    if(waktuSuhuTanah === 'today'){
                        graphSuhuTanah.update(sensor['nilai'], sensor['waktu'])
                    }
                } 
            }
        }
    }
}