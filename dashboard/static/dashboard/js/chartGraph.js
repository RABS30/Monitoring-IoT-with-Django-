import { createChart } from "./chartRealTime.js"; 
import { socket } from "./websocketConnect.js";




const Utils = {
    months: function ({ count }) {
      const monthNames = [
        'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli',
        'Agustus', 'September', 'Oktober', 'November', 'Desember'
      ];
      const today = new Date();
      let months = [];
      for (let i = 0; i < count; i++) {
        months.push(monthNames[(today.getMonth() + i) % 12]);
      }
      return months;
    },
    parseData: function(e){
      const message = JSON.parse(e.data);
      const { data, status } = message;
      return {data, status};
    }
};


const graphKelembapanTanah = new createChart(
  'graphKelembapanTanah', 
  'line',
  Utils.months({ count: 12 }),
  [{
    label: 'Kelembapan Tanah',
    data: [50,50,50,50,50,50,50,50,50,50,50,50],
    fill: true,
    borderColor: 'rgb(75, 192, 192)',
    tension: 0.1,
    borderWidth: 1,
    pointStyle : false,
  }], 
)

const graphSuhuTanah = new createChart(
  'graphSuhuTanah', 
  'line',
  Utils.months({ count: 12 }),
  [{
    label: 'Suhu Tanah',
    data: [50,50,50,50,50,50,50,50,50,50,50,50],
    fill: true,
    borderColor: 'rgb(75, 192, 192)',
    tension: 0.1,
    borderWidth: 1,
    pointStyle : false
  }]
)

const graphIntensitasCahaya = new createChart(
  'graphIntensitasCahaya', 
  'line',
  Utils.months({ count: 12 }),
  [{
    label: 'Intensitas Cahaya',
    data: [50,50,50,50,50,50,50,50,50,50,50,50],
    fill: true,
    borderColor: 'rgb(75, 192, 192)',
    tension: 0.1,
    borderWidth: 1,
    pointStyle : false,
  }],
  {
    y : {
      min : 0,
      max : 14
    }
  }
)
const graphNutrisiTanah = new createChart(
  'graphNutrisiTanah', 
  'line',
  Utils.months({ count: 12 }),
  [{
    label: 'Nutrisi Tanah',
    data: [50,50,50,50,50,50,50,50,50,50,50,50],
    fill: true,
    borderColor: 'rgb(75, 192, 192)',
    tension: 0.1,
    borderWidth: 1,
    pointStyle : false
  }]
)



export {graphKelembapanTanah, graphIntensitasCahaya, graphNutrisiTanah, graphSuhuTanah, Utils}