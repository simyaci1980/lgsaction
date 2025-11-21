from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    
def matematik(request):
    return render(request, 'matematik.html')
    
def turkce(request):
    return render(request, 'turkce.html')
    
def fen(request):
     return render(request, 'fen.html')

def inkilap(request):
    return render(request, 'inkilap.html')

def ingilizce(request):
    return render(request, 'ingilizce.html')

def din(request):
    return render(request, 'din.html')

def oyunlar(request):
    return render(request, 'oyunlar.html')
