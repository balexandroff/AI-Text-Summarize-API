from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Initialize FastAPI app
app = FastAPI(title="Text Summarization API", version="1.0")

# Define request model
class TextInput(BaseModel):
    text: str

@app.post("/api/summarize")
def summarize_text(input: TextInput):
    try:
        summary = summarizer(input.text, max_length=150, min_length=50, do_sample=False)
        return {"summary": summary[0]["summary_text"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Health check
@app.get("/")
def root():
    return {"message": "Text Summarization API is running!"}
