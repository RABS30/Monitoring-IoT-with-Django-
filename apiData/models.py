from django.db import models
from django.contrib.auth.models import User

class UserTokenTelegram(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    chatId      = models.CharField(("Chat ID"), max_length=50, null=True)
    refreshToken= models.CharField(max_length=500, null=True)
    accessToken = models.CharField(max_length=500, null=True)
    login       = models.BooleanField(("Apakah Sudah login ?"), default=False)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} : {self.chatId}'