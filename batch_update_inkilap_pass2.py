#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob

# İnkilap klasöründeki tüm HTML dosyalarını al
inkilap_dir = 'lgsweb/templates/inkilap'
html_files = glob.glob(os.path.join(inkilap_dir, '*.html'))

for file_path in sorted(html_files):
    filename = os.path.basename(file_path)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # İkinci pass: Kalan renkleri güncelle
    replacements = [
        # Harita ve diğer elementler
        ('border:2px solid #c62828;', 'border:2px solid #b8b8b8;'),
        ('border:2px solid #1565c0;', 'border:2px solid #b8b8b8;'),
        ('border:2px solid #2e7d32;', 'border:2px solid #b8b8b8;'),
        ('border:2px solid #e65100;', 'border:2px solid #b8b8b8;'),
        
        # Table background
        ('background:#e3f2fd;', 'background:#333333;'),
        ('background:#f1f8e9;', 'background:#333333;'),
        ('background:#fff3e0;', 'background:#333333;'),
        ('background:#ffebee;', 'background:#333333;'),
        ('background:#fff9c4;', 'background:#333333;'),
        ('background:#e8eaf6;', 'background:#333333;'),
        ('background:#f5f5f5;', ''),
        
        # Daha fazla metin renkleri
        ('color:#3f51b5;', 'color:#d4d4d4;'),
        ('color:#1976d2;', 'color:#d4d4d4;'),
        ('color:#0288d1;', 'color:#d4d4d4;'),
        ('color:#388e3c;', 'color:#2ecc71;'),
        ('color:#d32f2f;', 'color:#e85d5d;'),
        ('color:#7b1fa2;', 'color:#d4d4d4;'),
        ('color:#f57c00;', 'color:#f39c12;'),
        ('color:#0097a7;', 'color:#3498db;'),
        ('color:#455a64;', 'color:#c8c8c8;'),
        
        # Box shadow - dark theme uyuş
        ('box-shadow:0 2px 8px rgba(0,0,0,0.1);', 'box-shadow:0 2px 8px rgba(0,0,0,0.3);'),
    ]
    
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
    
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {filename} updated (second pass)")
    else:
        print(f"- {filename} (no changes needed)")

print("\nSecond pass completed!")
