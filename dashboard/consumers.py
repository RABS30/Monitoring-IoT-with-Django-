
import json
import asyncio

from django.utils import timezone
from django.db.models.functions import TruncMinute
from django.db.models import Avg
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer, SyncConsumer, AsyncConsumer

from asgiref.sync import sync_to_async

from dashboard.models import nilaiSensor


# Data Sensor Awal
dataSensor = nilaiSensor.objects.filter(sensor_id=110, waktu__gte=(timezone.now() - timezone.timedelta(hours=timezone.now().hour, minutes=timezone.now().minute, seconds=timezone.now().second)))
dataSensor = dataSensor.annotate(minute=TruncMinute('waktu')).values('minute').annotate(avg_value=Avg('nilai')).order_by('minute')

response = { 
        'waktu': [entry['minute'].strftime('%H:%M') for entry in dataSensor], 
        'nilai': [int(entry['avg_value']) for entry in dataSensor]
        }

 
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.updateData = True
        
        await self.accept()
        
        response = await self.getDataSensor()
        await self.send(text_data=json.dumps({
            "status"  : "connected",
            "data"    : response,
        }))
        
        asyncio.create_task(self.sendDataUpdate())
    
    async def disconnect(self, close_code):
        self.updateData = False
        print("Disconnected", close_code)
        print("Perangkat : ", self.scope['client'])
        await self.close()
        
        

    
    async def sendDataUpdate(self):
        while self.updateData:
            response = await self.getDataSensor()
            
            await self.send(text_data=json.dumps({
                "status"  : "updateData",
                "data"    : response,
            }))
            
            await asyncio.sleep(1)
        
    @database_sync_to_async
    def getDataSensor(self):
        nowaday = timezone.now() - timezone.timedelta(hours=timezone.now().hour, 
                                              minutes=timezone.now().minute, 
                                              seconds=timezone.now().second) + timezone.timedelta(days=1) - timezone.timedelta(hours=7)
        dataSensor = nilaiSensor.objects.filter(sensor_id=110, 
                                            waktu__gte=nowaday).order_by('-waktu')
        dataSensor = dataSensor.annotate(minute=TruncMinute('waktu')).values('minute').annotate(avg_value=Avg('nilai')).order_by('minute')
        
        response = { 
            'waktu': [entry['minute'].strftime('%H:%M') for entry in dataSensor], 
            'nilai': [int(entry['avg_value']) for entry in dataSensor]
        }

        return response

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        