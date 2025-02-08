from .serializers import sensorSerializer
from .models import UserTokenTelegram
from .botUtils import sendMessageToTelegram, validationToken

from django.conf import settings
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from dashboard.models import sensor

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken

import json
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_URL = settings.TELEGRAM_API_URL

 
    
# Login untuk mendapatkan Token JWT
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data     = request.POST
        username = data.get('username')
        password = data.get('password')
        chatId   = data.get('chatId')
        
        # Autentifikasi pengguna
        user = authenticate(request, username=username, password=password)
        
        if user:
            refresh = RefreshToken.for_user(user)
            try :
                # 
                if UserTokenTelegram.objects.get(chatId=chatId).login == True :
                    return JsonResponse({'error' : 'Anda sudah login, tolong logout terlebih dahulu '}, status=404)
            except Exception as message:
                
                # Simpan chat ID, access dan refresh token di database
                UserTokenTelegram.objects.update_or_create(user=user, defaults={
                    'refreshToken' : refresh, 
                    'accessToken'  : refresh.access_token, 
                    'chatId'       : chatId,
                    'login'        : True
                })
            
                return JsonResponse({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user'  : user.username
                })
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)   
    return JsonResponse({'error': 'Invalid request'}, status=400)
  
# Validasi Token JWT
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello, {request.user.username}! Token kamu valid."})

# Menangani komunikasi pengguna dan telegram bot
@method_decorator(csrf_exempt, name='dispatch')
class telegramWebhook(View):     
    def post(self, request, *args, **kwargs):
        data     = json.loads(request.body)
        chatId   = data['message']['chat']['id']
        command  = data['message']['text']
        
        # Mengakses bot
        if(command.startswith('/login')):
            try :
                _, username, password = command.split()
                # Mendapatkan access token
                userLogin = requests.post(f'https://{request.headers["Host"]}/bot/login/', data={'username' : username, 'password' : password, 'chatId' : chatId})
                
                # Gagal Mendapatkan access token
                if(userLogin.status_code == 400 or userLogin.status_code == 401):
                    replyText = 'Gagal Login, pastikan username dan password benar'
                elif(userLogin.status_code == 404):
                    replyText = 'Anda sudah login, tolong logout terlebih dahulu'
                # Berhasil mendapatkan access token
                else :
                    user = json.loads(userLogin.content)['user'] 
                    replyText = f'Berhasil Login sebagai {user}, silahkan berikan perintah'
            except Exception as message :
                replyText = f'Tolong masukkan data sesuai format {"/login <username> <password>"}'
                
        elif(command.lower() == '/logout'):
            try :
                user = UserTokenTelegram.objects.get(chatId=chatId).delete()
                
                replyText = 'Anda berhasil logout'
            except :
                replyText = 'Anda belum login'                
        
        elif(command.lower() == '/start'):
            validation = validationToken(request, chatId)
            if(validation['status']):
                replyText = 'Hello world'     
            else :
                replyText = 'Apakah anda sudah login ?'
        
        else :
            replyText = 'Maaf, saya tidak mengerti perintah anda'
            
        sendMessageToTelegram(TELEGRAM_API_URL, chatId, replyText)        
        return JsonResponse({'status' : 'ok'})


# REST API Datasets Sensor
class sensorViewSet(viewsets.ReadOnlyModelViewSet): 
    queryset = sensor.objects.all()
    serializer_class = sensorSerializer
    
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context
    
   
   
   
   
   
   
   
'''
        # ===== Ambil data ===== 
        data = json.loads(request.body)
        replyText = ''
        if 'message' in data :
            chatId      = data['message']['chat']['id']
            userMessage = data['message']['text']

        # ===== Verifikasi Pengguna =====
        try :
            user = UserTokenTelegram.objects.get(chatId=chatId)
        except Exception as message:
            sendMessageToTelegram(TELEGRAM_API_URL, chatId, f'Silahkan Login terlebih dahulu dengan "/login username password"')        
            return JsonResponse({'status' : 'Not Found'})
                
                
        # ===== Pesan Masuk =====
        if userMessage.startswith('/login'):
            _, username, password = userMessage.split()
            response = requests.post(f"https://{request.headers['Host']}/bot/login/", data={'username ' : username, 'password' : password})
            print('ini setelah login : ', response)


''' 
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    
    