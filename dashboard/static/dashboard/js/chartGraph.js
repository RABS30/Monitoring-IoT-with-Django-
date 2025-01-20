import { createChart } from "./chartSensor.js";
const months = new Date().getMonth()

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
    }
};

const graphKelembapanTanah = new createChart(
    'graphKelembapanTanah', 
    'line',
    Utils.months({ count: 12 }),
    [{
        label: 'Kelembapan Tanah',
        data: [65, 59, 80, 81, 56, 55, 40, 59, 80, 81, 56, 55],
        fill: true,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1,
        borderWidth: 3
      }]
)

const graphSuhuTanah = new createChart(
  'graphSuhuTanah', 
  'line',
  Utils.months({ count: 12 }),
  [{
      label: 'Suhu Tanah',
      data: [65, 59, 80, 81, 56, 55, 40, 59, 80, 81, 56, 55],
      fill: true,
      borderColor: 'rgb(75, 192, 192)',
      tension: 0.1,
      borderWidth: 3
    }]
)

const intensitasCahaya = new createChart(
  'graphIntensitasCahaya', 
  'line',
  Utils.months({ count: 12 }),
  [{
      label: 'Suhu Tanah',
      data: [65, 59, 80, 81, 56, 55, 40, 59, 80, 81, 56, 55],
      fill: true,
      borderColor: 'rgb(75, 192, 192)',
      tension: 0.1,
      borderWidth: 3,
    }]
)
const nutrisiTanah = new createChart(
  'graphNutrisiTanah', 
  'line',
  Utils.months({ count: 12 }),
  [{
      label: 'Suhu Tanah',
      data: [65, 59, 80, 81, 56, 55, 40, 59, 80, 81, 56, 55],
      fill: true,
      borderColor: 'rgb(75, 192, 192)',
      tension: 0.1,
      borderWidth: 3
    }]
)