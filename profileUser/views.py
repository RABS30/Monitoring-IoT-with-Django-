from django.shortcuts import render

def profile(request):
    print('Ini GET : ',request.GET)
    if request.method == 'GET' :
        print('Ini POST : ',request.POST)
        
    return render(request, 'profileUser/profile.html')