// Inisialisasi Broker MQTT
const client = mqtt.connect("wss://broker.emqx.io:8084/mqtt");

// Menghubungkan Broker MQTT
client.on('connect', () => {
    console.log('Terhubung ke Broker MQTT');
    // Subscribe ke topik 'sensor/tanaman'
    client.subscribe('sensor/tanaman', function (err) {
        if (!err) {
            console.log('Berhasil subscribe ke topik sensor/tanaman');
        };
    });
});

// Menerima pesan dari topic yang disubscribe
client.on('message', (topic, message) => {
    console.log(`Topic: ${topic} \nMessages: ${message} \nTipe : ${typeof(message)}`);
    message = JSON.parse(message);

    // console.log(message['SuhuPh']);
  
});


// Mengirim data ke topic sensor/tanaman2
function publishMessage() {
    var siram   = document.getElementById()
    const message = document.getElementById('message').value;
    if (message) {
        client.publish('sensor/tanaman2', message, (err) => {
        if (err) {
            console.log('Error publishing message:', err);
        } else {
            console.log('Message published:', message);
        }
        });
    }
}
