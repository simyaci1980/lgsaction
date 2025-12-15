#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('lgsweb/templates/inkilap/dogu_guney_cepheleri.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Tüm #b8b8b8 renkleri bölüm başlıklarında kalacak
# İçerik renkleri: Doğu Cephesi (Kırmızı #e85d5d), Güney Cephesi (Mavi #3498db), Maraş (Turuncu #f39c12), Antep (Yeşil #2ecc71)

# İpuçlarını renkli yap
content = content.replace('💡 İpucu 1:</b>: Doğu', '💡 İpucu 1:</b>: Doğu')  # keep it
content = content.replace('style="color:#b8b8b8;">💡 İpucu 1:', 'style="color:#e85d5d;">💡 İpucu 1:')
content = content.replace('style="color:#b8b8b8;">💡 İpucu 2:', 'style="color:#e85d5d;">💡 İpucu 2:')
content = content.replace('style="color:#b8b8b8;">💡 İpucu 3:', 'style="color:#3498db;">💡 İpucu 3:')
content = content.replace('style="color:#b8b8b8;">💡 İpucu 4:', 'style="color:#f39c12;">💡 İpucu 4:')
content = content.replace('style="color:#b8b8b8;">💡 İpucu 5:', 'style="color:#2ecc71;">💡 İpucu 5:')
content = content.replace('style="color:#b8b8b8;">💡 İpucu 6:', 'style="color:#f39c12;">💡 İpucu 6:')

with open('lgsweb/templates/inkilap/dogu_guney_cepheleri.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Colors updated!')
