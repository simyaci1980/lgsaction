# LGS Action - Eğitim Platformu

Django tabanlı eğitim içerikleri sunma platformu.

## 🚀 Özellikler

- **Matematik Modülü:**
  - Karekök Çarpma/Bölme İşlemleri
  - Karekök a√b Formülü (düzeltildi ✅)
  - Ondalık İfadeler ve Gerçek Sayılar (yeni ✨)

## 📦 Kurulum

```powershell
# Sanal ortam oluştur
python -m venv venv

# Sanal ortamı aktifleştir (Windows)
.\venv\Scripts\activate

# Bağımlılıkları yükle
pip install django

# Veritabanı migration
python manage.py migrate

# Sunucuyu başlat
python manage.py runserver
```

## 🛠️ Geliştirme

### Yeni Sayfa Ekleme

1. `lgsweb/urls.py` → Route ekle
2. `lgsweb/views.py` → View fonksiyonu yaz
3. `lgsweb/templates/` → HTML şablonu oluştur

### Teknolojiler

- Django 5.x
- KaTeX (matematik formülleri)
- Vanilla JavaScript
- SQLite

## 📝 Son Güncellemeler

- ✅ `karekok_akokb.html` tekrar eden kodlar temizlendi
- ✅ `karekok_ondalik.html` dropdown sıralama eklendi
- ✅ JavaScript syntax hataları düzeltildi

## 💡 Teknik Çözümler

### Karekök İşareti (√) Gösterimi

**Problem:** HTML içinde karekök işaretini input alanıyla birlikte matematiksel olarak doğru göstermek.

**Denenen Yöntemler:**
- ❌ KaTeX `$\sqrt{$` - Render problemi
- ❌ Unicode `√` + `text-decoration: overline` - Input kutusu görünmedi
- ❌ HTML entity ile border-top - Hizalama sorunları

**Çalışan Çözüm (SVG + Absolute Positioning):**

```html
<div style="display: inline-block; position: relative; margin-right: 8px;">
    <!-- SVG ile karekök sembolü çiz -->
    <svg width="70" height="40" viewBox="0 0 70 40" style="display: block;">
        <path d="M3 35 L10 35 L18 10 L68 10" 
              stroke="#1976d2" 
              stroke-width="2.5" 
              fill="none" 
              stroke-linecap="round" 
              stroke-linejoin="round"/>
    </svg>
    
    <!-- Üst çizgi -->
    <div style="position: absolute; top: 7px; left: 18px; right: 2px; height: 2.5px; background: #1976d2;"></div>
    
    <!-- Input alanı (absolute) -->
    <input type="number" 
           id="q1" 
           placeholder="?" 
           style="position: absolute; 
                  top: 12px; 
                  left: 22px; 
                  width: 42px; 
                  padding: 2px 4px; 
                  font-size: 1em; 
                  border: none; 
                  background: transparent; 
                  text-align: center; 
                  outline: none;">
</div>
```

**Avantajlar:**
- ✅ Matematiksel olarak doğru görünüm
- ✅ Responsive tasarım
- ✅ Input kök çizgisinin altında
- ✅ KaTeX render sorunları yok

**Kullanım Örneği:** `lgsweb/templates/matematik/karekok_carpma_bolme.html` (Soru 1, 2, 3)

**Not:** Tüm interaktif karekök ifadelerinde ve input ile birlikte gösterim gereken her yerde bu SVG + absolute input yöntemi kullanılmalıdır. KaTeX ile input birleştirme denemeleri hatalıdır; input kutusu mutlaka SVG kök çizgisiyle birleştirilmelidir. Stil ve kod örneği bu dosyada referans alınmalıdır.

---

### Olasılık Sayfası Tasarım Stili (Beğenilen Stil ⭐)

**Dosya:** `lgsweb/templates/matematik/olasilik.html`

**Temel Özellikler:**
- 📐 Font: `Segoe UI`, 18px base font, line-height 1.8
- 🎨 Ana renk paleti: Turuncu tonları (`#e65100`, `#f57c00`, `#fff3e0`)
- 📦 Kapsayıcı: max-width 900px, ortalanmış

**Tasarım Bileşenleri:**

1. **Konu Kutuları:**
```css
background: #fff3e0;
padding: 24px;
border-radius: 12px;
margin: 24px 0;
```

2. **Alt Kartlar (Tanımlar):**
```css
background: white;
padding: 16px;
border-radius: 8px;
border-left: 4px solid #f57c00;
```

3. **Örnek Kutuları:**
```css
background: #ffffff;
border-left: 6px solid #f57c00;
padding: 20px;
border-radius: 8px;
box-shadow: 0 2px 8px rgba(0,0,0,0.1);
```

