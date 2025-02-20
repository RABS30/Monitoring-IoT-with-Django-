import requests
import json
from .models import UserTokenTelegram

def sendMessageToTelegram(TELEGRAM_API_URL, chatId, data):
    requests.post(TELEGRAM_API_URL, json={
            'chat_id'   : chatId,
            'text'      : data
        })
    

def verificationToken(request, accessToken):
    response = requests.get(f'https://{request.headers["Host"]}/bot/verification/', headers={'Authorization' : f'Bearer {accessToken}'})
    return response


def validationToken(request, chatId):
    # verifikasi pengguna, ambil data pengguna dari database
    try :
        user            = UserTokenTelegram.objects.get(chatId=chatId)
        accessToken     = user.accessToken
        refreshToken    = user.refreshToken
        chatId          = user.chatId
    except :
        return {'status': False,
                'user'  : 'Pengguna tidak ditemukan'}
    
    # Verifikasi pengguna, verifikasi token
    response        = requests.get(f'https://{request.headers["Host"]}/bot/verification/', headers={'Authorization' : f'Bearer {accessToken}'})
    
    
    if response.status_code == 200 :
        return {'status': True,
                'user'  : user}
        
    elif response.status_code == 401:
        accessToken = newAccessToken(request, refreshToken, chatId)
        
        # Verifikasi pengguna, verifikasi token
        response = verificationToken(request, accessToken)
        
        if response.status_code == 200 :
            return {'status': True,
                    'user'  : user}

    return {'status'    : False,
            'user'      : 'Gagal verifikasi'}   



def newAccessToken(request, refreshToken, chatId):
    try :
        response        = requests.post(f'https://{request.headers["Host"]}/bot/token/refresh/', data = {'refresh' : refreshToken})
        
    except Exception as message:
        return {'status'    : False,
                'user'      : 'Gagal verifikasi'}   

    if response.status_code == 200 :
        accessToken     = json.loads(response.content)['access']

        tokenUpdate = UserTokenTelegram.objects.get(chatId = chatId)
        tokenUpdate.accessToken = accessToken
        tokenUpdate.save()
    else :
        return {'status'    : False,
        'user'              : f'Error {response}'}   
    return accessToken

   