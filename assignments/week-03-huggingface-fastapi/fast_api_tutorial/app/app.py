from fastapi import FastAPI
<<<<<<< HEAD
<<<<<<< HEAD
from pydantic import BaseModel
from typing import List
from transformers import pipeline

pipeline = pipeline(model="model/t5-small") # complete this line with the code to load the pipeline from the local file

app = FastAPI()

class TextToTranslate(BaseModel):
    input_text: str

class TextsToTranslate(BaseModel):
    input_texts: List[str]

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/echo")
def echo(text_to_translate: TextToTranslate):
    return {"message": text_to_translate.input_text}

@app.post("/translate")
def translate(texts_to_translate: TextsToTranslate):
    return {"message": pipeline(texts_to_translate.input_texts)}

=======
=======
>>>>>>> 1cb1d3d8b04ec2e0cde4dcac2a9dfe6de6b0ba77

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}
    
<<<<<<< HEAD
>>>>>>> 2a1bf3e1fb8d0f8fc0edda941b7d6c0efd16de43
=======
>>>>>>> 1cb1d3d8b04ec2e0cde4dcac2a9dfe6de6b0ba77
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)