#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('lgsweb/templates/inkilap/dogu_guney_cepheleri.html', 'r', encoding='utf-8') as f:
    content = f.read()

# İçerik başlıklarını renkli yap - bölüm başlıkları (#b8b8b8 - gri) kalacak

# Doğu Cephesi içerik başlıkları (Kırmızı #e85d5d)
content = content.replace('style="color:#b8b8b8;">Tanım:</b> <span', 'style="color:#e85d5d;">Tanım:</b> <span', 1)  # Doğu Cephesi tanımı
content = content.replace('📜 Ermenilerin Geçmiş</b>', '📜 Ermenilerin Geçmiş</b>').replace('style="color:#b8b8b8;\">📜 Ermenilerin', 'style="color:#e85d5d;\">📜 Ermenilerin')
content = content.replace('⚠️ Ermenilerin Saldırıları</b>', '⚠️ Ermenilerin Saldırıları</b>').replace('style="color:#b8b8b8;\">⚠️ Ermenilerin Saldırıları', 'style="color:#e85d5d;\">⚠️ Ermenilerin Saldırıları')

# 📅 8 Haziran 1920 (Kırmızı)
content = content.replace('📅 8 Haziran 1920 - Seferberlik Kararı:</b>', 'style="color:#e85d5d;">📅 8 Haziran 1920 - Seferberlik Kararı:</b>').replace('style="color:#b8b8b8;\">📅', 'style="color:#e85d5d;\">📅')

# 🎖️ 15 Haziran 1920 (Kırmızı)
content = content.replace('🎖️ 15 Haziran 1920 - BMM\'nin Kararı:</b>', '').replace('style="color:#b8b8b8;\">🎖️ 15 Haziran', 'style="color:#e85d5d;\">🎖️ 15 Haziran')

# Gümrü Antlaşması (Kırmızı)
content = content.replace('📜 Gümrü Antlaşması</h3>', '').replace('style="color:#b8b8b8; margin-top:0;\">📜 Gümrü', 'style="color:#e85d5d; margin-top:0;\">📜 Gümrü')

# Antlaşmanın Hükümleri (Kırmızı)
content = content.replace('Antlaşmanın Hükümleri:</b>', '').replace('style="color:#b8b8b8;\">Antlaşmanın', 'style="color:#e85d5d;\">Antlaşmanın')

# BMM başarısı (Yeşil #2ecc71)
content = content.replace('BMM\'nin ilk askerî başarısı, Gümrü Antlaşması ise ilk siyasi başarısıdır</b>', '<b style="color:#2ecc71;">BMM\'nin ilk askerî başarısı, Gümrü Antlaşması ise ilk siyasi başarısıdır</b>').replace('style="color:#b8b8b8;\">BMM', 'style="color:#2ecc71;\">BMM')

# Güney Cephesi - Tanım (Mavi #3498db)
content = content.replace('Güney Cephesi</h2>', 'Güney Cephesi</h2>')  # Başlık gri kalacak
# "Tanım" ikinci kez geldiğinde (Güney Cephesi)
lines = content.split('\n')
count = 0
for i, line in enumerate(lines):
    if 'style="color:#b8b8b8;">Tanım:</b>' in line and 'Güney Anadolu' in lines[i]:
        lines[i] = line.replace('style="color:#b8b8b8;">Tanım:', 'style="color:#3498db;">Tanım:')
        break
content = '\n'.join(lines)

# 🌍 İtilaf Devletleri (Mavi #3498db)
content = content.replace('🌍 İtilaf Devletlerinin Güney İşgalleri:</b>', '').replace('style="color:#b8b8b8;\">🌍', 'style="color:#3498db;\">🌍')

# Maraş Savunması - Turuncu #f39c12
content = content.replace('🏛️ Maraş Savunması</h3>', '').replace('style="color:#b8b8b8; text-align:center;\">🏛️ Maraş', 'style="color:#f39c12; text-align:center;\">🏛️ Maraş')

# 📜 Sütçü İmam Olayı (Turuncu)
content = content.replace('📜 Sütçü İmam Olayı - Direniş Başlangıcı:</b>', '').replace('style="color:#b8b8b8;\">📜 Sütçü', 'style="color:#f39c12;\">📜 Sütçü')

# 🚩 Organize Direniş (Turuncu)
content = content.replace('🚩 Organize Direniş:</b>', '').replace('style="color:#b8b8b8;\">🚩', 'style="color:#f39c12;\">🚩')

# 🎯 Şahin Bey (Yeşil #2ecc71)
content = content.replace('🎯 Şahin Bey - Direnişin Sembol İsmi:</b>', '').replace('style="color:#b8b8b8;\">🎯', 'style="color:#2ecc71;\">🎯')

# Kılıç Ali Bey (Turuncu)
content = content.replace('Kılıç Ali Bey Dönemi (Şahin Bey\'den Sonra):</b>', '').replace('style="color:#b8b8b8;\">Kılıç Ali', 'style="color:#f39c12;\">Kılıç Ali')

with open('lgsweb/templates/inkilap/dogu_guney_cepheleri.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Content titles colored!')
