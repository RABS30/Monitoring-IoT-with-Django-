
import json
import asyncio
from asyncio.exceptions import CancelledError

from django.utils import timezone
from django.db.models.functions import TruncMinute
from django.db.models import Avg

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer, SyncConsumer, AsyncConsumer

from asgiref.sync import sync_to_async

from dashboard.models import nilaiSensor,sensor

# Utilities, ambil semua data sensor hari ini berdasarkan ID
def dataSensor(id):
    todayTime   = timezone.now() - timezone.timedelta(hours=timezone.now().hour, 
                                                  minutes=timezone.now().minute, 
                                                  seconds=timezone.now().second)

    dataSensor = nilaiSensor.objects.filter(sensor_id=id, waktu__gte=(todayTime))
    dataSensor = dataSensor.annotate(minute=TruncMinute('waktu')).values('minute').annotate(avg_value=Avg('nilai')).order_by('minute')

    return {
        'nama'   : sensor.objects.get(id=id).nama,
        'sensor' : { 
            'waktu': [entry['minute'].strftime('%H:%M') for entry in dataSensor], 
            'nilai': [int(entry['avg_value']) for entry in dataSensor]
        }
    }

# Utilities, ambil semua data sensor hari ini dari semua sensor
def allDataSensor():
    idSensor = set(sensor.objects.values_list('id', flat=True))

    sensorData = []
    for id in idSensor:
        sensorData.append(dataSensor(id))
        
    return sensorData



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # mengonfirmasi perangkat yang terhubung 
        await self.accept()
        # Mengambil data dari database untuk menampilkan semua data awal
        response = await sync_to_async(allDataSensor)()
        # Mengirim data ke client websocket
        await self.send(text_data=json.dumps({
            "status"  : "connected",
            "data"    : response,
        }))
        
        # Buat tugas sendDataUpdate untuk mengirim data terbaru setiap detik
        self.update_task = asyncio.create_task(self.sendDataUpdate())
    
    async def disconnect(self, close_code):
        # nonaktifkan update data pada function sendDataUpdate
        if hasattr(self, 'update_task'):
            self.update_task.cancel()
            try :
                await asyncio.wait_for(self.update_task, timeout=5)
            except CancelledError:
                print('Task updateData dibatalkan')
            except asyncio.TimeoutError:
                print('Timeout saat menunggu pembatalan task')
        await self.close()
        
    async def sendDataUpdate(self):
        while True:
            try :
                # ambil data sensor terbaru
                response = await asyncio.wait_for(sync_to_async(allDataSensor)(), timeout=5)
                # kirim data ke client websocket
                await self.send(text_data=json.dumps({
                    "status"  : "updateData",
                    "data"    : response,
                }))
                # jeda 1 detik
                await asyncio.sleep(1)
            except CancelledError:
                print('cancel sendUpdate Data')
                break
            finally :
                print('SendDataUpdate selesai')


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        