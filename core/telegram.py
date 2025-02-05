import requests
from django.conf import settings


def sendTelegramMessage(chatID, message):
    botToken = settings.TELEGRAM_BOT_TOKEN
    telegramAPIUrl = f'https://api.telegram.org/bot{botToken}/sendMessage'
    payload = {'chatID' : chatID, 'text' : message, 'parse_mode' : 'HTML'}
    requests.post(telegramAPIUrl, data=payload)