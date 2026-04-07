from fastapi import FastAPI,File,UploadFile
import uvicorn
from PIL import Image
import numpy as np
import io
import tensorflow as tf


app=FastAPI()
model=tf.keras.models.load_model('model.keras' ,compile=False)
class_names=['Early Blight','Late Blight','Healthy']
@app.get("/")
async def home():
    return {"status": "Server is running", "message": "Go to /docs to test the API"}

@app.post("/uploadfile")
async def upload_file(file: UploadFile):
    print(f'file name:{file.filename}')
    content=await file.read()
    image=Image.open(io.BytesIO(content))
    array=np.array(image)
    img=tf.image.resize(array,(256,256))
    img=np.expand_dims(img,0)
    prediction=model.predict(img)
    index=np.argmax(prediction[0])
    return {'prediction':class_names[index]}
        
