import os
from PIL import Image
from collections import Counter

ruta_base = "/home/salvarado/TFM/Dataset_preparados/dataset_kanji_prep/dataset_original/images"

for split in ["train", "val", "test"]:
    print(f"\n=== {split} ===")
    ruta = os.path.join(ruta_base, split)
    archivos = [f for f in os.listdir(ruta) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

    tamanos = []
    for f in archivos:
        with Image.open(os.path.join(ruta, f)) as img:
            tamanos.append(img.size)  # (ancho, alto)

    contador = Counter(tamanos)
    print(f"Total imagenes: {len(tamanos)}")
    print(f"Tamanos distintos encontrados: {len(contador)}")
    for tamano, cantidad in contador.most_common():
        print(f"  {tamano}: {cantidad} imagenes")

