import streamlit as st
from tensorflow import keras
import numpy as np
from PIL import Image
import gdown
import os

# Download model from Google Drive (only once)
model_path = "bird_vs_drone_model.keras"
if not os.path.exists(model_path):
    url = "https://drive.google.com/uc?id=11-yOcHcaHrp98JdrRAc1t9kSd1pCo5aw"
    gdown.download(url, model_path, quiet=False)

# Load your trained model
model = keras.models.load_model(model_path)

# Map prediction to label
idx_to_class = {0: "bird", 1: "drone"}

# Title
st.title("🕊️ Bird vs Drone Classifier")

# Upload image
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess image
    img = image.resize((224, 224))  # match your model's input size
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # shape: (1, 224, 224, 3)

    # Predict
    prediction = model.predict(img_array)[0][0]
    label = "drone" if prediction > 0.5 else "bird"
    confidence = prediction if label == "drone" else 1 - prediction

    # Show result
    st.markdown(f"### Prediction: **{label.upper()}**")
    st.markdown(f"Confidence: **{confidence:.2f}**")
