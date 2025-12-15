#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob

# İnkilap klasöründeki tüm HTML dosyalarını al
inkilap_dir = 'lgsweb/templates/inkilap'
html_files = glob.glob(os.path.join(inkilap_dir, '*.html'))

# Zaten yapıldı olanları atla
already_done = {
    'baskomutanlik_kanunu.html',
    'maarif_kongresi.html',
    'bati_cepheleri.html',
    'dogu_guney_cepheleri.html'
}

for file_path in sorted(html_files):
    filename = os.path.basename(file_path)
    
    if filename in already_done:
        print(f"Skipping {filename} (already done)")
        continue
    
    print(f"Processing {filename}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Dark-theme script ekle (eğer yoksa)
    if 'document.body.classList.add(\'dark-theme\')' not in content:
        if '{% block extra_head %}' in content and '<script>' not in content.split('{% block extra_head %}')[1].split('{% endblock %}')[0]:
            # Script ekle
            script_injection = '''    <script>
        document.addEventListener('DOMContentLoaded', function() {
            document.body.classList.add('dark-theme');
        });
    </script>'''
            content = content.replace('{% block extra_head %}', '{% block extra_head %}\n' + script_injection)
    
    # 2. Tüm renkleri güncelle - eski paletler
    replacements = [
        # Eski renk paletleri -> Yeni sistem
        ('#f5f5f5', ''),  # açık gri arka plan -> kaldır
        ('#e8eaf6', ''),  # açık mavi -> kaldır
        ('#fff9c4', ''),  # açık sarı -> kaldır
        ('#f1f8e9', ''),  # açık yeşil -> kaldır
        ('#fff3e0', ''),  # açık turuncu -> kaldır
        ('#ffebee', ''),  # açık kırmızı -> kaldır
        ('background:#c5cae9', 'background:#555555'),  # mavi arka plan
        ('background:#e8eaf6', ''),  # kaldır
        ('background:#f1f8e9', ''),  # kaldır
        ('background:#fff3e0', ''),  # kaldır
        ('background:#fff9c4', ''),  # kaldır
        ('background:#ffebee', ''),  # kaldır
        ('background:#fff;', 'background:#2a2a2a;'),  # beyaz -> koyu gri
        ('background:#fff', 'background:#2a2a2a'),  # beyaz -> koyu gri
        
        # Metin renkleri
        ('color:#283593', 'color:#d4d4d4'),  # koyu mavi -> gri
        ('color:#1a237e', 'color:#d4d4d4'),  # çok koyu mavi -> gri
        ('color:#3949ab', 'color:#b8b8b8'),  # mavi -> gri (başlıklar)
        ('color:#c62828', 'color:#e85d5d'),  # kırmızı -> açık kırmızı (işaret)
        ('color:#d32f2f', 'color:#e85d5d'),  # kırmızı -> açık kırmızı
        ('color:#2e7d32', 'color:#2ecc71'),  # yeşil -> açık yeşil
        ('color:#1565c0', 'color:#3498db'),  # mavi -> açık mavi
        ('color:#34495e', 'color:#c8c8c8'),  # gri -> açık gri
        ('color:#555', 'color:#c8c8c8'),  # gri -> açık gri
        ('color:#e65100', 'color:#f39c12'),  # turuncu -> açık turuncu
        ('color:#f57f17', 'color:#f39c12'),  # turuncu -> açık turuncu
        ('color:#c77a3a', 'color:#d4d4d4'),  # turuncu -> gri
        ('color:#a0632f', 'color:#c8c8c8'),  # kahverengi -> gri
        ('color:white', 'color:#d4d4d4'),  # beyaz -> gri
        
        # Border renkleri
        ('border-left:6px solid #c62828', 'border-left:6px solid #e85d5d'),
        ('border-left:6px solid #2e7d32', 'border-left:6px solid #2ecc71'),
        ('border-left:6px solid #1565c0', 'border-left:6px solid #3498db'),
        ('border-left:6px solid #e65100', 'border-left:6px solid #f39c12'),
        ('border-left:6px solid #f57f17', 'border-left:6px solid #f39c12'),
        ('border-left:4px solid #c62828', 'border-left:4px solid #e85d5d'),
        ('border-left:4px solid #f57f17', 'border-left:4px solid #f39c12'),
        
        # Button renkleri
        ('background:#c5cae9;', 'background:#555555;'),
        ('background:#c62828;', 'background:#444444;'),
        ('background:#1565c0;', 'background:#444444;'),
        ('background:#2e7d32;', 'background:#444444;'),
        ('background:#e65100;', 'background:#444444;'),
    ]
    
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
    
    # 3. Harita container arka planını kaldır
    content = content.replace('style="margin:32px 0; background:#f5f5f5; padding:20px; border-radius:12px;"', 'style="margin:32px 0; padding:20px; border-radius:12px;"')
    content = content.replace('style="margin-top:32px; margin-bottom:32px; background:#f5f5f5; padding:20px; border-radius:12px;"', 'style="margin-top:32px; margin-bottom:32px; padding:20px; border-radius:12px;"')
    
    # 4. Renksiz inline style'ları temizle
    content = content.replace('style="background:#f5f5f5; padding', 'style="padding')
    content = content.replace('style="background:#fff; ', 'style="background:#2a2a2a; ')
    content = content.replace('background:#f5f5f5;', '')
    content = content.replace('background:#e8eaf6;', '')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ {filename} updated")

print("\nAll files processed!")
