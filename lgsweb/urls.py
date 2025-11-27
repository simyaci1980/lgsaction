"""
URL configuration for lgsweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('matematik/', views.matematik, name='matematik'),
    path('matematik/unite-1/', views.matematik_unite_1, name='matematik_unite_1'),
    path('matematik/unite-2/', views.matematik_unite_2, name='matematik_unite_2'),
    path('matematik/veri-analizi/', views.veri_analizi, name='veri_analizi'),
    path('matematik/karekok/', views.karekok, name='karekok'),
    path('matematik/karekok_foyler/', views.karekok_foyler, name='karekok_foyler'),
    path('matematik/karekok_tamkare/', views.karekok_tamkare, name='karekok_tamkare'),
    path('matematik/karekok_akokb/', views.karekok_akokb, name='karekok_akokb'),
    path('matematik/carpanlar-katlar/', views.carpanlar_katlar, name='carpanlar_katlar'),
    path('turkce/', views.turkce, name='turkce'),
    path('fen/', views.fen, name='fen'),
    path('inkilap/', views.inkilap, name='inkilap'),
    path('ingilizce/', views.ingilizce, name='ingilizce'),
    path('matematik/uslu_ifadeler/', views.uslu_ifadeler, name='uslu_ifadeler'),
    path('matematik/uslu_foyler/', views.uslu_foyler, name='uslu_foyler'),
    path('matematik/uslu_islemler/', views.uslu_islemler, name='uslu_islemler'),
    path('matematik/uslu_ondalik/', views.uslu_ondalik, name='uslu_ondalik'),
    path('matematik/uslu_bilimsel/', views.uslu_bilimsel, name='uslu_bilimsel'),
    path('din/', views.din, name='din'),
    path('oyunlar/', views.oyunlar, name='oyunlar'),
]
