
import paho.mqtt.client as mqtt
import json
from .models import sensorTanaman
 
def startMqtt():
    # callback saat berhasil terhubung ke server
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("sensor/tanaman")
        client.subscribe("sensor/tanaman2")


    # callback saat menerima pesan 
    def on_message(client, userdata, msg):
        message = json.loads(msg.payload)
        for data in message:
            sensorTanaman.objects.create(nama=data, nilai=message[data])
            


    # Konfigurasi MQTT
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message


    # Hubungkan ke broker
    try :
        client.connect("broker.emqx.io", 1883, 60)
    except Exception as e:
        print(f'Gagal terhubung ke Broker : {e}')
        print('Mencoba reconnect....')
        client.reconnect()
        
    client.loop_start()

