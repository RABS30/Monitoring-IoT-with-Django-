import paho.mqtt.client as mqtt
import os
import json
from datetime import datetime
from . import models
from .models import nilaiSensor, sensor
 
def startMqtt():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # callback saat berhasil terhubung ke server
    def on_connect(client, userdata, flags, rc): 
        print("Connected with result code "+str(rc))
        client.subscribe("sensor/tanaman")
        client.subscribe("sensor/tanaman2")
        
                
        
        



    # callback saat menerima pesan 
    def on_message(client, userdata, msg):
        try :
            message = json.loads(msg.payload)
            if("message" in message):
                # Menyimpan data sensor 
                if(message["message"] == "Data Sensor"):
                    for data in message:
                        if message[data] != "Data Sensor" :
                            if data in sensor.objects.values_list('nama', flat=True) :
                                namaSensor = sensor.objects.get(nama=data)
                                nilaiSensor(sensor=namaSensor, nilai=message[data]).save()
                            else:
                                namaSensor = sensor(nama=data)
                                namaSensor.save()
                                nilaiSensor(sensor=namaSensor, nilai=message[data]).save()         
                
                # Menyimpan data penyiraman terakhir
                if(message["message"] == "Siram"):
                    data = models.penyiramanTerakhir.objects.first()
                    if data :
                        data.waktu = datetime.now().replace(second=0, microsecond=0)
                        data.save()
                
                # Menyimpan data pupuk terakhir
                if(message["message"] == "Beri Pupuk"):
                    data = models.pemberianPupukTerakhir.objects.first()
                    if data :
                        data.waktu = datetime.now().replace(second=0, microsecond=0)
                        data.save()
            
            else :
                print('Data tidak terdefinisi : ', message)
        except Exception as message :
            print('error : ', message)


            


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