4. **Yüzen Dekoratif İkonlar:**
```css
.floating-icon {
    position: absolute;
    font-size: 3em;
    opacity: 0.15;
    pointer-events: none;
    z-index: 0;
}
```
- Emoji ikonlar: 🎲🎯🎰🎪🎡💰🃏🎮🎨🎭
- Sayfanın sağ ve solunda dağıtılmış
- Mobile'da gizlenir (`@media max-width: 768px`)

5. **Tipografi:**
- Strong etiketler: `font-weight: 600`, renk vurguları
- Başlıklar: `line-height: 1.4`
- Paragraflar: `line-height: 1.7`
- İtalik açıklamalar: `color: #666`

**Neden İyi Görünüyor:**
- ✅ Temiz, havadar layout (24px marginler)
- ✅ Görsel hiyerarşi (renk, boyut, border)
- ✅ İlgi çekici emoji kullanımı
- ✅ Yüzen ikonlar sayede canlı görünüm
- ✅ 13 yaş hedef kitle için ideal: sıkmayan, eğlenceli ama profesyonel

**Yeniden Kullanım:** Diğer matematik konularına (geometri, cebir vb.) aynı stil uygulanabilir, sadece renk paletini değiştir.

---

### CSS Container Sınıfı Kullanımı

**Problem:** `brochure-container` sınıfı CSS'de tanımlı değildi, içerik ortalanmıyordu.

**Çözüm:** Mevcut `.container` sınıfına geçildi.

**Etkilenen Dosyalar:**
- `lgsweb/templates/matematik/uslu_ifadeler.html`
- `lgsweb/templates/matematik/uslu_islemler.html`

**CSS Kuralı (`dersler.css`):**
```css
.container {
    max-width: 1000px;
    margin: 40px auto;
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    padding: 32px;
}
```

**Not:** Yeni sayfa eklerken içeriği ortalamak için `<div class="container">` kullan, `brochure-container` kullanma.

---

### Fen Ünitesi Ara Sayfası Stili (Beğenilen Stil ⭐)

**Dosya:** `lgsweb/templates/fen/fen_unite_1.html`

**Temel Özellikler:**
- 📐 Layout: Tek kolon grid (`grid-template-columns: 1fr`)
- 📦 Maksimum genişlik: 800px, ortalanmış
- 🎨 Gradient kartlar: 135deg açılı, aktif konular canlı renk
- 📱 Responsive: Mobilde otomatik uyumlu

**Tasarım Bileşenleri:**

1. **Başlık ve Alt Başlık:**
```html
<h1 class="main-title">1. ÜNİTE: MEVSİMLER VE İKLİM 🌍</h1>
<p style="text-align:center; color:#666; font-size:1.1em; margin-bottom:40px;">
    Bu ünitede Dünya'nın hareketleri, mevsimler ve iklim konularını öğreneceğiz.
</p>
```

2. **Tek Kolon Grid Container:**
```html
<div style="display:grid; grid-template-columns:1fr; gap:20px; max-width:800px; margin:0 auto;">
```

3. **Aktif Konu Kartı:**
```html
<a href="/fen/mevsimler-iklim/" 
   style="display:block; 
          background:linear-gradient(135deg, #2196F3 0%, #1976d2 100%); 
          padding:24px; 
          border-radius:12px; 
          text-decoration:none; 
          color:white; 
          box-shadow:0 4px 12px rgba(0,0,0,0.15); 
          transition:transform 0.2s;" 
   onmouseover="this.style.transform='translateY(-4px)'" 
   onmouseout="this.style.transform='translateY(0)'">
    <div style="display:flex; align-items:center; gap:16px;">
        <div style="font-size:3em;">🌍</div>
        <div style="flex:1;">
            <h2 style="margin:0; font-size:1.4em; color:white;">Mevsimler ve İklim</h2>
            <p style="margin:8px 0 0 0; opacity:0.9; font-size:0.95em;">
                Dünya'nın hareketleri, eksen eğikliği...
            </p>
        </div>
        <div style="font-size:2em;">→</div>
    </div>
</a>
```

4. **Kilitli/Hazırlanıyor Konu Kartı (Eskisi):**
```html
<div style="display:block; 
            background:linear-gradient(135deg, #90caf9 0%, #64b5f6 100%); 
            padding:24px; 
            border-radius:12px; 
            color:white; 
            box-shadow:0 4px 12px rgba(0,0,0,0.1); 
            opacity:0.7;">
    <div style="display:flex; align-items:center; gap:16px;">
        <div style="font-size:3em;">🌡️</div>
        <div style="flex:1;">
            <h2 style="margin:0; font-size:1.4em; color:white;">İklim Olayları</h2>
            <p style="margin:8px 0 0 0; opacity:0.9; font-size:0.95em;">
                (Yakında eklenecek)
            </p>
        </div>
        <div style="font-size:1.5em; opacity:0.5;">🔒</div>
    </div>
</div>
```

