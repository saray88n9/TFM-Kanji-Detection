import os
os.chdir("/home/salvarado/TFM/Mamba-YOLO")
from ultralytics import YOLO

model_conf = "ultralytics/cfg/models/mamba-yolo/Mamba-YOLO-B.yaml"

args = {
    "data": "/home/salvarado/TFM/Dataset_preparados/dataset_kanji_parches/denoised/dataset_parches_denoised.yaml",
    "epochs": 50,
    "batch": 2,
    "imgsz": 1024,
    "patience": 10,
    "seed": 42,
    "device": "1",
    "amp": True,
    "project": "/home/salvarado/TFM/resultados/result_mambayolo",
    "name": "parches_denoised_1024_50ep_M",
}

YOLO(model_conf).train(**args)