import paho.mqtt.client as mqtt
   
# callback saat berhasil terhubung ke server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("sensor/tanaman")
    

# callback saat menerima pesan
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    pass
    

# Konfigurasi MQTT
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message


# Hubungkan ke broker
try :
    mqttc.connect("broker.emqx.io", 1883, 60)
except Exception as e:
    print(f'Gagal terhubung ke Broker : {e}')
    
mqttc.loop_start()