**Renk Paletleri (Fen için):**
- Mavi: `#2196F3`, `#1976d2` (Ana konu rengi)
- Teal/Yeşil: `#00897b`, `#00695c` (İkinci konu)
- Açık mavi: `#90caf9`, `#64b5f6` (Kilitli durum)

**Avantajlar:**
- ✅ Tek kolon = Mobilde düzen bozulmaz
- ✅ Hover efekti = Etkileşimli, modern
- ✅ Gradient = Görsel derinlik
- ✅ Emoji + Ok = Net navigasyon
- ✅ Opacity 0.7 = Kilitli konular belli

**Kullanım Kuralı:**
- 🔧 Tüm fen ünitesi ara sayfaları (`fen_unite_1.html`, `fen_unite_2.html`, vb.) bu stili kullanmalı
- 🎨 Renk değişimi: Her ünite için farklı gradient tonları seçilebilir
- 📝 İçerik: Ünite başlığı + kısa açıklama + konu kartları

**Örnek Uygulama:**
```
fen.html (7 ünite kartı)
  └─ fen_unite_1.html (2 konu kartı - TEK KOLON)
       ├─ mevsimler_iklim.html
       └─ iklim_olaylari.html
```

---

### Dark Theme İçerik Sayfası - Renkli Yazı ve Görünür İkonlar (İnkılap Tarihi)

**Dosya:** `lgsweb/templates/inkilap/dunyasavasi_1.html`

**Dark Theme Aktivasyon:**
```html
{% block extra_head %}
<link rel="stylesheet" href="/static/dersler.css">
<script>
    document.addEventListener('DOMContentLoaded', function() {
        document.body.classList.add('dark-theme');
    });
</script>
{% endblock %}
```

**CSS'den Kural:**
- Siyah arka plan (#0d0d0d - #1a1a1a gradient)
- Container'lar: #1e1e1e, #282828, #333333
- Default yazı rengi: #c8c8c8 gri

**Yazı Renglendirilmesi (Önemli!):**
```html
<!-- Başlık (kalın) - Renkli -->
<b style="color:#3498db;">I. Dünya Savaşı:</b>

<!-- Normal metin - BEYAZ (#ffffff) -->
<span style="color:#ffffff;">Tarihin kaydettiği ilk küresel savaştır...</span>
```

**Neden Beyaz?**
- Siyah arka plan üzerinde #c8c8c8 gri = Soluk görülüyor
- #ffffff beyaz = Dark theme'de maksimum kontras ve okunabilirlik
- Başlık renglerinin (mavi, kırmızı, turuncu) yanında ayırım yapar

**Renk Kodlaması (Semantik):**
- 🔵 **Mavi (#3498db):** Savaşın Nedenleri bölümü başlıkları
- 🔴 **Kırmızı (#e85d5d):** Bloklaşmalar ve İttifaklar bölümü
- 🟠 **Turuncu (#f39c12):** Savaşın Başlaması ve Gelişmesi bölümü

**Floating İkonlar - Görünürlük:**
```html
<!-- Soluk değil, PARLAK glow ile -->
<div class="floating-icon" 
     style="top:120px; left:-60px; 
             opacity:1; 
             filter:drop-shadow(0 0 8px rgba(52, 152, 219, 0.6));">⚔️</div>
```

**İkon Özellikleri:**
- `opacity: 1` = Tam görünür (0.15 değil!)
- `filter: drop-shadow(...)` = Renkli halo efekti
- Mavi ikonlar (sol taraf) = #3498db glow
- Turuncu ikonlar (sağ taraf) = Kendi renkleri glow
- Halo işaretleri: 8px bulanıklık, %60 opasite

**Yazı vs İkon Özeti:**

| Eleman | Renk | Opasite | Neden |
|--------|------|---------|-------|
| **Başlık (b tag)** | #3498db, #e85d5d, #f39c12 | 100% | Bölüm tanımlaması |
| **Normal Metin (span)** | #ffffff BEYAZ | 100% | Dark theme'de okunabilirlik |
| **Yüzen İkonlar** | Emoji (belli) | 100% | Görsel dekorasyon, parlak glow |

**Yeniden Kullanım Kuralı:**
1. Dark theme script ✅
2. Normal yazılar: #ffffff beyaz ✅
3. Bölüm başlıkları: Renkli (kodu #3498db vb.) ✅
4. Yüzen ikonlar: `opacity:1` + `filter:drop-shadow()` ✅
5. Kutular: Border-left renk, arka plan SİYAH (açık renk yok) ✅

