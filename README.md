# Potato Leaf Disease Detection API

A Deep Learning-based API built with **FastAPI** and **TensorFlow** to classify potato leaf diseases. This project identifies whether a potato leaf is Healthy or affected by Early/Late Blight.

## 🚀 Features
- **FastAPI Backend**: Optimized for high-speed image processing.
- **Deep Learning**: Uses a Keras model for accurate classification.
- **Port 8001**: Pre-configured to run on port 8001 to avoid common port conflicts.

## 🛠️ Tech Stack
- **Framework**: FastAPI
- **Model**: TensorFlow / Keras
- **Image Handling**: Pillow (PIL), NumPy
- **Server**: Uvicorn

## 📥 Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-link>
   cd potato-disease-project

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

### 🏃 How to Run
    Start the FastAPI server on port 8001:
    bash
    uvicorn main:app --host 127.0.0.1 --port 8001 --reload

### 🧪 Testing the API
    Open your browser and go to: http://127.0.0
    Locate the /uploadfile POST endpoint.
    Click "Try it out", upload a potato leaf image, and click "Execute".
    The API will return a JSON response: {"prediction": "Early Blight"}
