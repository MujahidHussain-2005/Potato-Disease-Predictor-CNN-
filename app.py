import streamlit as st
import requests
from PIL import Image
import io

# Backend URL
API_URL = "http://127.0.0.1:8001/uploadfile"

st.title("Leaf Disease Detector")
st.write("Upload a leaf image to detect Early Blight, Late Blight, or Healthy.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Leaf', use_container_width=True)
    
    if st.button('Analyze Leaf'):
        st.write("Analyzing...")
        
        # Prepare file to send to API
        files = {"file": uploaded_file.getvalue()}
        
        # Send to FastAPI backend
        try:
            response = requests.post(API_URL, files=files)
            result = response.json()
            
            st.success(f"Prediction: {result['prediction']}")
        except Exception as e:
            st.error(f"Error connecting to backend: {e}")
