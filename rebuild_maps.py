#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# Basit harita şablonu - bölüm başında ve sonunda
map_html = '''    <!-- LEAFLET HARİTA -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>
    
    <div style="margin:32px 0; padding:20px; border-radius:12px;">
        <h3 style="margin-top:0; text-align:center;">📍 Harita</h3>
        <div id="map" style="width:100%; height:500px; border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,0.3);"></div>
    </div>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            if (document.getElementById('map')) {
                const map = L.map('map').setView([39.0, 35.0], 6);
                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    attribution: '© OpenStreetMap',
                    maxZoom: 19
                }).addTo(map);
            }
        });
    </script>
'''

# Harita dosyaları
map_files = {
    'lgsweb/templates/inkilap/bati_cepheleri.html': 'Batı Cephesi Haritası',
    'lgsweb/templates/inkilap/dogu_guney_cepheleri.html': 'Doğu ve Güney Cepheleri Haritası',
    'lgsweb/templates/inkilap/askerlik_hayati.html': 'Askerlik Görevleri Haritası',
}

for file_path, desc in map_files.items():
    print(f"Processing {os.path.basename(file_path)} - {desc}...")
    
    # Dosyayı oku
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Eski harita kodunu kaldır (<!-- LEAFLET HARİTA --> ile başlayan bölümü)
    import re
    
    # Tüm harita bloğunu kaldır
    pattern = r'<!-- LEAFLET HARİTA -->.*?</script>\s*'
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # Eğer section'ın hemen sonrasında (<!-- LEAFLET --> varsa bunu kaldır
    pattern = r'<div style="margin:32px 0;[^}]*</script>\s*'
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # <section class="section"> öncesine harita ekle
    if '<section class="section">' in content:
        content = content.replace('<section class="section">', map_html + '\n    <section class="section">', 1)
    elif '<div class="container">' in content and 'section' not in content:
        # Container varsa ondan sonra ekle
        content = content.replace('<div class="container">', '<div class="container">\n' + map_html, 1)
    
    # Yazıp kaydet
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ {os.path.basename(file_path)} updated")

print("\nHarita kodları yenilendi!")
