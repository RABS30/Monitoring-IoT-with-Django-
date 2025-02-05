from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .serializers import sensorSerializer
from dashboard.models import sensor


from rest_framework import viewsets

from django.views import View

import json
import requests

# curl -X POST "https://api.telegram.org/bot7593019334:AAErjxou9aDEhQE2_4qVOV8epfmkL3yIW2E/setWebhook?url=https://8a47-36-72-151-137.ngrok-free.app/bot/webhook/"

# https://api.telegram.org/bot7630117939:AAGJVBsXCUkEjPLaA1KYJlqiQZvrklhNOc4/getWebhookInfo
# curl -X GET "https://api.telegram.org/bot7630117939:AAGJVBsXCUkEjPLaA1KYJlqiQZvrklhNOc4/deleteWebhook"


# ===== Telegram Bot Configuration =====
TELEGRAM_BOT_TOKEN  = '7593019334:AAErjxou9aDEhQE2_4qVOV8epfmkL3yIW2E'
TELEGRAM_API_URL    = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"



@method_decorator(csrf_exempt, name='dispatch')
class telegramWebhook(View): 
    def post(self, request, *args, **kwargs):
        
        print(f'ini webhook headers : {request.headers}')
        data = json.loads(request.body)
        print(f'ini webhook : {data}')
        
        if 'message' in data :
            chatID  = data['message']['chat']['id']
            text    = data['message']['text']
            print(f'ini chatID : {chatID}')
            print(f'ini pesan  : {text}')
            if text.lower() == '/start':
                replyText = 'Hallo! Selamat datang di Django Telegram Bot 🚀'    
            elif text.lower() == "hallo":
                replyText = f'Hallo! {data["message"]["chat"]["first_name"]}'
            else :
                replyText = f'https://8a47-36-72-151-137.ngrok-free.app/'        

        requests.post(TELEGRAM_API_URL, json={
            'chat_id' : chatID,
            'text'   : replyText
        })
        
        return JsonResponse({'status' : 'ok'})


class sensorViewSet(viewsets.ReadOnlyModelViewSet): 
    queryset = sensor.objects.all()
    serializer_class = sensorSerializer
    
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context