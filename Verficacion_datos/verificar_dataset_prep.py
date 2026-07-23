"""
Script de verificacion del dataset final de entrenamiento.
Comprueba que dataset_original y dataset_denoised, tras todo el proceso
de preparacion (normalizacion de nombres, conversion a bounding boxes,
division train/val/test), estan correctamente organizados:

 1) Cada imagen tiene su archivo de anotacion (.txt) correspondiente.
 2) No hay paginas duplicadas dentro de cada split.
 3) dataset_original y dataset_denoised usan exactamente las mismas
    paginas en cada split (train, val, test), para que la comparacion
    entre ambos sea justa.
"""

import os
import re

# --- CONFIGURACION ---
ruta_base = "/home/salvarado/TFM/Dataset_preparados/dataset_kanji_prep"
versiones = ["dataset_original", "dataset_denoised"]
splits = ["train", "val", "test"]


def nombre_base(nombre_archivo):
    """Quita la extension y el sufijo 'denoised' para poder comparar
    el mismo nombre de pagina entre ambas versiones del dataset."""
    n = os.path.splitext(nombre_archivo)[0]
    n = re.sub(r"denoised$", "", n)
    return n


# Guardamos aqui los nombres de cada split, para comparar original vs denoised al final
paginas_por_split = {v: {} for v in versiones}

print("=" * 60)
print("PASO 1: Comprobar que cada imagen tiene su label, y viceversa")
print("=" * 60)

for version in versiones:
    print(f"\n--- {version} ---")
    for split in splits:
        ruta_images = os.path.join(ruta_base, version, "images", split)
        ruta_labels = os.path.join(ruta_base, version, "labels", split)

        imagenes = [f for f in os.listdir(ruta_images) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
        labels = [f for f in os.listdir(ruta_labels) if f.lower().endswith(".txt")]

        nombres_img = set(os.path.splitext(f)[0] for f in imagenes)
        nombres_lbl = set(os.path.splitext(f)[0] for f in labels)

        sin_label = nombres_img - nombres_lbl
        sin_imagen = nombres_lbl - nombres_img

        estado = "OK" if not sin_label and not sin_imagen else "REVISAR"
        print(f"  {split}: {len(imagenes)} imagenes, {len(labels)} labels -> {estado}")
        if sin_label:
            print(f"    Imagenes sin label: {sin_label}")
        if sin_imagen:
            print(f"    Labels sin imagen: {sin_imagen}")

        # Guardamos los nombres base (sin 'denoised') para el paso 3
        paginas_por_split[version][split] = set(nombre_base(f) for f in imagenes)


print("\n" + "=" * 60)
print("PASO 2: Comprobar que no hay paginas duplicadas dentro de cada split")
print("=" * 60)

for version in versiones:
    print(f"\n--- {version} ---")
    for split in splits:
        ruta_images = os.path.join(ruta_base, version, "images", split)
        imagenes = [f for f in os.listdir(ruta_images) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
        bases = [nombre_base(f) for f in imagenes]
        duplicados = set([b for b in bases if bases.count(b) > 1])
        if duplicados:
            print(f"  {split}: DUPLICADOS ENCONTRADOS -> {duplicados}")
        else:
            print(f"  {split}: sin duplicados ({len(set(bases))} paginas unicas)")


print("\n" + "=" * 60)
print("PASO 3: Comprobar que original y denoised usan las mismas paginas")
print("=" * 60)

for split in splits:
    set_orig = paginas_por_split["dataset_original"][split]
    set_den = paginas_por_split["dataset_denoised"][split]
    if set_orig == set_den:
        print(f"  {split}: IDENTICO ({len(set_orig)} paginas coinciden en ambas versiones)")
    else:
        print(f"  {split}: DIFERENTE")
        print(f"    Solo en original: {set_orig - set_den}")
        print(f"    Solo en denoised: {set_den - set_orig}")

print("\n" + "=" * 60)
print("VERIFICACION FINALIZADA")
print("=" * 60)