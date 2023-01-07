from fastapi import FastAPI
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


app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)