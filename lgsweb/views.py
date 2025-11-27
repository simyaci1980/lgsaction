from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def matematik(request):
    return render(request, 'matematik/matematik.html')

def turkce(request):
    return render(request, 'turkce/turkce.html')

def fen(request):
    return render(request, 'fen/fen.html')

def inkilap(request):
    return render(request, 'inkilap/inkilap.html')

def ingilizce(request):
    return render(request, 'ingilizce/ingilizce.html')

def din(request):
    return render(request, 'din/din.html')

def oyunlar(request):
    return render(request, 'oyunlar.html')

def carpanlar_katlar(request):
    return render(request, 'matematik/carpanlar_katlar.html')

def matematik_unite_1(request):
    return render(request, 'matematik/matematik_unite_1.html')

def matematik_unite_2(request):
    return render(request, 'matematik/matematik_unite_2.html')

def veri_analizi(request):
    return render(request, 'matematik/veri_analizi.html')

def karekok(request):
    return render(request, 'matematik/karekok.html')

def uslu_ifadeler(request):
    return render(request, 'matematik/uslu_ifadeler.html')

def uslu_foyler(request):
    return render(request, 'matematik/uslu_foyler.html')

def uslu_islemler(request):
    return render(request, 'matematik/uslu_islemler.html')

def uslu_ondalik(request):
    return render(request, 'matematik/uslu_ondalik.html')

def uslu_bilimsel(request):
    return render(request, 'matematik/uslu_bilimsel.html')

def karekok_foyler(request):
    return render(request, 'matematik/karekok_foyler.html')

def karekok_tamkare(request):
    return render(request, 'matematik/karekok_tamkare.html')

def karekok_akokb(request):
    return render(request, 'matematik/karekok_akokb.html')
    




