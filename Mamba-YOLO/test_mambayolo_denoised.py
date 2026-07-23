import os
os.chdir("/home/salvarado/TFM/Mamba-YOLO")
from ultralytics import YOLO

model = YOLO("/home/salvarado/TFM/resultados/result_mambayolo/parches_denoised_1024_50ep_M/weights/best.pt")

metrics = model.val(
    data="/home/salvarado/TFM/Dataset_preparados/dataset_kanji_parches/denoised/dataset_parches_denoised.yaml",
    split="test",
    imgsz=1024,
    batch=2,
    device="0"
)

print("Resultados MambaYOLO-B Parches Denoised - Test")
print("-" * 45)
print(f"Precisión : {metrics.box.mp:.3f}")
print(f"Recall    : {metrics.box.mr:.3f}")
print(f"mAP50     : {metrics.box.map50:.3f}")
print(f"mAP50-95  : {metrics.box.map:.3f}")
