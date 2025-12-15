#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('lgsweb/templates/inkilap/dogu_guney_cepheleri.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Border-left renklerini gri (#555555) yerine temaya uygun renklere çevir
# Doğu Cephesi (Kırmızı)
content = content.replace('border-left:6px solid #555555; padding:20px; border-radius:8px; margin-top:24px;"><p><b style="color:#', 'border-left:6px solid #e85d5d; padding:20px; border-radius:8px; margin-top:24px;"><p><b style="color:#')
# Güney Cephesi (Mavi)
content = content.replace('border-left:6px solid #555555; padding:20px; border-radius:8px; margin-top:24px;"><p><b style="color:#3498db;', 'border-left:6px solid #3498db; padding:20px; border-radius:8px; margin-top:24px;"><p><b style="color:#3498db;')

# Ermenilerin Geçmiş Çıkışkınlıkları border (Kırmızı)
content = content.replace('border-left:6px solid #555555; padding:20px; border-radius:8px; margin-top:24px;"><p><b style="color:#e85d5d;', 'border-left:6px solid #e85d5d; padding:20px; border-radius:8px; margin-top:24px;"><p><b style="color:#e85d5d;')

# Ermenilerin Saldırıları border (Kırmızı)
content = content.replace('border-left:6px solid #555555; padding:20px; border-radius:8px; margin-top:24px;"><p><b style="color:#e85d5d;⚠️', 'border-left:6px solid #e85d5d; padding:20px; border-radius:8px; margin-top:24px;"><p><b style="color:#e85d5d;⚠️')

# İtilaf Devletleri border (Mavi)
content = content.replace('border-left:6px solid #555555; padding:20px; border-radius:8px; margin-top:24px;"><p><b style="color:#3498db;🌍', 'border-left:6px solid #3498db; padding:20px; border-radius:8px; margin-top:24px;"><p><b style="color:#3498db;🌍')

# Gümrü Antlaşması border (Kırmızı)
content = content.replace('border-left:6px solid #555555; padding:20px; border-radius:8px; margin-top:24px;"><h3 style="color:#e85d5d;', 'border-left:6px solid #e85d5d; padding:20px; border-radius:8px; margin-top:24px;"><h3 style="color:#e85d5d;')

with open('lgsweb/templates/inkilap/dogu_guney_cepheleri.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Borders updated!')
