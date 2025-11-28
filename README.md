🕊️ Bird vs Drone Classifier
A deep learning project that classifies images as either birds or drones using a custom-trained CNN model. Built with care, deployed with clarity, and designed for real-world use.

📌 Project Overview
This project aims to distinguish between birds and drones in aerial imagery—a task relevant to wildlife monitoring, airspace safety, and surveillance. The model was trained on a curated dataset and deployed using Streamlit Cloud for interactive use.

🧠 Model Architecture
- Type: Convolutional Neural Network (CNN)
- Framework: TensorFlow / Keras
- Input Size: 224 × 224 RGB images
- Output: Binary classification (Bird or Drone)
- Activation: Sigmoid
- Loss Function: Binary Crossentropy

🧪 Dataset
- Source: Custom dataset of bird and drone images
- Preprocessing: Resizing, normalization, data augmentation
- Split: Training and validation sets

🚀 Deployment
The model is deployed using Streamlit, allowing users to upload an image and receive a prediction with confidence score.
🔗 Live App: https://bird-vs-drone-classifier-4raeuohpt4bxhmvybj6eee.streamlit.app/

📓 Google Colab Notebook
The full training pipeline, model saving, and deployment setup are documented in the Colab notebook.
🔗 Colab Notebook:https://colab.research.google.com/drive/1Y99DiJGSDAFsVoR5t2UAY3fjz_PPkFPM?usp=sharing

📂 Model File
The trained model is hosted on Google Drive and downloaded dynamically in the app.

🔗 [Bird vs Drone Model classifier]:
https://drive.google.com/drive/folders/1UhERI06oZ9RoV-o7W6tRNUwyiPUM3kRj?usp=sharing



💡 Features
- Upload .jpg, .jpeg, or .png images
- Real-time prediction with confidence score
- Lightweight deployment using tensorflow-cpu
- Model hosted via Google Drive and downloaded with gdown


🌟 Reflections
This project taught me how to:
- Build and train CNNs from scratch
- Handle deployment challenges with Streamlit
- Manage model hosting and dynamic loading
- Blend technical precision with emotional clarity







