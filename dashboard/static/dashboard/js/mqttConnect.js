// Inisialisasi Broker MQTT
const client = mqtt.connect("wss://broker.emqx.io:8084/mqtt");

// Function saat berhasil terhubung dan subscribe topic
client.on('connect', () => {
    console.log('Berhasil terhubung ke MQTT');
    // subscribe ke topic sensor/tanaman
    client.subscribe('sensor/tanaman', (err) => {
        if(!err){
            console.log('Berhasil subscribe ke topic sensor/tanaman');
        };
    })
})

export {client}