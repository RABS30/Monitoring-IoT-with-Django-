// Inisialisasi Broker MQTT
const client = mqtt.connect("wss://broker.emqx.io:8084/mqtt");

// Menghubungkan Broker MQTT
client.on('connect', () => {
    console.log('Terhubung ke Broker MQTT');
    // Subscribe ke topik 'sensor/tanaman'
    client.subscribe('sensor/tanaman2', function (err) {
        if (!err) {
            console.log('Berhasil subscribe ke topik sensor/tanaman');
        };
    });
});

client.on('message', (topic, message) => {
    // Menampilkan pesan di HTML
    const msg = document.createElement('p');
    msg.textContent = `Topic: ${topic}, Message: ${message.toString()}`;
    document.getElementById('messages').appendChild(msg);
  });


function publishMessage() {
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