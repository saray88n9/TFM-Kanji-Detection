import os
os.chdir("/home/salvarado/TFM/Mamba-YOLO")
from ultralytics import YOLO

model = YOLO("/home/salvarado/TFM/resultados/result_mambayolo/imagen_completa_denoised_1600_50ep_M/weights/best.pt")

metrics = model.val(
    data="/home/salvarado/TFM/Dataset_preparados/dataset_kanji_prep/dataset_denoised/dataset_denoised.yaml",
    split="test",
    imgsz=1600,
    batch=1,
    device="2"
)

print("Resultados MambaYOLO-B Imagen Completa Denoised - Test")
print("-" * 50)
print(f"Precisión : {metrics.box.mp:.3f}")
print(f"Recall    : {metrics.box.mr:.3f}")
print(f"mAP50     : {metrics.box.map50:.3f}")
print(f"mAP50-95  : {metrics.box.map:.3f}")