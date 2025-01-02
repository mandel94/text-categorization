from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
from categorizer import Categorizer

# Example cinema categories for index
INDEX = {
    "Drama": "Movies with intense, emotional, and realistic storytelling.",
    "Comedy": "Movies filled with humor and light-hearted storytelling.",
    "Horror": "Movies that aim to scare and thrill the audience.",
    "Action": "Movies packed with high-energy scenes and physical feats."
}

app = FastAPI()
categorizer = Categorizer(INDEX)
summarizer = pipeline("summarization")

class TextRequest(BaseModel):
    text: str
    method: str = "chunk"  # chunk, summary, or full

@app.post("/categorize")
def categorize_text(request: TextRequest):
    try:
        category = categorizer.assign_category(
            request.text, method=request.method, summarizer=summarizer
        )
        return {"category": category}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
