# Detección de Kanjis en manuscritos japoneses mediante Deep Learning

Repositorio correspondiente al Trabajo Final de Máster (TFM) del Máster en Ciencia de Datos de la Universitat de Girona.

DESCRIPCIÓN DEL PROYECTO

Este proyecto tiene como objetivo estudiar la detección automática de caracteres Kanji presentes en manuscritos japoneses históricos de la colección Sakuma del dataset YUWasanDB mediante modelos de detección de objetos basados en Deep Learning.

El trabajo analiza diferentes arquitecturas de detección de objetos y estrategias de procesamiento de imágenes para localizar caracteres Kanji dentro de documentos manuscritos de gran resolución.


MODELOS EVALUADOS

Durante el desarrollo del proyecto se evaluaron los siguientes modelos de detección de objetos:

- YOLO
- RT-DETR
- RF-DETR
- Mamba-YOLO

Además, se compararon diferentes estrategias de entrada:

- Imágenes completas de los manuscritos.
- División de imágenes en parches.
- Imágenes originales y versiones con eliminación de ruido.


ESTRUCTURA DEL REPOSITORIO

El repositorio está organizado de la siguiente manera:

- notebooks_yolo/
  Contiene los notebooks utilizados para entrenamiento, inferencia y evaluación de YOLO.

- notebooks_RT_DTR/
  Contiene los notebooks utilizados para entrenamiento y evaluación de RT-DETR.

- noteboosks_RF_DTR/
  Contiene los notebooks utilizados para entrenamiento y evaluación de RF-DETR.

- Mamba-YOLO/
  Contiene los scripts desarrollados para el entrenamiento y evaluación de Mamba-YOLO.

- Verficacion_datos/
  Contiene los scripts utilizados para la preparación y validación de los datos.


DATASET

El proyecto utiliza el dataset YUWasanDB, concretamente la colección Sakuma, formada por imágenes de manuscritos japoneses históricos.

Los datos originales, datasets preparados y modelos entrenados no se incluyen en este repositorio debido a su tamaño.


TECNOLOGÍAS UTILIZADAS

- Python
- PyTorch
- CUDA
- Ultralytics
- YOLO
- RT-DETR
- RF-DETR
- Mamba-YOLO


REQUISITOS

Para ejecutar los experimentos es necesario disponer de un entorno Python con las dependencias necesarias para cada arquitectura y soporte para GPU NVIDIA con CUDA.

Las configuraciones utilizadas durante los entrenamientos se encuentran definidas en los notebooks incluidos en el repositorio.


EJECUCIÓN

Los notebooks contienen el flujo completo seguido durante el desarrollo del proyecto:

1. Preparación y transformación de los datos.
2. Entrenamiento de los modelos de detección.
3. Evaluación utilizando el conjunto de prueba.
4. Cálculo de métricas de detección.
5. Generación de predicciones.


RESULTADOS

Los experimentos realizados permiten comparar el rendimiento de diferentes modelos de detección de objetos aplicados a la localización automática de Kanjis en manuscritos históricos.

Los resultados detallados y el análisis de las métricas obtenidas se encuentran descritos en la memoria del Trabajo Final de Máster.


AUTOR

Natalia Alvarado

Trabajo Final de Máster
Máster en Ciencia de Datos
Universitat de Girona
