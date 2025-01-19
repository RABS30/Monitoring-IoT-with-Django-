
import paho.mqtt.client as mqtt
import json
from datetime import datetime
from . import models
 
def startMqtt():
    # callback saat berhasil terhubung ke server
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("sensor/tanaman")
        client.subscribe("sensor/tanaman2")


    # callback saat menerima pesan 
    def on_message(client, userdata, msg):
        try :
            message = json.loads(msg.payload)
            
        except Exception as message :
            print('error : ', message)
            
        # Menerima pesan callback
        if("message" in message):
            if(message["message"] == "Siram"):
                data = models.penyiramanTerakhir.objects.first()
                if data :
                    data.waktu = datetime.now().replace(second=0, microsecond=0)
                    data.save()
                
            if(message["message"] == "Beri Pupuk"):
                data = models.pemberianPupukTerakhir.objects.first()
                if data :
                    data.waktu = datetime.now().replace(second=0, microsecond=0)
                    data.save()



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

