import os
os.chdir("/home/salvarado/TFM/Mamba-YOLO")
from ultralytics import YOLO

model_conf = "ultralytics/cfg/models/mamba-yolo/Mamba-YOLO-T.yaml"

args = {
    "data": "/home/salvarado/TFM/Dataset_preparados/dataset_kanji_parches/originales/dataset_parches_originales.yaml",
    "epochs": 1,
    "batch": 16,
    "device": "0",
    "amp": True,
    "project": "/home/salvarado/TFM/resultados/result_mambayolo",
    "name": "prueba_servidor_sm61",
}

YOLO(model_conf).train(**args)