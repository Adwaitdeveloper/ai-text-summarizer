from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline
import torch  # Make sure torch is installed

# 1. Initialize the FastAPI app
app = FastAPI()

# 2. Add CORS middleware to allow your index.html (frontend)
# to communicate with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (e.g., your "Go Live" server)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (POST, GET, etc.)
    allow_headers=["*"],  # Allows all headers
)

# 3. Load the AI model (this happens once, on startup)
print("Loading AI model... This might take a moment. Please wait.")
try:
    # This downloads the model from Hugging Face
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    print("Model loaded successfully. Server is ready.")
except Exception as e:
    print(f"CRITICAL ERROR: Failed to load model: {e}")
    summarizer = None

# 4. Define the data models for the request and response
# This tells FastAPI what the JavaScript data will look like
class TextIn(BaseModel):
    text: str

class SummaryOut(BaseModel):
    summary: str

# 5. This is the API endpoint your JavaScript is trying to call
@app.post("/summarize", response_model=SummaryOut)
def summarize_text(data: TextIn):
    """
    Receives text from the frontend and returns a summary.
    """
    if summarizer is None:
        # This error will be sent back to the JavaScript
        return {"summary": "Error: The AI model is not running on the server. Check the server console for errors."}
    
    raw_text = data.text
    
    # Run the AI model to get the summary
    summary_list = summarizer(raw_text, max_length=150, min_length=30, do_sample=False)
    
    # Extract the summary text
    summary_str = summary_list[0]['summary_text']
    
    # Send the summary back to the JavaScript
    return {"summary": summary_str}

# 6. This is the root endpoint for testing
@app.get("/")
def read_root():
    return {"message": "AI Summarizer API is running!"}

