import os

ruta_base = "/home/salvarado/TFM/Dataset_preparados/dataset_kanji_parches"

for version in ["denoised", "originales"]:
    print(f"\n{version}:")

    for split in ["train", "val", "test"]:
        ruta_images = os.path.join(ruta_base, version, "images", split)
        ruta_labels = os.path.join(ruta_base, version, "labels", split)

        imagenes = os.listdir(ruta_images)
        labels = os.listdir(ruta_labels)

        # nombres sin extension, para poder comparar
        nombres_img = set(f.split(".")[0] for f in imagenes)
        nombres_lbl = set(f.split(".")[0] for f in labels)

        todo_bien = nombres_img == nombres_lbl

        print(f"  {split}: {len(imagenes)} imagenes, {len(labels)} labels -> {'OK' if todo_bien else 'REVISAR'}")