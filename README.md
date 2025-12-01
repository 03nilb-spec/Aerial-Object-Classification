# Aerial-Object-Detection
---
This Project aims to develop a deep learning solution that can classify aerial images into two categories 'Bird' and 'Drone'.

## Project Overview 
- The project classifies the aerial images into two categries:
      Bird
      Drone
- It helps in security survillance, wildlife protection, and airspace safety where accurate classification of birds and drone is critical.
- In this project, Custom CNN with 3 and 4 Layers is used for builing a model from scratch.
- For transfer learning. pre-trained models like MobileNetV2 and InceptionV3 is used.
- Both the pre-trained models had an awesome accuracy and overall metrics, but for Custom CNN it isn't that good as expected.
---
## Features 
- Upload an aerial image and get instant classification
- Deep Learning model based on MobileNetV2
- Lightweight and optimized for fast inference
- Clean Streamlit-based user interface
- Easy to run locally
---
## Model Training 
- Base Model: MobileNetV2 (ImageNet pre-trained)
- Image Size: 224 × 224
- Optimizer: Adam
- Loss Function: categorical_crossentropy
- Metrics: accuracy
- Training performed on Jupyter notebook
- You can find the training notebook inside the Notebooks folder.
---
## Results 
|Model|	Accuracy	|Precision	|Recall|	F1_score|
|-|-|-|-|-|
|InceptionV3	|0.99	|0.98	|1.00	|0.99|
|MobileNetV2	|0.99	|0.98	|1.00	|0.99|
|Custom CNN	|0.51	|0.58	|0.53	|0.55|
---
## Future Imporvements 
- Add more classes (Planes, Helicopters, UAV types)
- Implement real-time object detection (YOLOv8 / SSD / Faster R-CNN)
---

## Author 
**Nilesh Bahirgaonkar**
 
Data Scientist & Enthusiast
