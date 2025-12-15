#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import re

inkilap_dir = 'lgsweb/templates/inkilap'
html_files = glob.glob(os.path.join(inkilap_dir, '*.html'))

for file_path in sorted(html_files):
    filename = os.path.basename(file_path)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Boş style attribute'ları kaldır
    content = re.sub(r'\s+style=""\s*', ' ', content)
    content = re.sub(r'\s+style=\'\'\s*', ' ', content)
    content = re.sub(r'\s+style=""\s+', ' ', content)
    
    # Eksik property değerleri düzelt (background-; gibi)
    content = re.sub(r'background-;\s*', '', content)
    content = re.sub(r';\s*background-;', ';', content)
    
    # Çift semicolon'ları düzelt
    content = re.sub(r';+', ';', content)
    
    # Boş style attribute'ları (sadece whitespace'li) kaldır
    content = re.sub(r'style="\s*"', '', content)
    content = re.sub(r"style='\s*'", '', content)
    
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {filename} - Final cleanup")
    else:
        print(f"- {filename} - No issues")

print("\nFinal cleanup completed!")
