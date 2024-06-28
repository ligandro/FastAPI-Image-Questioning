from model import model_pipeline

from typing import Union
import uvicorn
from fastapi import FastAPI, UploadFile

import io
from PIL import Image

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/ask")
def ask(text: str, image: UploadFile):
    content = image.file.read()
    
    image = Image.open(io.BytesIO(content))
    # image = Image.open(image.file)
    
    result = model_pipeline(text, image)
    return {"answer": result}
    
    
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)  
    
