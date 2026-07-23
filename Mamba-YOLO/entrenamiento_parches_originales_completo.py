import os
os.chdir("/home/salvarado/TFM/Mamba-YOLO")
from ultralytics import YOLO

model_conf = "ultralytics/cfg/models/mamba-yolo/Mamba-YOLO-B.yaml"

args = {
    "data": "/home/salvarado/TFM/Dataset_preparados/dataset_kanji_parches/originales/dataset_parches_originales.yaml",
    "epochs": 50,
    "batch": 2,
    "imgsz": 1024,
    "patience": 10,
    "seed": 42,
    "device": "0",
    "amp": True,
    "project": "/home/salvarado/TFM/resultados/result_mambayolo",
    "name": "parches_original_1024_50ep_M",
}

YOLO(model_conf).train(**args)