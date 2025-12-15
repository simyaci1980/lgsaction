#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

files = [
    'lgsweb/templates/inkilap/bati_cepheleri.html',
    'lgsweb/templates/inkilap/dogu_guney_cepheleri.html',
    'lgsweb/templates/inkilap/askerlik_hayati.html'
]

for fname in files:
    if not os.path.exists(fname):
        print(f"❌ Dosya bulunamadı: {fname}")
        continue
    
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # === 1. Eski initMap fonksiyonunu sil (ilk script bloğu) ===
    pattern1 = r'<script>\s*function initMap\(\) \{[^}]*\}[\s\S]*?document\.addEventListener\([\'"]DOMContentLoaded[\'"]\s*,\s*initMap\s*\);[\s\S]*?</script>'
    content = re.sub(pattern1, '', content, flags=re.DOTALL)
    
    # === 2. İkinci harita bölümünün <!-- LEAFLET HARİTA --> ile başlayan tüm scripti sil ===
    pattern2 = r'<!-- LEAFLET HARİTA -->[\s\S]*?</script>'
    content = re.sub(pattern2, '', content, flags=re.DOTALL)
    
    # === 3. Boş style attribute'leri temizle ===
    content = re.sub(r'style="\s*;\s*"', 'style=""', content)
    content = re.sub(r'style=";', 'style=""', content)
    
    # === 4. Eksik CSS propertylerini temizle ===
    content = re.sub(r'background-;', '', content)
    content = re.sub(r'border-;', '', content)
    content = re.sub(r'border-left-;', '', content)
    content = re.sub(r'margin:;\s*', '', content)
    
    # === 5. Leaflet CDN yinelemelerini temizle ===
    lines = content.split('\n')
    seen_leaflet_css = False
    seen_leaflet_js = False
    cleaned_lines = []
    
    for line in lines:
        if 'leaflet.min.css' in line:
            if not seen_leaflet_css:
                cleaned_lines.append(line)
                seen_leaflet_css = True
        elif 'leaflet.min.js' in line:
            if not seen_leaflet_js:
                cleaned_lines.append(line)
                seen_leaflet_js = True
        else:
            cleaned_lines.append(line)
    
    content = '\n'.join(cleaned_lines)
    
    # === 6. Dosyaya yazınız ===
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {fname} temizlendi")

print("\n🎯 Harita temizliği tamamlandı!")
