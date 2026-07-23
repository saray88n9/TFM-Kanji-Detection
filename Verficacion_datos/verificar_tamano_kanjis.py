import os

ruta_images = "/home/salvarado/TFM/Dataset_preparados/dataset_kanji_prep/dataset_original/images/train"
ruta_labels = "/home/salvarado/TFM/Dataset_preparados/dataset_kanji_prep/dataset_original/labels/train"

# Todas las imagenes del dataset miden 9922x7012 (ya verificado antes)
img_ancho = 9922
img_alto = 7012

anchos_px = []
altos_px = []

archivos_labels = [f for f in os.listdir(ruta_labels) if f.lower().endswith(".txt")]

for archivo in archivos_labels:
    ruta_archivo = os.path.join(ruta_labels, archivo)
    with open(ruta_archivo, "r") as f:
        for linea in f:
            partes = linea.strip().split()
            if len(partes) != 5:
                continue
            clase, cx, cy, ancho_norm, alto_norm = partes
            ancho_px = float(ancho_norm) * img_ancho
            alto_px = float(alto_norm) * img_alto
            anchos_px.append(ancho_px)
            altos_px.append(alto_px)

print(f"Total de kanjis analizados (en las 55 paginas de train): {len(anchos_px)}")
print(f"Ancho medio: {sum(anchos_px)/len(anchos_px):.1f} px  (el ejemplo usaba 133 px)")
print(f"Alto medio: {sum(altos_px)/len(altos_px):.1f} px  (el ejemplo usaba 85 px)")
print(f"Ancho minimo: {min(anchos_px):.1f} px, Ancho maximo: {max(anchos_px):.1f} px")
print(f"Alto minimo: {min(altos_px):.1f} px, Alto maximo: {max(altos_px):.1f} px")

