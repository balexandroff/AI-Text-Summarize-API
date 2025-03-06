from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

app = FastAPI(title="Text Summarization API", version="1.0")

class TextInput(BaseModel):
    text: str

# Function to split text into 1024-token chunks
def chunk_text(text, max_tokens=1024):
    words = text.split()
    chunks = [" ".join(words[i:i + max_tokens]) for i in range(0, len(words), max_tokens)]
    return chunks

@app.post("/api/summarize")
def summarize_text(input: TextInput):
    try:
        text_chunks = chunk_text(input.text, max_tokens=1000)  # Use 1000 to be safe
        summaries = [summarizer(chunk, max_length=250, min_length=100, do_sample=False)[0]["summary_text"] for chunk in text_chunks]
        
        return {"summary": " ".join(summaries)}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "Text Summarization API is running!"}
