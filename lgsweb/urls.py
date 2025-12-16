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
    path('matematik/unite-3/', views.matematik_unite_3, name='matematik_unite_3'),
    path('matematik/veri-analizi/', views.veri_analizi, name='veri_analizi'),
    path('matematik/karekok/', views.karekok, name='karekok'),
    path('matematik/karekok_foyler/', views.karekok_foyler, name='karekok_foyler'),
    path('matematik/karekok_tamkare/', views.karekok_tamkare, name='karekok_tamkare'),
    path('matematik/karekok_akokb/', views.karekok_akokb, name='karekok_akokb'),
    path('matematik/karekok_carpma_bolme/', views.karekok_carpma_bolme, name='karekok_carpma_bolme'),
    path('matematik/karekok_toplama_cikarma/', views.karekok_toplama_cikarma, name='karekok_toplama_cikarma'),
    path('matematik/karekok_ondalik/', views.karekok_ondalik, name='karekok_ondalik'),
    path('matematik/carpanlar-katlar/', views.carpanlar_katlar, name='carpanlar_katlar'),
    path('turkce/', views.turkce, name='turkce'),
    path('fen/', views.fen, name='fen'),
    path('fen/unite-1/', views.fen_unite_1, name='fen_unite_1'),
    path('fen/unite-1-ozeti/', views.unite_1_ozeti, name='unite_1_ozeti'),
    path('fen/mevsimler-iklim/', views.mevsimler_iklim, name='mevsimler_iklim'),
    path('fen/iklim-olaylari/', views.iklim_olaylari, name='iklim_olaylari'),
    path('fen/unite-2/', views.fen_unite_2, name='fen_unite_2'),
    path('fen/dna-genetik-kod/', views.dna_genetik_kod, name='dna_genetik_kod'),
    path('fen/kalitim/', views.kalitim, name='kalitim'),
    path('fen/mutasyon-modifikasyon/', views.mutasyon_modifikasyon, name='mutasyon_modifikasyon'),
    path('fen/adaptasyon/', views.adaptasyon, name='adaptasyon'),
    path('fen/biyoteknoloji/', views.biyoteknoloji, name='biyoteknoloji'),
    path('fen/unite-2-ozeti/', views.unite_2_ozeti, name='unite_2_ozeti'),
    path('fen/unite-3/', views.fen_unite_3, name='fen_unite_3'),
    path('fen/basinc/', views.basinc, name='basinc'),
    path('fen/unite-4/', views.fen_unite_4, name='fen_unite_4'),
    path('fen/periyodik_sistem/', views.periyodik_sistem, name='periyodik_sistem'),
    path('fen/fiziksel_kimyasal_degisim/', views.fiziksel_kimyasal_degisim, name='fiziksel_kimyasal_degisim'),
    path('fen/kimyasal_tepkimeler/', views.kimyasal_tepkimeler, name='kimyasal_tepkimeler'),
    path('fen/asitler_bazlar/', views.asitler_bazlar, name='asitler_bazlar'),
    path('fen/maddenin_isi_etkisimi/', views.maddenin_isi_etkisimi, name='maddenin_isi_etkisimi'),
    path('fen/unite-7/', views.fen_unite_7, name='fen_unite_7'),
    path('fen/yazili_hazirligi/', views.yazili_hazirligi, name='yazili_hazirligi'),
    path('inkilap/', views.inkilap, name='inkilap'),
    path('inkilap/unite-1/', views.inkilap_unite_1, name='inkilap_unite_1'),
    path('inkilap/gelisen-avrupa/', views.gelisen_avrupa, name='gelisen_avrupa'),
    path('inkilap/unite-2/', views.inkilap_unite_2, name='inkilap_unite_2'),
    path('inkilap/dunyasavasi-1/', views.dunyasavasi_1, name='dunyasavasi_1'),
    path('inkilap/dunyasavasi-osmanlı/', views.dunyasavasi_osmanlı, name='dunyasavasi_osmanlı'),
    path('inkilap/mondros-ateskesi/', views.mondros_ateskesi, name='mondros_ateskesi'),
    path('inkilap/kuvayi-milliye/', views.kuvayi_milliye, name='kuvayi_milliye'),
    path('inkilap/hazirlik-donemi/', views.hazirlik_donemi, name='hazirlik_donemi'),
    path('inkilap/misak-i-milli-tbmm/', views.misak_i_milli_tbmm, name='misak_i_milli_tbmm'),
    path('inkilap/ayaklanmalar/', views.ayaklanmalar, name='ayaklanmalar'),
    path('inkilap/sevr-antlasmasi/', views.sevr_antlasmasi, name='sevr_antlasmasi'),
    path('inkilap/unite-3/', views.inkilap_unite_3, name='inkilap_unite_3'),
    path('inkilap/dogu-guney-cepheleri/', views.dogu_guney_cepheleri, name='dogu_guney_cepheleri'),
    path('inkilap/bati-cephesi/', views.bati_cepheleri, name='bati_cepheleri'),
    path('inkilap/maarif-kongresi/', views.maarif_kongresi, name='maarif_kongresi'),
    path('inkilap/baskomutanlik-kanunu/', views.baskomutanlik_kanunu, name='baskomutanlik_kanunu'),
    path('inkilap/sakarya-mudanya/', views.sakarya_mudanya, name='sakarya_mudanya'),
    path('inkilap/lozan-baris/', views.lozan_baris, name='lozan_baris'),
    path('inkilap/sanat-edebiyat/', views.sanat_edebiyat, name='sanat_edebiyat'),
    path('inkilap/unite-1/', views.inkilap_unite_1, name='inkilap_unite_1'),
    path('inkilap/cocukluk-donem/', views.cocukluk_donem, name='cocukluk_donem'),
    path('inkilap/fikir-hayati/', views.fikir_hayati, name='fikir_hayati'),
    path('inkilap/askerlik-hayati/', views.askerlik_hayati, name='askerlik_hayati'),
    path('ingilizce/', views.ingilizce, name='ingilizce'),
    path('matematik/uslu_ifadeler/', views.uslu_ifadeler, name='uslu_ifadeler'),
    path('matematik/uslu_foyler/', views.uslu_foyler, name='uslu_foyler'),
    path('matematik/uslu_islemler/', views.uslu_islemler, name='uslu_islemler'),
    path('matematik/uslu_ondalik/', views.uslu_ondalik, name='uslu_ondalik'),
    path('matematik/cebirsel-ifadeler/', views.cebirsel_ifadeler, name='cebirsel_ifadeler'),
    path('matematik/uslu_bilimsel/', views.uslu_bilimsel, name='uslu_bilimsel'),
    path('matematik/olasilik/', views.olasilik, name='olasilik'),
    path('din/', views.din, name='din'),
    path('oyunlar/', views.oyunlar, name='oyunlar'),
]
