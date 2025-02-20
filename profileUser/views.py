from django.shortcuts import render
from allauth.account import views


def profile(request):
    return render(request, 'profileUser/profile.html')