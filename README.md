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


## 📄 Lisans

Eğitim amaçlı proje.
