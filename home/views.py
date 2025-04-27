from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def iniciosesion(request):
    return render(request, 'home/iniciosesion.html')

def registro(request):
    return render(request, 'home/registro.html')
