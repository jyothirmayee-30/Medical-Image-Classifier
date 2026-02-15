# Medical Image Classifier 📸

A deep learning application that analyzes chest X-ray images to provide automated screening for common pulmonary conditions using CNNs.

## Description
A deep learning application that analyzes chest X-ray images to provide automated screening for common pulmonary conditions using Convolutional Neural Networks for high-accuracy feature extraction.

## Key Features
- **Automated Screening:** Detects signs of pneumonia, infiltration, and nodules in X-ray scans.
- **Heatmap Visualization:** Uses Grad-CAM to highlight specific regions of the image influencing the AI’s decision.
- **DICOM Integration:** Supports standard medical imaging formats for seamless clinical workflow integration.

## Tech Stack
- **Language:** Python
- **Libraries:** Keras, TensorFlow, OpenCV, Streamlit, NumPy
- **Model:** DenseNet-121 or ResNet-50 pre-trained on the ChestX-ray14 dataset.

## Engineering Logic
- **Backend:** The system performs image normalization and data augmentation before passing the pixel data through a deep CNN to extract spatial features.
- **Software Engine:** A Streamlit dashboard allows doctors to upload an X-ray and receive a probability score across multiple diagnostic categories within seconds.
