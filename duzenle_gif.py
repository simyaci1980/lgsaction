
import imageio
from PIL import Image, ImageDraw, ImageFont
import os


# İngilizce aylar ve Türkçeleri
ing_aylar = [
    "September", "October", "November", "December", "January", "February", "March", "April", "May"
]
tr_aylar = [
    "Eylül", "Ekim", "Kasım", "Aralık", "Ocak", "Şubat", "Mart", "Nisan", "Mayıs"
]


# Her kare için ay adını sırayla ekle
frame_labels = []
for ay in tr_aylar:
    frame_labels.append(ay)



# GIF dosya yolu
input_gif = "lgsweb/static/resimler/mevsimlerin_olusumu.gif"
output_gif = "lgsweb/static/resimler/mevsimlerin_olusumu_tr.gif"

# Font ayarı (Windows için)
font_path = "arial.ttf"  # Gerekirse font dosyasını static'e ekleyin
font_size = 18
font = ImageFont.truetype(font_path, font_size)

# GIF'i karelere ayır
reader = imageio.get_reader(input_gif)
frames = []
for i, frame in enumerate(reader):
    img = Image.fromarray(frame)
    draw = ImageDraw.Draw(img)
    # Sol üstteki eski metni kapat (beyaz dikdörtgen)
    draw.rectangle([(0, 0), (100, 28)], fill=(255,255,255,255))
    # Sırayla ay adını ekle
    if i < len(frame_labels):
        metin = frame_labels[i]
    else:
        metin = ""
    draw.text((10, 8), metin, font=font, fill=(0, 0, 0))
    frames.append(img)

# Yeni GIF olarak kaydet
frames[0].save(output_gif, save_all=True, append_images=frames[1:], duration=reader.get_meta_data()['duration'], loop=0)
print("Düzenlenmiş GIF kaydedildi:", output_gif)
