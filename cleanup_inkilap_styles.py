#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import re

inkilap_dir = 'lgsweb/templates/inkilap'
html_files = glob.glob(os.path.join(inkilap_dir, '*.html'))

for file_path in sorted(html_files):
    filename = os.path.basename(file_path)
    
    print(f"Cleaning {filename}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. Tüm inline style color/background'ları kaldır (sadece CSS'e bırak)
    # Örnek: style="color:#b8b8b8;" -> style=""  sonra da style="" kaldır
    
    # background: kaldır
    content = re.sub(r';\s*background:[^;]*', '', content)
    content = re.sub(r'\s*background:[^;]*;', ';', content)
    
    # color: kaldır
    content = re.sub(r';\s*color:[^;]*', '', content)
    content = re.sub(r'\s*color:[^;]*;', ';', content)
    
    # Boş style attribute'ları kaldır
    content = re.sub(r'\s+style=""\s*', ' ', content)
    content = re.sub(r'\s+style=\'\'\s*', ' ', content)
    
    # border renkleri kaldır ama border-radius gibi şeyleri tut
    content = re.sub(r';\s*border:[^;]*solid\s+#[0-9a-f]{6}', '', content, flags=re.IGNORECASE)
    content = re.sub(r'\s*border:[^;]*solid\s+#[0-9a-f]{6}', '', content, flags=re.IGNORECASE)
    content = re.sub(r';\s*border-left:[^;]*solid\s+#[0-9a-f]{6}', '', content, flags=re.IGNORECASE)
    
    # Boş padding/margin value'ları temizle (sadece önemli property'leri tut)
    # opacity, z-index gibi değerleri tut ama renkleri kaldır
    
    # Inline background attribute'ları CSS'e devret
    # style="background:#xyz; padding..." -> style="padding..."
    
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ {filename} cleaned")
    else:
        print(f"  - {filename} (no changes)")

print("\nCleanup completed! Now all styling comes from dersler.css")
