from django.shortcuts import redirect, render


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
