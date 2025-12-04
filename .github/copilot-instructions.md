**Repo Özeti**
- Bu proje küçük bir Django web sitesidir (tek proje klasörü `lgsweb`). Statik dosyalar `lgsweb/static`, şablonlar `lgsweb/templates` altında bulunur. Veritabanı olarak proje kökünde `db.sqlite3` kullanılıyor.

**Hedef ve Mimari**
- Tek amaç: eğitim içeriklerini statik şablonlar aracılığıyla sunmak. Sunucu tarafı çok hafif — view fonksiyonları `lgsweb/views.py` içinde doğrudan `render()` kullanır.
- URL → View → Template akışı: yeni sayfa eklemek için `lgsweb/urls.py`'e bir `path()` ekleyin, `lgsweb/views.py` içinde karşılık gelen view fonksiyonunu oluşturun ve `lgsweb/templates/<katalog>/...html` olarak şablonu koyun.

**Hızlı Başlangıç / Geliştirme**
- Kök dizinde (Windows PowerShell) geliştirme sunucusunu başlatmak için:

```powershell
python manage.py migrate
python manage.py runserver
```

- Canlı içerik düzenleme: template, `lgsweb/static` içindeki CSS/JS veya view fonksiyonlarını değiştirdikten sonra sayfayı yenileyin.

**Örnek Tasarım Deseni (somut örnekler)**
- `lgsweb/urls.py` içindeki örnek:

```py
path('matematik/karekok_carpma_bolme/', views.karekok_carpma_bolme, name='karekok_carpma_bolme')
```

bu route, `lgsweb/views.py` içinde

```py
def karekok_carpma_bolme(request):
    return render(request, 'matematik/karekok_carpma_bolme.html')
```

şeklinde bir view ile doğrudan `lgsweb/templates/matematik/karekok_carpma_bolme.html` dosyasını render eder. Yeni sayfa eklerken bu üç dosyayı eşleştirin.

**Proje-özgü kurallar / konvansiyonlar**
- Tüm şablonlar `lgsweb/templates` altında konu bazlı klasörlere yerleştirilmiş (ör. `matematik/`, `turkce/`, `fen/`). Bu konvansiyona uyun.
- Basit view'lar `lgsweb/views.py` içinde fonksiyonel olarak tutuluyor — class-based view veya yeni uygulama (app) oluşturulmadan önce mevcut düzeni koruyun.
- Statik kaynaklar doğrudan `lgsweb/static` içine konur. CSS örneği: `lgsweb/static/dersler.css`.
- KaTeX gibi üçüncü taraf frontend kitaplıkları CDN üzerinden kullanılıyor (ör. KaTeX script'leri doğrudan template'lerde). Yerel paket bağımlılığı yok.

**Veritabanı ve konfigürasyon**
- `DATABASES` ayarında SQLite (`db.sqlite3`) kullanılıyor — migration'laraz önce `python manage.py migrate` çalıştırın.
- `settings.py`'de `DEBUG = True` ve sabit bir `SECRET_KEY` var; uzak ortama (public repo) gönderirken dikkat edin. (Bu dosya şu an geliştirici ortamı için ayarlı görünmektedir.)

**Değişiklik yaparken dikkat edilecekler**
- Yeni route eklerken: `lgsweb/urls.py` → `lgsweb/views.py` → `lgsweb/templates/...` üçgenini güncelleyin.
- Statik dosya değişiklikleri için `lgsweb/static` kullanın; `base.html` içinde `{% load static %}` kullanımı mevcut, yeni statik referansları bu şekilde ekleyin.
- JavaScript, KaTeX gibi betikler çoğunlukla şablon içine gömülü; daha karmaşık interaktivite gerekiyorsa `lgsweb/static/js/` altında dosya eklemeyi tercih edin.

**İpucu: Hata ayıklama ve rutin komutlar**
- Sunucu başlatma: `python manage.py runserver` (PowerShell). Eğer `ImportError` veya bağımlılık hatası alırsanız sanal ortamın aktif olup olmadığını kontrol edin.
- Veritabanı dosyası: `db.sqlite3` proje kökünde.

**Neler eksik / dikkat edilmesi gereken noktalar (AI için)**
- Projede custom Django app yapısı veya modeller yok; yeni veri modeline ihtiyaç varsa önce `INSTALLED_APPS`'e uygulama ekleyip migration oluşturun.
- Testler veya CI konfigürasyonu bulunmuyor. Otomatik test/formatlama talimatı verirken bunu belirtin.

**Proje Sahibi Tercihleri (Copilot için)**
- ❌ Uzun açıklamalar yapma
- ✅ Direkt kopyalanabilir kod ver
- ✅ Tek satır komutlar tercih et
- ✅ Hata mesajında anında çözüm sun
- ✅ Dosya yollarını tam yaz
- ❌ "Yapabilirsin, deneyebilirsin" gibi öneri cümleleri kurma
- ✅ Direkt "Şunu yap" tarzında yaz

**Sık Kullanılan Kalıplar**
```python
# Yeni view ekleme
def sayfa_adi(request):
    return render(request, 'matematik/sayfa_adi.html')
```

```python
# URL pattern
path('matematik/sayfa_adi/', views.sayfa_adi, name='sayfa_adi'),
```

**Otomatik Kontrol Listesi**
Her yeni sayfa eklendiğinde:
1. urls.py güncellendi mi?
2. views.py'de fonksiyon var mı?
3. Template oluşturuldu mu?
4. KaTeX CDN bir kez mi yükleniyor?
5. base.html extend edildi mi?

Eğer bu dosyada eksik gördüğünüz veya daha ayrıntı isterseniz belirtin — içerikleri proje özelinde genişleteyim.

*** Son güncelleme: Otomatik olarak oluşturuldu — lütfen geri bildirim verin. ***
