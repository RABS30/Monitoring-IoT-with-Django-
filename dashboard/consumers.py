
import json
import asyncio
from asyncio.exceptions import CancelledError

from django.utils import timezone
from django.db.models.functions import TruncMinute
from django.db.models import Avg

from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
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



class ChatConsumer2(AsyncWebsocketConsumer):
    async def connect(self):
        # mengonfirmasi perangkat yang terhubung 
        await self.accept()
        print(self.scope['user'])
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
                print('mengirim data ke : ', self.scope['user'])
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
                print('SendDataUpdate selesai ke :', self.scope['user'])

class ChatConsumer(AsyncWebsocketConsumer):
    taskRunning     = False # Status Task berjalan atau tidak
    backgroundTask  = None  # Menyimpan task ke dalam variable
    
    async def connect(self):
        # Nama Group
        self.room_group_name    = 'todayDataSensor'
        
        # Masukkan client 'channel_name' ke Group 'todayDataSensor'
        await (self.channel_layer.group_add)(                       # type:ignore
            self.room_group_name, self.channel_name
        )
        await self.accept()
        
        if not ChatConsumer.taskRunning : 
            ChatConsumer.taskRunning = True
            # Membuat tugas untuk mengirim sensor setiap 1 detik
            ChatConsumer.backgroundTask = asyncio.create_task(self.dataSensorToday())
        
        
    async def disconnect(self, code):
        # Keluarkan client 'channel_name' dari group 'todayDataSensor'
        await (self.channel_layer.group_discard)(self.room_group_name, self.channel_name)         # type:ignore
        await self.close()
        
    async def receive(self, text_data):
        # Menerima pesan dari client
        textDataJson    = json.loads(text_data)
        data            = textDataJson['message']
        
        # Mengirim pesan ke client 
        message         = {'type' : 'clientConnectMessage','message' : f'{self.scope["user"]} terhubung ke group'}
        
        # Kirim message ke room group dengan handler 'client_connect'
        await (self.channel_layer.group_send)(self.room_group_name, message) #type:ignore
        
         
# ===== Message ke client =====
    # 1. memberi tahu bahwa ada client yang terhubung
    async def clientConnectMessage(self, event):
        message = event['message']
        # Send message ke client
        await self.send(text_data=json.dumps({'message': message}))
    

    # 2. mengirim pesan ke semua client tentang update data harian
    async def sendDataSensorTodayMessage(self, event):
        message = event['message']
        # Send message ke client
        await self.send(text_data=json.dumps({'status' : 'updateData',
                                             'data' : message})
                        )
        
# ===== function tambahan =====
    # 1. Mengambil data sensor hari ini
    async def dataSensorToday(self):
        while True : 
            print('mengirim data')
            try :
                message = {
                    'type' : 'sendDataSensorTodayMessage',
                    'message' : await sync_to_async(allDataSensor)()
                }
                await self.channel_layer.group_send(self.room_group_name, message)   # type: ignore
                await asyncio.sleep(2)

            except Exception as errorMessage:
                print(f'Error: {errorMessage}')
                break
            
        
        
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        